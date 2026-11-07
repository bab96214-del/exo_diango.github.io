from django.contrib import admin
from .models import GalleryPhoto


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ("titre", "lieu", "date_ajout")
    list_filter = ("lieu",)
    search_fields = ("titre", "description")
    readonly_fields = ("date_ajout",)
