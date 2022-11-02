from . import views
from django.urls import path
from booking import views


urlpatterns = [
    path('', views.BookingList.as_view(), name="home"),
    path('news/', views.News.as_view(), name="news"),
    path('booking/', views.Create_Booking.as_view(), name="booking"),
    path('booking/<item_id>/edit/', views.edit_booking, name='edit_booking'),
    path('delete/<item_id>', views.delete_booking, name='delete'),
]
