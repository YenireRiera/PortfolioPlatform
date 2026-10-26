
from rest_framework import status
from rest_framework.test import APITestCase

from apps.contact.models import ContactMessage


class ContactMessageAPITests(APITestCase):
    def setUp(self):
        self.url = "/api/contact/"
        self.valid_data = {
            "name": "María Pérez",
            "email": "maria@example.com",
            "phone": "",
            "company": "",
            "service": None,
            "subject": "Consulta de servicios",
            "message": "Quisiera recibir información.",
        }

    def test_create_contact_message(self):
        response = self.client.post(
            self.url,
            self.valid_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(
            ContactMessage.objects.first().status,
            "new",
        )

    def test_reject_empty_name(self):
        data = self.valid_data.copy()
        data["name"] = "   "

        response = self.client.post(
            self.url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_reject_empty_subject(self):
        data = self.valid_data.copy()
        data["subject"] = "   "

        response = self.client.post(
            self.url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_reject_empty_message(self):
        data = self.valid_data.copy()
        data["message"] = "   "

        response = self.client.post(
            self.url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
        self.assertEqual(ContactMessage.objects.count(), 0)
