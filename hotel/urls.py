from django.urls import path
from . import views

urlpatterns = [
    path('hotel/list/', views.HotelListView.as_view()),
    path('hotel/<int:pk>/', views.HotelDetailView.as_view()),
    path('hotel/create/', views.HotelCreateView.as_view()),
    path('room/list/', views.RoomListView.as_view()),
    path('room/<int:pk>/', views.RoomDetailView.as_view()),
    path('room/create/', views.RoomCreateView.as_view()),
    path('booking/list/', views.BookingListView.as_view()),
    path('booking/<int:pk>/', views.BookingDetailView.as_view()),
    path('booking/create/', views.BookingCreateView.as_view()),
]
