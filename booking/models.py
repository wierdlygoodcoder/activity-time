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

staff_members = \
    [('1', 'Gareth'),
     ('2', 'Emily'),
     ('3', 'Rodger'),
     ('4', 'Greg'),
     ('5', 'Alan'),
     ('6', 'Stevephen'),
     ('7', 'Patrick')]


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    booking_date = models.DateField(auto_now_add=False)
    booking_time = models.TimeField(max_length=30)
    email = models.EmailField(max_length=100,)
    phone_number = PhoneNumberField(blank=True, region="GB")
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="users_ids"
    )
    what_they_would_like_to_do = models.CharField(max_length=50,
                                                  choices=activity_choices,
                                                  default='bulding models')
    assigned_staff_member = models.CharField(max_length=50,
                                             choices=staff_members,
                                             default='Greg')

    class Meta:
        unique_together = [['booking_date', 'booking_time']]

    def __str__(self):
        return self.first_name
