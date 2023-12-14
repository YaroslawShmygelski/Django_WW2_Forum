from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Persons(models.Model):
    title = models.CharField(max_length=255)
    slug=models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Генерация slug на основе title перед сохранением
        self.slug = slugify(self.title)
        super(Persons, self).save(*args, **kwargs)

    def __repr__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug":slugify(self.title)})