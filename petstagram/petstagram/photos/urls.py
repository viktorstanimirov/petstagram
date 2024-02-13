from django.urls import path, include

from petstagram.photos import views

urlpatterns = (
    path('add/', views.add_photo, name='add-photo'),
    path('<int:pk>/', include([
        path('', views.photo_details_page, name='photo-details'),
        path('edit/', views.photo_edit_page, name='edit-photo')
    ])),
)