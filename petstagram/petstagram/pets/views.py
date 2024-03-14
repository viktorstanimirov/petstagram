from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


class PetCreateView(views.CreateView):
    model = Pet
    form_class = PetCreateForm
    template_name = "pets/create_pet.html"

    def get_success_url(self):
        return reverse("details_pet", kwargs={
            "username": "Viktor",
            "pet_slug": self.object.slug,
        })


class PetDetailView(views.DetailView):
    model = Pet
    '''Can be used queryset to prefetch related data'''
    # queryset = Pet.objects.all() \
    #     .prefetch_related("petphoto_set") \
    #     .prefetch_related("petphoto_set__photolike_set") \
    #     .prefetch_related("petphoto_set__pets")

    template_name = "pets/details_pet.html"
    slug_url_kwarg = "pet_slug"


class PetEditView(views.UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = "pets/edit_pet.html"

    slug_url_kwarg = "pet_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["username"] = "Doncho"
        return context

    def get_success_url(self):
        return reverse("details pet", kwargs={
            "username": self.request.GET.get("username"),
            "pet_slug": self.object.slug,
        })


class PetDeleteView(views.DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = "pets/delete_pet.html"

    slug_url_kwarg = "pet_slug"

    success_url = reverse_lazy("index")

    extra_context = {
        "username": "Viktor",
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.get_object()
        return kwargs


'''Class Based View For: Create Pet, Details Pet, Edit Pet and Delete Pet'''


# def create_pet(request):
#     pet_form = PetCreateForm(request.POST or None)
#
#     if request.method == "POST":
#         if pet_form.is_valid():
#             created_pet = pet_form.save()
#             return redirect("details_pet", username="Viktor", pet_slug=created_pet.slug)
#
#     context = {
#         "pet_form": pet_form,
#     }
#     return render(request, "pets/create_pet.html", context)


# def details_pet(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#     all_photos = pet.photo_set.all()
#
#     context = {
#         "pet": pet,
#         "all_photos": all_photos,
#
#     }
#     return render(request, "pets/details_pet.html", context)


# def edit_pet(request, username, pet_slug):
#     pet = Pet.objects.filter(slug=pet_slug).get()
#
#     pet_form = PetEditForm(request.POST or None, instance=pet)
#
#     if request.method == "POST":
#         if pet_form.is_valid():
#             updated_pet = pet_form.save()
#             return redirect("details_pet", username=username, pet_slug=pet_slug)
#
#     context = {
#         "pet_form": pet_form,
#         "username": username,
#         "pet": pet,
#     }
#
#     return render(request, "pets/edit_pet.html", context)


# def delete_pet(request, username, pet_slug):
#     pet = Pet.objects.filter(slug=pet_slug).get()
#     pet_form = PetDeleteForm(request.POST or None, instance=pet)
#
#     if request.method == "POST":
#         pet_form.save()
#         return redirect("index")
#
#     context = {
#         "pet_form": pet_form,
#         "username": username,
#         "pet": pet,
#     }
#
#     return render(request, "pets/delete_pet.html", context)
#
#
# '''Function Based View For: Create Pet, Details Pet, Edit Pet'''
