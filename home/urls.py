from django.urls import path
from . import views

urlpatterns = [
    path("", views.movie_index, name="movie_index"),
    path("<int:pk>/", views.movie_detail, name="movie_detail"),
    path("<category>/", views.movie_category, name="movie_category")
]