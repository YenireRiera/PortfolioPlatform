from django.urls import path

from .views import (
    CategoryListAPIView, FeatureListAPIView, ServiceListAPIView,)


urlpatterns = [
    path(
        "categories/",
        CategoryListAPIView.as_view(),
        name="category-list",
    ),

    path(
        "features/",
        FeatureListAPIView.as_view(),
        name="feature-list",
    ),

    path(
        "",
        ServiceListAPIView.as_view(),
        name="service-list",
    ),
]