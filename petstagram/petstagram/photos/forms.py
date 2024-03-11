from django import forms

from petstagram.photos.models import Photo


class PhotoCreteForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('photo',)
