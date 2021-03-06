from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
    path('adduser/', views.adduser, name="blog-adduser"),
    path('viewprofile/<str:pk>/', views.viewprofile, name="blog-viewprofile"),
]