from . import views
from django.urls import path
from booking.views import News, Create_Booking


urlpatterns = [
    path('', views.BookingList.as_view(), name="home"),
    path('news/', views.News.as_view(), name="news"),
    path('booking/', views.Create_Booking.as_view(), name="booking"),
]
