from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Característica"
        verbose_name_plural = "Características"

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="services"
    )

    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text="Ejemplo: fa-code, fa-globe, fa-mobile"
    )

    short_description = models.CharField(max_length=250)

    description = models.TextField()

    process = models.TextField(
        blank=True,
        help_text="Describe el proceso de trabajo para este servicio."
    )

    benefits = models.TextField(
        blank=True,
        help_text="Beneficios principales del servicio."
    )

    target_audience = models.TextField(
        blank=True,
        help_text="¿Para quién está dirigido este servicio?"
    )

    features = models.ManyToManyField(
        Feature,
        blank=True,
        related_name="services"
    )

    technologies = models.ManyToManyField(
        "portfolio.Technology",
        blank=True,
        related_name="services"
    )

    image = models.ImageField(
        upload_to="services/",
        blank=True,
        null=True
    )

    featured = models.BooleanField(default=False)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.name