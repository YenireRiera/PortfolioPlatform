from rest_framework import generics, filters

from apps.services.models import Category, Feature, Service

from .serializers import (
    CategorySerializer,
    FeatureSerializer,
    ServiceSerializer,
)


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(active=True)
    serializer_class = CategorySerializer


class FeatureListAPIView(generics.ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class ServiceListAPIView(generics.ListAPIView):
    queryset = (
        Service.objects
        .filter(active=True)
        .select_related("category")
        .prefetch_related("features", "technologies")
    )

    serializer_class = ServiceSerializer

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "name",
        "short_description",
        "description",
    ]

    ordering_fields = [
        "name",
        "created_at",
    ]

    ordering = [
        "name",
    ]