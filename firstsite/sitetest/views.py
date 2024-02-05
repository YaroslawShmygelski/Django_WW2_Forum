from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView, ListView

from sitetest.form import CreateForm, UploadFileForm
from sitetest.models import Persons, Category, TagPost, FileModel

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add Post", 'url_name': 'add_post'},

        ]


# def index(request):
#     posts = Persons.published.all().select_related('cat')
#
#     data = {"title": "Mywebsite",
#
#             "number": 220,
#             "posts": posts,
#             "menu": menu,
#             }
#     return render(request, "sitetest/index.html", context=data)


class Persons_Main(ListView):
    template_name = "sitetest/index.html"
    context_object_name = 'posts'
    extra_context = {"title": "WW2 Persons",
                     "menu": menu, }

    def get_queryset(self):
        return Persons.published.all()


def about_index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = FileModel(file=form.cleaned_data['file'])
            fp.save()

    else:
        form = UploadFileForm()
    return render(request, 'sitetest/about.html', {'form': form})


def addpost(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateForm()

    data = {
        'menu': menu,
        'title': 'Добавление статьи',
        'form': form
    }
    return render(request, "sitetest/addpost.html", context=data)


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_post(request, post_slug):
    post = get_object_or_404(Persons, slug=post_slug)
    tag = post.tags.all()
    data = {
        "title": post.title,
        "content": post.content,
        "tags": tag,
        "post": post,
        "menu": menu,
        "gay": True,

    }

    return render(request, "sitetest/post.html", context=data)


# def show_categories(request, cat_slug):
#     category = get_object_or_404(Category, slug=cat_slug)
#     post = Persons.published.filter(cat_id=category.pk).select_related('cat')
#     data = {
#         "name": category.name,
#         "slug": category.slug,
#         "posts": post,
#         "menu": menu,
#         "cat_selected": category.pk,
#         "gay": True,
#
#     }
#
#     return render(request, "sitetest/index.html", context=data)


class ShowCategories(ListView):
    template_name = 'sitetest/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Persons.published.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat  # cat is name of the Category of the first queryset value
        context['title'] = cat.name + 's'
        context['menu'] = menu
        context['cat_selected'] = cat.id
        return context


# def show_tags(request, tag_slug):
#     tag = get_object_or_404(TagPost, slug=tag_slug)
#     posts = tag.tags.filter(is_published=Persons.Status.PUBLISHED)
#
#     data = {
#         "title": tag.tag,
#         "posts": posts,
#         "menu": menu,
#         "cat_selected": None
#
#     }
#     return render(request, "sitetest/index.html", context=data)


class ShowTags(ListView):
    template_name = 'sitetest/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag = get_object_or_404(TagPost, slug=self.kwargs['tag_slug'])
        return tag.tags.filter(is_published=Persons.Status.PUBLISHED)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = context['posts'][0].tags.all()[0].tag  # tag is str name of a tag from first queryset value
        context['title'] = "TAG " + tag
        context['menu'] = menu
        return context


def index2(request, id):
    return HttpResponse(f"<h1>Hello </h1><p>id: {id}</p>")


def years(request, year):
    return HttpResponse(f"<h1>Hello </h1><p>YEAR: {year}</p>")
