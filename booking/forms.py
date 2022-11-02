from django import forms
from django.forms import ModelForm
from .models import Booking


TIME_SLOTS = \
    [('09:00', '09:00'),
     ('10:00', '10:00'),
     ('11:00', '11:00'),
     ('12:00', '12:00'),
     ('13:00', '13:00'),
     ('14:00', '14:00'),
     ('15:00', '15:00'),
     ('16:00', '16:00')]


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('first_name', 'last_name', 'booking_date', 'booking_time',
                  'email', 'phone_number', 'what_they_would_like_to_do',
                  'assigned_staff_member',)
        widgets = {
            'booking_date': DateInput(),
        }

    booking_time = forms.ChoiceField(choices=TIME_SLOTS)
