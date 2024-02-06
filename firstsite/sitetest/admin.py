from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from sitetest.models import Persons, Category


@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    fields = ['title','photo','post_photo', 'cat','content', 'tags', 'is_published']
    list_display = ['id', 'title', 'time_create', 'is_published', 'post_photo']
    readonly_fields = ['post_photo']
    list_display_links = ['id', 'title']
    list_editable = ('is_published',)
    list_per_page = 10
    actions = ['set_published', 'set_draft']

    @admin.display(description="Photo", ordering='content')
    def post_photo(self, person: Persons):
        if person.photo:
            return mark_safe(F"<img src='{person.photo.url}' width=70>")
        else:
            return "NO PHOTO"

    @admin.action(description="Publish all chosen")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Persons.Status.PUBLISHED)
        self.message_user(request, f"Published {count} persons.")

    @admin.action(description="Unpublish all chosen")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Persons.Status.DRAFT)
        self.message_user(request, f"{count} persons unpublished ", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

# admin.site.register(Persons, Person)
