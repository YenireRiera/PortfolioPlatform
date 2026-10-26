
from rest_framework import status
from rest_framework.test import APITestCase

from apps.services.models import Category, Service


class ServicesAPITests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Desarrollo web",
            active=True,
        )

        self.service = Service.objects.create(
            category=self.category,
            name="Desarrollo de aplicaciones",
            short_description="Creación de aplicaciones web",
            active=True,
        )

    def test_list_services(self):
        response = self.client.get("/api/services/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_list_categories(self):
        response = self.client.get("/api/services/categories/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_service_is_in_list(self):
        response = self.client.get("/api/services/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        results = response.data.get(
            "results",
            response.data,
        )

        self.assertTrue(
            any(item["name"] == self.service.name for item in results)
        )

    def test_inactive_service_is_not_visible(self):
        self.service.active = False
        self.service.save()

        response = self.client.get("/api/services/")

        results = response.data.get(
            "results",
            response.data,
        )

        self.assertFalse(
            any(item["name"] == self.service.name for item in results)
        )
