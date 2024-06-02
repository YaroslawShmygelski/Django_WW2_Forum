from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView, CreateView
from sitetest.form import CreateForm, UploadFileForm
from sitetest.models import Persons, Category, TagPost
from sitetest.utils import DataMixin


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
    title_page = 'WW2 Persons'

    def get_queryset(self):
        return Persons.published.all().order_by('pk')

@login_required
def about_index(request):
    posts_query=Persons.published.all()
    paginator=Paginator(posts_query,3)

    page_num=request.GET.get('page')
    page_obj=paginator.get_page(page_num)
    return render(request, 'sitetest/about.html', {'page_object': page_obj})


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


class AddPost(LoginRequiredMixin,DataMixin, CreateView):
    form_class = CreateForm
    template_name = 'sitetest/addpost.html'
    # success_url = reverse_lazy('home')
    title_page = 'Add Post'

    def form_valid(self, form):
        obj_form=form.save(commit=False)
        obj_form.author=self.request.user
        return super().form_valid(form)


class ChangePost(DataMixin, UpdateView):
    model = Persons
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'sitetest/addpost.html'
    success_url = reverse_lazy('home')
    title_page = 'Changing Form'


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
class ShowPost(LoginRequiredMixin,DataMixin, DetailView):
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
        return Persons.published.filter(cat__slug=self.kwargs['cat_slug']).order_by('pk')

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
