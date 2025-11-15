from django.shortcuts import render
from django.views.generic import TemplateView, BlogDetailView
from django.views.edit import CreateView, UpdateView
from .models import Post
from django.url import reverse_lazy


class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'app/blog_list.html'

class BlogDetailView(BlogDetailView)
    model = Post
    context_object_name = 'posts'
    template_name = 'app/blog_detail.html'

class BlogCreateView(CreateView)
    model = Post
    fields = ['title', 'author', 'body']
    template_name = 'app/blog_create.html'

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'author', 'body']
    template_name = 'app/blog_update.html'

class BlogDeleteView(UpdateView):
        model = Post
        template_name = 'app/blog_delete.html'
        success_url = reverse_lazy'home'