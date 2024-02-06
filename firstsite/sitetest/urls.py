from django.conf.urls.static import static
from django.urls import path, register_converter

from firstsite import settings
from . import views
from . import converts

register_converter(converts.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.Persons_Main.as_view(), name="home"),
    path('about/', views.about_index, name="about"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name="post"),
    path('category/<slug:cat_slug>/', views.ShowCategories.as_view(), name="category"),
    path('addpost', views.AddPost.as_view(), name='add_post'),
    path('edit/<int:pk>/', views.ChangeForm.as_view(), name='edit_post'),
    path('tags/<slug:tag_slug>/', views.ShowTags.as_view(), name="tags"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
