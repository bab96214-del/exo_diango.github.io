from django.db import models

# Create your models here.
from django.core.validators import FileExtensionValidator
from django.db import models
from django.core.exceptions import ValidationError


def validate_image_size(image):
    if image.size > 8 * 1024 * 1024:
        raise ValidationError("La taille de l'image ne doit pas dépasser 8 Mo.")


class GalleryPhoto(models.Model):
    LIEUX = [
        ("quartier", "Mom Sa Rew"),
        ("cem", "CEM Mom Sa Rew"),
        ("terrain", "Terrain Mom Sa Rew"),
    ]

    titre = models.CharField(max_length=100)
    description = models.CharField(max_length=240, blank=True)
    lieu = models.CharField(max_length=12, choices=LIEUX, default="quartier")
    image = models.FileField(
        upload_to="galerie/",
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"]),
            validate_image_size,
        ],
    )
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_ajout"]
        verbose_name = "photo de la galerie"
        verbose_name_plural = "photos de la galerie"

    def __str__(self):
        return self.titre
