from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Post

# Create your views here.
class PostIndexView(ListView):
    template_name = 'posts/index.html'
    model = Post
    context_object_name = 'posts'

class PostCreateView(CreateView):
    template_name = 'posts/create.html'
    model = Post
    fields = ['title', 'content', 'active', 'status']
    context_object_name = 'post'
    success_url = reverse_lazy('posts:index')

class PostUpdateView(UpdateView):
    template_name = 'posts/update.html'
    model = Post
    fields = ['title', 'content', 'active', 'status']
    context_object_name = 'post'
    success_url = reverse_lazy('posts:index')

class PostDeleteView(DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('posts:index')
