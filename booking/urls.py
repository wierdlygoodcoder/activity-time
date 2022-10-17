from . import views
from django.urls import path
from booking.views import News


urlpatterns = [
    path('', views.BookingList.as_view(), name='home'),
    path('news/', News.as_view(), name="news")
]
