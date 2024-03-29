from django.contrib import admin

from petstagram.common.models import PhotoLike, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at')


@admin.register(PhotoLike)
class PhotoLikeAdmin(admin.ModelAdmin):
    list_display = ('pet_photo',)
