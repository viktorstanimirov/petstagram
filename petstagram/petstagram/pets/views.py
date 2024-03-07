from django.shortcuts import render, redirect

from petstagram.pets.forms import PetCreateForm, PetEditForm
from petstagram.pets.models import Pet


def create_pet(request):
    pet_form = PetCreateForm(request.POST or None)

    if request.method == 'POST':
        if pet_form.is_valid():
            created_pet = pet_form.save()
            return redirect('pet details', username='Viktor', pet_slug=created_pet.slug)

    context = {
        'pet_form': pet_form,
    }
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
    pet = Pet.objects.filter(slug=pet_slug).get()

    pet_form = PetEditForm(request.POST or None)

    if request.method == 'POST':
        if pet_form.is_valid():
            updated_pet = pet_form.save()
            return redirect('pet details', username=username, pet_slug=pet_slug)

    context = {
        'pet_form': pet_form,
        'username': username,
        'pet': pet,

    }
    return render(request, "pets/edit_pet.html", context)


def delete_pet(request, username, pet_slug):
    context = {}
    return render(request, "pets/delete_pet.html", context)
