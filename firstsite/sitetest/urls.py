from django.urls import path, register_converter
from . import views
from . import converts

register_converter(converts.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about_index, name="about"),
    path('post/<slug:post_slug>/', views.show_post, name="post"),
    path('cats/<year4:year>/', views.years)
]
