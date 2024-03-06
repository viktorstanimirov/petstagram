from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size


class Photo(models.Model):
    MAX_DESCRIPTION_LENGTH = 300
    MIN_DESCRIPTION_LENGTH = 10
    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        validators=(validate_file_size,)
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(
                MIN_DESCRIPTION_LENGTH
            ),
        ),
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        blank=True,
        null=True
    )

    pets = models.ManyToManyField(
        Pet,
        blank=True
    )

    date_of_publication = models.DateField(
        auto_now=True
    )
