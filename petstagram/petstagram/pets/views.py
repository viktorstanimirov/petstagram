from django.shortcuts import render

from petstagram.pets.models import Pet


def create_pet(request):
    context = {}
    return render(request, "pets/create_pet.html", context)


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos,
    }
    return render(request, "pets/details_pet.html", context)


def edit_pet(request, username, pet_slug):
    context = {}
    return render(request, "pets/edit_pet.html", context)


def delete_pet(request, username, pet_slug):
    context = {}
    return render(request, "pets/delete_pet.html", context)
