from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Booking


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
            'booking_time': TimeInput(),
        }

    # def clean(self):
    #     booking_date = self.cleaned_data['booking_date']
    #     if Booking.objects.filter(booking_date=booking_date).exists():
    #         raise ValidationError("bookings already exists")
    #     return render(request, "booking.html")
