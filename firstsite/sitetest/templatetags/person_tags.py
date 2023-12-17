from django import template
import sitetest.views as views
from sitetest.models import Category

register = template.Library()



@register.inclusion_tag('sitetest/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}
