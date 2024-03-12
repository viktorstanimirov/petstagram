from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.common.models import PhotoLike, Comment
from petstagram.photos.models import Photo


def index(request):
    pet_photos = Photo.objects.all()
    comment_form = CommentForm()
    context = {
        'pet_photos': pet_photos,
        'comment_form': comment_form,
    }
    return render(request, "common/index.html", context)


def like_pet_photo(request, pk):
    pet_photo_like = PhotoLike.objects.filter(pet_photo_id=pk).first()

    if pet_photo_like:
        pet_photo_like.delete()
    else:
        PhotoLike.objects.create(pet_photo_id=pk)

    return redirect(request.META.get('HTTP_REFERER') + f"#photo-{pk}")


def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(pk=photo_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment_text = request.POST.get("text")
            comment = Comment(pet_photo=photo, text=comment_text)
            comment.save()

    return redirect(request.META.get('HTTP_REFERER') + f"#photo-{photo_id}")
