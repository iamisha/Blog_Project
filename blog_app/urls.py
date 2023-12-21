
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("post/<int:pk>",views.post_detail,name="details"),
    path("signup/",views.signup_view,name="signup"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("add_post/",views.add_post,name="add_post"),
    path("update_post/<int:id>",views.update_post,name="update_post"),
    path("delete_post/<int:id>",views.delete_post,name="delete_post"),
]
