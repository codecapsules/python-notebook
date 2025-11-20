from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

from posts.forms import PostCreateForm
from posts.models import Post
from posts.views import index

###### on the core project #####
urlpatterns = [
    path("admin/", admin.site.urls),
    path("posts/", include("posts.urls", namespace="posts")),
]

###### on the generated apps urls.py #####
app_name = "posts"

urlpatterns = [
    path("", index, name="index"),
]
###################################

###### A Create Post functions in FBV ##########
def create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            post = Post(title=form_data['title'], status=form_data['status'])
            post.save()
    else:
        form = PostCreateForm()

    return render(request, 'posts/create.html', {'form': form})
#################################################