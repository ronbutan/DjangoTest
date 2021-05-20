from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="movie-index"),
    path("create/",views.create, name="movie-create"),
    path("update/<str:pk>/",views.update, name="movie-update")
]