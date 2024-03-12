from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoCreteForm
from petstagram.photos.models import Photo


def create_photo(request):
    form = PhotoCreteForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('photo_details', form.instance.pk)

    context = {
        'form': form
    }
    return render(request, "photos/photo-add-page.html", context)


def photo_details(request, pk):
    context = {
        'pet_photo': Photo.objects.get(pk=pk)
    }
    return render(request, "photos/photo-details-page.html", context)


def photo_edit_page(request, pk):
    context = {}
    return render(request, "photos/photo-edit-page.html", context)


def photo_delete(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('index')
