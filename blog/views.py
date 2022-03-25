from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView #new
from django.urls import reverse_lazy #new
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title','author','body']  #database field we want to expose

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView): #new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')   #opposed to reverse so that it won't execute the URL redirect until our view has finished deleting the blog post
                                         #simply reverse_lazy('home') redirect us after deleting to the home page, the page which is given as an argument

# Create your views here.
