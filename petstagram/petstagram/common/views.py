from django.shortcuts import render
from django.views import generic as views

from petstagram.photos.models import Photo


def index(request):
    pet_photos = Photo.objects.all()
    context = {
        'pet_photos': pet_photos
    }
    return render(request, "common/index.html", context)


# class IndexView(views.ListView):
#     queryset = Photo.objects.all() \
#         .prefetch_related("pets") \
#         .prefetch_related("photolike_set")
#
#     template_name = "common/index.html"
