from django.test import TestCase

import tempfile

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import GalleryPhoto


class HomePageTests(TestCase):
    def test_homepage_shows_neighborhood_sections(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mom Sa Rew")
        self.assertContains(response, "La paix au quotidien")
        self.assertContains(response, "La fête des voisins")

    def test_neighborhood_pages_are_reachable(self):
        pages = {
            "/histoire/": "Il était une fois MOM SA REW",
            "/galerie/": "Nos souvenirs",
            "/lieux/": "Le CEM Mom Sa Rew",
        }

        for path, expected_text in pages.items():
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, expected_text)
                if path == "/galerie/":
                    self.assertNotContains(response, "Ajouter une photo")

    def test_gallery_photo_is_available_on_gallery_page(self):
        with tempfile.TemporaryDirectory() as media_root:
            with override_settings(MEDIA_ROOT=media_root):
                photo = GalleryPhoto.objects.create(
                    titre="La place du quartier",
                    image=SimpleUploadedFile("place.jpg", b"image de test"),
                    lieu="cem",
                )

                response = self.client.get("/galerie/")

                self.assertContains(response, photo.titre)
                places_response = self.client.get("/lieux/")

                self.assertContains(places_response, photo.titre)

    def test_gallery_photo_can_be_added_through_admin(self):
        admin_user = get_user_model().objects.create_superuser(
            username="gallery-admin",
            email="gallery@example.com",
            password="test-password",
        )
        self.client.force_login(admin_user)

        response = self.client.get(reverse("admin:accueil_galleryphoto_add"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "CEM Mom Sa Rew")
