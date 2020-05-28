from django.db import models
from django.contrib import admin


WORK = [
    ['Freelance', 'Freelance'],
    ['Architecture', 'Architecture'],
    ['Photography', 'Photography'],
    ['Design', 'Design'],
]


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(verbose_name="Dirección Web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    work = models.CharField(max_length=20, null=False, blank=False, choices=WORK, default='Architecture')
    description = models.TextField(max_length=200, verbose_name="Description", null=False, blank=False)
    link = models.URLField(verbose_name="URL", null=True, blank=True)
    start_date = models.TextField(max_length=25, verbose_name="start_date", null=False, blank=False)
    end_date = models.TextField(max_length=25, verbose_name="end_date", null=False, blank=False)

    def __str__(self):
        return self.title


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

