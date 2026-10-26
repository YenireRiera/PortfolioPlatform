
from rest_framework import generics, filters

from apps.portfolio.models import Project, Technology
from .serializers import (
    ProjectSerializer,
    TechnologySerializer,
)


class TechnologyListAPIView(generics.ListAPIView):
    queryset = Technology.objects.filter(active=True)
    serializer_class = TechnologySerializer


class ProjectListAPIView(generics.ListAPIView):
    queryset = (
        Project.objects
        .filter(active=True)
        .prefetch_related("technologies")
    )
    serializer_class = ProjectSerializer

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "title",
        "client",
        "short_description",
    ]

    ordering_fields = [
        "created_at",
        "title",
    ]

    ordering = [
        "-created_at",
    ]


class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = (
        Project.objects
        .filter(active=True)
        .prefetch_related("technologies")
    )
    serializer_class = ProjectSerializer
    lookup_field = "slug"
