from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.base import View
from django.db.models.query import QuerySet
from django.contrib import messages
from .models import Booking
from .forms import BookingForm, EditBookingForm


class BookingList(generic.ListView):
    model = Booking
    template_name = "index.html"
    paginate_by = 6


class News(View):
    def get(self, request, *args, **kwargs):
        all_bookings = Booking.objects.all()

        return render(
            request,
            "news.html",
        )


class Create_Booking(View):
    def get(self, request, *args, **kwargs):
        all_bookings = Booking.objects.all().order_by("booking_date", "booking_time")

        return render(
            request,
            "booking.html",
            {
                "bookingform": BookingForm(),
                "all_bookings": all_bookings,
            },
        )

    def post(self, request, *args, **kwargs):
        all_bookings = Booking.objects.all()

        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():

            booking_form.instance.email = request.user.email
            booking = booking_form.save(commit=False)

            booking_exists = Booking.objects.filter(
                booking_date=booking.booking_date, booking_time=booking.booking_time).exists()
            print(booking_exists)
            if booking_exists is False:
                print(request.user)
                print(request.user.id)
                booking.user_id = request.user
                booking.save()
                messages.warning(
                    request, 'booking succesful see your booking in view booking')
                return render(request, "index.html")
            else:
                messages.error(request, 'time and date slots are already used')
        messages.error(request, "Form not valid")
        return render(
            request,
            "booking.html",
            {
                "bookingform": BookingForm(),
            },
        )


def edit_booking(request, item_id):
    booking = get_object_or_404(Booking, id=item_id)
    if request.method == 'POST':
        form = EditBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking')
    form = EditBookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)


def delete_booking(request, item_id):
    booking = get_object_or_404(Booking, id=item_id)
    booking.delete()
    return redirect('booking')
