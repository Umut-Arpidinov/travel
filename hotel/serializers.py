from rest_framework import fields, serializers
from .models import Hotel, Rooms, Booking

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id',"title", "location", "contacts", "hotel_picture")


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ('id',"room_no", "price", "hotel", "is_booked")


class BookingSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer
    room = RoomSerializer
    class Meta:
        model = Booking
        fields =('id',"user", "hotel", "room", "checkin_date", "checkout_date",)

