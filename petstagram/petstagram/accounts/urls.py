from django.urls import path, include

from petstagram.accounts import views

urlpatterns = (
    path("signup/", views.signup_user, name="signup_user"),
    path("signin/", views.signin_user, name="signin_user"),

    path("profile/<int:pk>/", include([
        path("", views.details_profile, name="profile_details"),
        path("edit/", views.edit_profile, name="profile_edit"),
        path("delete/", views.delete_profile, name="profile_delete")
    ])),
)
