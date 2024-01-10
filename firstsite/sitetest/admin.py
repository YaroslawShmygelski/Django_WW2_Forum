from django.contrib import admin

from sitetest.models import Persons, Category


@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'time_create','is_published']
    list_display_links = ['id', 'title']
    list_editable = ('is_published',)
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


# admin.site.register(Persons, Person)
