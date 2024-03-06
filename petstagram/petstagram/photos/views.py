from django.shortcuts import render


def create_photo(request):
    context = {}
    return render(request, "photos/photo-add-page.html", context)


def photo_details(request, pk):
    context = {}
    return render(request, "photos/photo-details-page.html", context)


def photo_edit_page(request, pk):
    context = {}
    return render(request, "photos/photo-edit-page.html", context)
