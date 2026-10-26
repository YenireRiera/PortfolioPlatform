
from rest_framework import status
from rest_framework.test import APITestCase

from apps.portfolio.models import Project, Technology


class PortfolioAPITests(APITestCase):
    def setUp(self):
        self.technology = Technology.objects.create(
            name="Python",
            active=True,
        )

        self.project = Project.objects.create(
            title="Proyecto de prueba",
            short_description="Descripción del proyecto",
            active=True,
        )

        self.project.technologies.add(self.technology)

    def test_list_projects(self):
        response = self.client.get("/api/projects/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_project_detail_by_slug(self):
        response = self.client.get(
            f"/api/projects/{self.project.slug}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            response.data["title"],
            self.project.title,
        )

    def test_inactive_project_is_not_visible(self):
        self.project.active = False
        self.project.save()

        response = self.client.get(
            f"/api/projects/{self.project.slug}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_list_technologies(self):
        response = self.client.get("/api/technologies/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
