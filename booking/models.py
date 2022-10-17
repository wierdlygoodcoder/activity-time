from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinLengthValidator
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField
import datetime

activity_choices = \
    [('buliding models', 'Buliding Models'),
     ('painting models', 'Painting Models'),
     ('playing wargames', 'Playing Wargames'),
     ('need specific pating addvice', 'Need Specific Painting Advice'),
     ('understanding how to play certain game',
        'Understanding How To Play Certain Game'),
     ('advice on canvas poainting', 'Advice On Canvas Painting')]

staff_memebers = \
    [('1', 'Gareth'),
     ('2', 'Emily'),
     ('3', 'Rodger'),
     ('4', 'Greg'),
     ('5', 'Alan'),
     ('6', 'Stevephen'),
     ('7', 'Patrick')]


def default_user():
    user = User(username="john", email="john@hotmail.com")
    return user.id


class Booking(models.Model):
    first_name = models.CharField(max_length=200, unique=True)
    last_name = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    booking_date = models.DateTimeField(auto_now_add=False)
    email = models.EmailField(max_length=100,)
    phone_number = PhoneNumberField(blank=True, region="GB")
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="users_ids"
    )
    what_they_would_like_to_do = models.CharField(max_length=50,
                                                  choices=activity_choices,
                                                  default='bulding models')
    whom_with = models.CharField(max_length=50, choices=staff_memebers,
                                 default='Greg')

    def __str__(self):
        return self.first_name
