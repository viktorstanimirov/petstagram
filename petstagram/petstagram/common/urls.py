from django.urls import path

from petstagram.common.views import like_pet_photo, add_comment, IndexView

urlpatterns = (
    path("", IndexView.as_view(), name="index"),
    path("pet_photo_like/<int:pk>/", like_pet_photo, name="like_pet_photo"),
    path("pet_photo_comment/<int:photo_id>", add_comment, name="add_comment"),
)
