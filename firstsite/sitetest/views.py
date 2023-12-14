from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string

from sitetest.models import Persons

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
    Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
     'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

data = {"title": "Mywebsite",
        "menu": menu,
        "number": 220,
        "posts":data_db
        }

def index(request):
    posts=Persons.objects.filter(is_published=True)

    data = {"title": "Mywebsite",
            "menu": menu,
            "number": 220,
            "posts": posts
            }
    return render(request,"sitetest/index.html", context=data)

def about_index(request):
    return render(request,"sitetest/about.html", context=data)


def show_post(request, post_slug):
    post=get_object_or_404(Persons, slug=post_slug)
    def make_slug_links():
        for p in post:
            p.slug=slugify(p.title)
    data={
        "title":post.title,
        "content":post.content,
        "menu": menu,
        "gay":True,
        "slugi":slugify(post.title)
    }

    return render(request, "sitetest/post.html", context=data)

def index2(request,id):
    return HttpResponse(f"<h1>Hello </h1><p>id: {id}</p>")

def years(request,year):
    return HttpResponse(f"<h1>Hello </h1><p>YEAR: {year}</p>")