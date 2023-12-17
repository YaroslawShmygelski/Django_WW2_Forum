from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Persons.Status.PUBLISHED)


class Persons(models.Model):
    class Status(models.IntegerChoices):
        DRAFT =0,"Not Published"
        PUBLISHED =1,"Published"

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    objects = models.Manager()
    published = PublishedManager()

    def save(self, *args, **kwargs):
        # Генерация slug на основе title перед сохранением
        self.slug = slugify(self.title)
        super(Persons, self).save(*args, **kwargs)

    def __repr__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Генерация slug на основе title перед сохранением
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug":self.slug} )