from django.urls import path

from applications.blog.apps import BlogConfig
from applications.blog.views import IndexView, DeletePostView
from applications.blog.views.update_post import UpdatePostView
from applications.blog.views.new_post import NewPostView

app_name = BlogConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("new/", NewPostView.as_view(), name="new-post"),
    path("<int:pk>/delete/", DeletePostView.as_view(), name="delete-post"),
    path("<int:pk>/update/", UpdatePostView.as_view(), name="update-post"),
]
