from django.contrib import admin, messages
from sitetest.models import Persons, Category


@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'time_create', 'is_published', 'brief_info']
    list_display_links = ['id', 'title']
    list_editable = ('is_published',)
    list_per_page = 10
    actions = ['set_published', 'set_draft']

    @admin.display(description="Post's Text", ordering='content')
    def brief_info(self, person: Persons):
        return f"Text {len(person.content)} symbols."

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
