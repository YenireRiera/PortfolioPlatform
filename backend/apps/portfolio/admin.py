
from django.contrib import admin
from .models import Project, Technology


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):



    list_display = (
        "title",
        "client",
        "status",
        "featured",
        "active",
        "created_at",
    )

    list_filter = (
        "status",
        "featured",
        "active",
    )

    search_fields = (
        "title",
        "client",
        "short_description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    filter_horizontal = (
        "technologies",
    )

    ordering = (
        "-featured",
        "-created_at",
    )

    list_per_page = 20

    fieldsets = (
        ("📌 Información General", {
            "fields": (
                "title",
                "slug",
                "client",
                "status",
            )
        }),

        ("🖼 Imagen Principal", {
            "fields": (
                "main_image",
            )
        }),

        ("📝 Descripción", {
            "fields": (
                "short_description",
                "full_description",
            )
        }),

        ("📖 Caso de Estudio", {
            "fields": (
                "problem",
                "goal",
                "solution",
                "result",
                "impact",
                "lessons_learned",
            )
        }),

        ("🛠 Tecnologías", {
            "fields": (
                "technologies",
            )
        }),

        ("🔗 Enlaces", {
            "fields": (
                "repo_url",
                "demo_url",
            )
        }),


        ("⚙ Configuración", {
            "fields": (
                "featured",
                "active",
            )
        }),
    )





@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "level",
        "active",
    )

    list_filter = (
        "category",
        "level",
        "active",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "name",
    )

    list_per_page = 20

    fieldsets = (
        ("🛠 Información", {
            "fields": (
                "name",
                "category",
                "level",
            )
        }),

        ("🎨 Apariencia", {
            "fields": (
                "logo",
                "color",
            )
        }),

        ("⚙ Configuración", {
            "fields": (
                "active",
            )
        }),
    )