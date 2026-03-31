from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("posts/", views.posts, name="posts"),
    path("posts/<int:id>", views.post_details, name="post_details"),
    path("create/", views.create_post, name="create_post"),
    path("posts/<int:id>/update", views.update_post, name="update_post"),
    path("posts/<int:id>/delete", views.delete_post, name="delete_post"),
    path("signup/", views.signup, name="signup"),
]
