
from django.urls import path

from .views import (
    TechnologyListAPIView,
    ProjectListAPIView,
    ProjectDetailAPIView,
)

urlpatterns = [
    path(
        "technologies/",
        TechnologyListAPIView.as_view(),
        name="technology-list",
    ),
    path(
        "projects/",
        ProjectListAPIView.as_view(),
        name="project-list",
    ),
    path(
        "projects/<slug:slug>/",
        ProjectDetailAPIView.as_view(),
        name="project-detail",
    ),
]
