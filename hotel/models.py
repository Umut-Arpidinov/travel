from django.db import models
from account.models import User 
from datetime import datetime

class Hotel(models.Model):
    title = models.CharField(max_length=150)
    opening_time = models.TimeField(auto_now_add=False, default=datetime.now)
    closing_time = models.TimeField(auto_now_add=False, default=datetime.now)
    location = models.CharField(max_length=200)
    hotel_picture = models.ImageField(upload_to="hotels_pictures", null=True, blank=True)
    contacts = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'

class Rooms(models.Model):
    room_no = models.IntegerField(default=101)
    price = models.FloatField(default=1000.0)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.room_no}'
    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    count_of_guest = models.IntegerField(default=1)
    checkin_date = models.DateField(default=datetime.now)
    checkout_date = models.DateField(default=datetime.now)
    is_checkout = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.checkin_date}  -->  {self.checkout_date}'
