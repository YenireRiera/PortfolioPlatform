from django.db import models
from django.utils.text import slugify


class Technology(models.Model):
    CATEGORY_CHOICES = [
        ("language", "Lenguaje"),
        ("framework", "Framework"),
        ("database", "Base de datos"),
        ("tool", "Herramienta"),
    ]

    LEVEL_CHOICES = [
        ("learning", "Aprendiendo"),
        ("comfortable", "Cómodo"),
        ("proficient", "Dominado"),
    ]

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

    logo = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=20, blank=True)

    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ("in_progress", "En progreso"),
        ("completed", "Completado"),
    ]

    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    client = models.CharField(max_length=150, blank=True)

    main_image = models.ImageField(upload_to="portfolio/", blank=True, null=True)

    short_description = models.CharField(max_length=250)
    full_description = models.TextField()

    # Caso de estudio
    problem = models.TextField(help_text="¿Qué problema tenía el cliente/usuario?")
    goal = models.TextField(help_text="¿Qué se buscaba lograr?")
    solution = models.TextField(help_text="¿Cómo se resolvió?")
    result = models.TextField(help_text="¿Qué se logró?")
    impact = models.TextField(blank=True, help_text="Impacto medible, si aplica")
    lessons_learned = models.TextField(blank=True)

    technologies = models.ManyToManyField(Technology, related_name="projects", blank=True)

    repo_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="completed")
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-featured", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title