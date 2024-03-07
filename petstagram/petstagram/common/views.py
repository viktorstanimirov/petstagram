from django.shortcuts import render, redirect

from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo


def index(request):
    pet_photos = Photo.objects.all()
    context = {
        'pet_photos': pet_photos
    }
    return render(request, "common/index.html", context)


def like_pet_photo(request, pk):
    pet_photo_like = PhotoLike.objects.filter(pet_photo_id=pk).first()

    if pet_photo_like:
        pet_photo_like.delete()
    else:
        PhotoLike.objects.create(pet_photo_id=pk)

    return redirect('photo_details', pk=pk)