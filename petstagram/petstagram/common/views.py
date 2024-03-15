from django.shortcuts import redirect
from django.views import generic as views

from petstagram.common.forms import CommentForm
from petstagram.common.models import PhotoLike, Comment
from petstagram.photos.models import Photo


class IndexView(views.ListView):
    context_object_name = "pet_photos"

    queryset = Photo.objects.all() \
        .prefetch_related("pets") \
        .prefetch_related("photolike_set")

    template_name = "common/index.html"

    paginate_by = 1

    @property
    def pet_name_pattern(self):
        return self.request.GET.get("pet_name_pattern", None)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["pet_name_pattern"] = self.pet_name_pattern or ""
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.filter_by_pet_name_pattern(queryset)

        return queryset

    def filter_by_pet_name_pattern(self, queryset):
        pet_name_pattern = self.pet_name_pattern

        filter_query = {}

        if pet_name_pattern:
            filter_query['pets__name__icontains'] = pet_name_pattern

        return queryset.filter(**filter_query)


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


"""Rewrite the 'index' FBV to a CBV"""

# def index(request):
#     pet_photos = Photo.objects.all()
#     comment_form = CommentForm()
#     search_form = SearchForm()
#     context = {
#         'pet_photos': pet_photos,
#         'comment_form': comment_form,
#         'search_form': search_form,
#     }
#     return render(request, "common/index.html", context)
