from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Persons.Status.PUBLISHED)


class Persons(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, "Not Published"
        PUBLISHED = 1, "Published"

    title = models.CharField(max_length=255, verbose_name="Name")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")
    photo = models.FileField(upload_to='photos/%Y/%m/%d/',
                             blank=True, null=True, verbose_name="Photo")
    content = models.TextField(blank=True, verbose_name="content")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time of creation")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Last update")
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Published Status")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='categ', verbose_name="Category")
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags', verbose_name="Tags")
    country = models.OneToOneField('Country', blank=True, on_delete=models.SET_NULL, null=True, related_name='countri',
                                   verbose_name="Country")
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='posts', null=True,
                               default=True)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name_plural = "Person"

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
    name = models.CharField(max_length=100, db_index=True, verbose_name="Category")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Catefories"

    def __str__(self):
        return self.name

    # Automatic Generation of slug based on name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse("tags", kwargs={"tag_slug": self.slug})


class Country(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, null=True, db_index=True)

    def __str__(self):
        return self.name

    # Automatic Generation of slug based on na



