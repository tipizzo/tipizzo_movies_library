from django.shortcuts import render
from home.models import Movie

def movie_index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, "movie_index.html", context)

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }
    return render(request, "movie_detail.html", context)

def movie_category(request, category):
    movies = Movie.objects.filter(categories__name__contains=category
    ).order_by('-created_on')
    context = {
        'category': category,
        'movies': movies
    }
    return render(request, 'movie_category.html', context)
