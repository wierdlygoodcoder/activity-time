from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime

activity_choices = \
    [('buliding models', 'painting models'),
     ('playing wargames', 'need specific pating addvice'),
     ('understanding how to play certain games', 'advice on canvas poainting')]


class Booking(models.Model):
    first_name = models.CharField(max_length=200, unique=True)
    last_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    booking_date = models.DateTimeField(auto_now_add=False)
    email = models.EmailField(max_length=100,)
    moblie = models.IntegerField(max_length=11,)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="users_ids"
    )
    what_they_would_like_to_do = models.CharField(max_length=50,
                                                  choices=activity_choices,
                                                  default='bulding models')
