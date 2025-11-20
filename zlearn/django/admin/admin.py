from django.contrib import admin
from posts.models import Post

# adding a model to djano-admin
admin.site.register(Post)