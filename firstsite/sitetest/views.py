from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView

from sitetest.form import CreateForm, UploadFileForm
from sitetest.models import Persons, Category, TagPost, FileModel
from sitetest.utils import DataMixin

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add Post", 'url_name': 'add_post'},
        {'title': "Contact", 'url_name': 'contact'},
        {'title': "Login", 'url_name': 'login'}

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


class Persons_Main(DataMixin, ListView):
    template_name = "sitetest/index.html"
    context_object_name = 'posts'
    title_page = Persons

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


# def addpost(request):
#     if request.method == 'POST':
#         form = CreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = CreateForm()
#
#     data = {
#         'menu': menu,
#         'title': 'Добавление статьи',
#         'form': form
#     }
#     return render(request, "sitetest/addpost.html", context=data)


class AddPost(DataMixin, FormView):
    form_class = CreateForm
    template_name = 'sitetest/addpost.html'
    success_url = reverse_lazy('home')
    title_page = 'Add Post'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ChangeForm(DataMixin, UpdateView):
    model = Persons
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'sitetest/addpost.html'
    success_url = reverse_lazy('home')
    title_page = 'Changing Form'


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


# def show_post(request, post_slug):
#     post = get_object_or_404(Persons, slug=post_slug)
#     tag = post.tags.all()
#     data = {
#         "title": post.title,
#         "content": post.content,
#         "tags": tag,
#         "post": post,
#         "menu": menu,
#         "gay": True,
#
#     }
#
#     return render(request, "sitetest/post.html", context=data)


# View class of processing exact post data
class ShowPost(DataMixin, DetailView):
    template_name = "sitetest/post.html"
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context_data(context, title=context['post'].title)

    # Function redefined to process only published objects
    def get_object(self, queryset=None):
        return get_object_or_404(Persons, slug=self.kwargs[self.slug_url_kwarg])


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


class ShowCategories(DataMixin, ListView):
    template_name = 'sitetest/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Persons.published.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat  # cat is name of the Category of the first queryset value
        return self.get_mixin_context_data(context, title='Cat' + cat.name, cat_selected=cat.id)


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


class ShowTags(DataMixin, ListView):
    template_name = 'sitetest/index.html'
    context_object_name = 'posts'

    # Function to get queryset of Persons objects filtered by exact tag by tag_slug
    def get_queryset(self):
        tag = get_object_or_404(TagPost, slug=self.kwargs['tag_slug'])
        return tag.tags.filter(is_published=Persons.Status.PUBLISHED)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = context['posts'][0].tags.all()[0].tag  # tag is str name of a tag from first queryset value
        return self.get_mixin_context_data(context, title='Tag' + tag)
