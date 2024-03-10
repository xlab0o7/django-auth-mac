
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("logout", views.signout, name="logout"),
    path("login/", views.login1, name="login1"),
    path("chat/", views.ChatBox, name="chatbox"), # type: ignore

]

