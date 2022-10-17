from django.shortcuts import render
from django.views import generic
from .models import Booking
from django.views.generic.base import View


class BookingList(generic.ListView):
    model = Booking
    template_name = "index.html"
    paginate_by = 6


class News(View):

    def get(self, request, *args, **kwargs):
        # queryset = Post.objects.filter(status=1)
        # post = get_object_or_404(queryset, slug=slug)
        # comments = post.comments.filter(approved=True).order_by("-created_on")
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
