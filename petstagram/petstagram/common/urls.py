
from django.urls import path

from petstagram.common.views import index

# from petstagram.common.views import IndexView

urlpatterns = (
    path("", index, name="index"),
    # path("", IndexView.as_view(), name="index"),
    # path("pet_photo_like/<int:pk>/", like_pet_photo, name="like_pet_photo"),

)