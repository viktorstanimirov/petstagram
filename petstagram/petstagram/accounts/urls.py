from django.urls import path, include

from petstagram.accounts import views

urlpatterns = (
    path("signup/", views.signup_user, name="signup-user"),
    path("signin/", views.signin_user, name="signin-user"),
    path("profile/<int:pk>/", include([
        path("", views.details_profile, name="profile-details"),
        path("edit/", views.edit_profile, name="profile-edit"),
        path("delete/", views.delete_profile, name="profile-delete")
    ])),
)
