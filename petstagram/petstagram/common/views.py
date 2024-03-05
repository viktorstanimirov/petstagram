from django.shortcuts import render
from django.views import generic as views

from petstagram.photos.models import Photo


# def home_page(request):
#     all_photos = Photo.objects.all()
#     context = {
#         'all_photos': all_photos
#     }
#     return render(request, "common/home-page.html", context)


class IndexView(views.ListView):
    queryset = Photo.objects.all() \
        .prefetch_related("pets") \
        .prefetch_related("photolike_set")

    template_name = "common/index.html"
