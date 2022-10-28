from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.base import View
from django.db.models.query import QuerySet
from .models import Booking
from .forms import BookingForm


class BookingList(generic.ListView):
    model = Booking
    template_name = "index.html"
    paginate_by = 6


class News(View):
    def get(self, request, *args, **kwargs):
        all_bookings = Booking.objects.all()
        # post = get_object_or_404(queryset)
        # comments =
        # post.comments.filter(approved=True).order_by("-created_on")
        # liked = False
        # if post.likes.filter(id=self.request.user.id).exists():
        #     liked = True

        return render(
            request,
            "news.html",
            # {
            #     "post": post,
            #     "comments": comments,
            #     "commented": False,
            #     "liked": liked,
            #     "comment_form": CommentForm()
            # },
        )


class Create_Booking(View):
    def get(self, request, *args, **kwargs):
        all_bookings = Booking.objects.all()
        # post = get_object_or_404(queryset)
        # comments =
        # post.comments.filter(approved=True).order_by("-created_on")
        # liked = False
        # if post.likes.filter(id=self.request.user.id).exists():
        #     liked = True
        # print(all_bookings)
        return render(
            request,
            "booking.html",
            {
                # "all_bookings": all_bookings,
                #     "comments": comments,
                #     "commented": False,
                #     "liked": liked,
                "bookingform": BookingForm()
            },
        )

    def post(self, request, *args, **kwargs):
        all_bookings = Booking.objects.all()

        # post = get_object_or_404(all_bookings)
        # comments =
        # post.comments.filter(approved=True).order_by("-created_on")
        # liked = False
        # if post.likes.filter(id=self.request.user.id).exists():
        #     liked = True

        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():

            booking_form.instance.email = request.user.email
            # booking_form.instance.name = request.user.username
            booking = booking_form.save(commit=False)
 
            # booking_exists = Booking.objects.filter(date = booking.date, time=booking.time).exists
            # if booking_exists:
            #   delete booking
            #   message ("clash in bookings")
            # else:
            #   create and add booking

            # add User_Id Field to saved form object before saving & commiting - NL
            # booking.email = request.user.email
            print(request.user)
            print(request.user.id)
            booking.user_id = request.user
            booking.save()

        else:
            booking_form = BookingForm()
        # print(booking.instance.booking_time)
        return render(
            request,
            "index.html",
            {
                # "all_bookings": all_bookings,
                # "comments": comments,
                # "commented": True,
                "bookingform": BookingForm(),
                # "liked": liked
            },
        )
