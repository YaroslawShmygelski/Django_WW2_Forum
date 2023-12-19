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
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')
    country=models.OneToOneField('Country', blank=True, on_delete=models.SET_NULL, null=True, related_name='countri')

    objects = models.Manager()
    published = PublishedManager()

    # Automatic Generation of a slug based on titile
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Persons, self).save(*args, **kwargs)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    # Automatic Generation of slug based on name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug":self.slug} )


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse("tags", kwargs={"tag_slug":self.slug} )


class Country(models.Model):
    name=models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, null=True, db_index=True)

    def __str__(self):
        return self.name

    # Automatic Generation of slug based on na