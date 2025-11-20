from django.urls import path

from posts.views import PostCreateView, PostIndexView, PostUpdateView, PostDeleteView

app_name = "posts"

urlpatterns = [
    path("", PostIndexView.as_view(), name="index"),
    path("create/", PostCreateView.as_view(), name="create"),
    path("<int:pk>/update", PostUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", PostDeleteView.as_view(), name="delete"),
]
