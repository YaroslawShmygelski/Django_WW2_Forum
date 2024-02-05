from django.conf.urls.static import static
from django.urls import path, register_converter

from firstsite import settings
from . import views
from . import converts

register_converter(converts.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.Persons_Main.as_view(), name="home"),
    path('about/', views.about_index, name="about"),
    path('post/<slug:post_slug>/', views.show_post, name="post"),
    path('category/<slug:cat_slug>/', views.ShowCategories.as_view(), name="category"),
    path('addpost', views.addpost, name='add_post'),
    path('tags/<slug:tag_slug>/', views.ShowTags.as_view(), name="tags"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
