from django import forms
from django.forms import ModelForm

from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('first_name', 'last_name', 'booking_date', 'booking_time',
                  'email', 'phone_number', 'what_they_would_like_to_do',
                  'assigned_staff_member',)
        # widgets = {
        #     'booking_date': forms.SelectDateWidget(
        #          empty_label=("Choose Year", "Choose Month", "Choose Day"),
        #     ),
        #     'booking_time': forms.TimeInput
        #     (attrs={'type': 'time'})
        # }
