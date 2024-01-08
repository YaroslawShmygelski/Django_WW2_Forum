from django import template
from django.db.models import Count

import sitetest.views as views
from sitetest.models import Category, TagPost

register = template.Library()


@register.inclusion_tag('sitetest/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(total=Count("categ")).filter(total__gt=0)
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('sitetest/list_tags.html')
def show_tags():
    tags = TagPost.objects.annotate(total=Count("tags")).filter(total__gt=0)
    return {'tags': tags}

