# from django.shortcuts import render
from django.contrib.auth.views import LoginView
from main_app.models import Post
from main_app.forms import PostForm
from django.views.generic import CreateView
# from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
    template_name = 'home.html'

# class PostCreate(LoginRequiredMixin, CreateView):
class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    # success_url = '/'