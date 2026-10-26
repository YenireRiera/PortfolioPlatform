from django.contrib import admin
from .models import Category, Feature, Service


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "active")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "featured",
        "active",
        "created_at",
    )

    list_filter = (
        "category",
        "featured",
        "active",
    )

    search_fields = (
        "name",
        "short_description",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    filter_horizontal = (
        "features",
        "technologies",
    )

    ordering = (
        "name",
    )

    list_per_page = 20

    fieldsets = (

        ("📌 Información General", {
            "fields": (
                "name",
                "slug",
                "icon",
                "category",
            )
        }),

        ("📝 Descripción", {
            "fields": (
                "short_description",
                "description",
            )
        }),

        ("🎯 Público Objetivo", {
            "fields": (
                "target_audience",
            )
        }),

        ("⭐ Beneficios", {
            "fields": (
                "benefits",
            )
        }),

        ("⚙️ Proceso de Trabajo", {
            "fields": (
                "process",
            )
        }),

        ("🛠 Tecnologías y Características", {
            "fields": (
                "technologies",
                "features",
            )
        }),

        ("🖼 Imagen", {
            "fields": (
                "image",
            )
        }),

        ("⚙ Configuración", {
            "fields": (
                "featured",
                "active",
            )
        }),

    )