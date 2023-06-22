from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def validate_first_name(value):
    if not value[0].isupper():
        raise ValidationError('Your name must start with a capital letter!')


def validate_plant_name(value):
    if not value.isalpha():
        raise ValidationError('Plant name should contain only letters!')


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[
            validators.MinLengthValidator(2, message='It should consist of a minimum of 2 characters!')
        ]
    )

    first_name = models.CharField(
        max_length=20,
        validators=[validate_first_name],
    )

    last_name = models.CharField(
        max_length=20,
        validators=[validate_first_name],
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class Plant(models.Model):
    PLANT_TYPE_CHOICES = (
        ('Outdoor Plants', 'Outdoor Plants'),
        ('Indoor Plants', 'Indoor Plants'),
    )
    plant_type = models.CharField(
        max_length=14,
        choices=PLANT_TYPE_CHOICES,
    )

    name = models.CharField(
        max_length=20,
        validators=[
            validators.MinLengthValidator(2, message='It should consist of a minimum of 2 characters!'),
            validate_plant_name,
        ]
    )

    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()
