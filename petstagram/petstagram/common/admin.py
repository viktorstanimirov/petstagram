from django.contrib import admin

from petstagram.common.models import Comment, Like


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_time_of_publication')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('to_photo',)