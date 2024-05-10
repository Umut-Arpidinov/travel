# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from account.serializers import UserSerializer

# from .models import Hotel, Rooms, Booking, User
# from .serializers import HotelSerializer, RoomSerializer, BookingSerializer

# from collections import namedtuple


# nt = namedtuple("object", ["model", "serializers"])
# pattern = {
# "guest" : nt(User, UserSerializer),
# "hotel" : nt(Hotel, HotelSerializer),
# "room" : nt(Rooms, RoomSerializer),
# "booking": nt(Booking, BookingSerializer),
# }

# @api_view(["GET", "POST"]) 
# def ListView(request, api_name): 
#     object = pattern.get(api_name, None)
#     if object == None:
#         return Response(
#         data = "Invalid URL",
#         status = status.HTTP_404_NOT_FOUND,
#         )
#     if request.method == "GET":
#         object_list = object.model.objects.all()
#         serializers = object.serializers(object_list, many=True)
#         return Response(serializers.data)

#     if request.method == "POST":
#         data = request.data
#         serializers = object.serializers(data=data)

#     if not serializers.is_valid():
#         return Response(
#         data = serializers.error,
#         status = status.HTTP_404_NOT_FOUND
#         )
#     serializers.save()
#     return Response(
#     data = serializers.error,
#     status = status.HTTP_201_CREATED
#     )

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import generics
from .models import Hotel, Rooms, Booking
from .serializers import HotelSerializer, RoomSerializer, BookingSerializer
from rest_framework import permissions

class HotelListView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get_permissions(self):
        return [permissions.AllowAny()]

class HotelDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    def get_permissions(self):
        return [permissions.AllowAny()]

class HotelCreateView(generics.CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    def get_permissions(self):
        return [permissions.AllowAny()]


class RoomListView(generics.ListAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer
    def get_permissions(self):
        return [permissions.AllowAny()]

class RoomDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer
    def get_permissions(self):
        return [permissions.AllowAny()]

class RoomCreateView(generics.CreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer
    def get_permissions(self):
        return [permissions.AllowAny()]

class BookingListView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    def get_permissions(self):
        return [permissions.AllowAny()]

class BookingDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    def get_permissions(self):
        return [permissions.AllowAny()]

class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    def get_permissions(self):
        return [permissions.AllowAny()]
