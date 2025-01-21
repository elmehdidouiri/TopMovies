from django.shortcuts import render, get_object_or_404, redirect

from .models import Movie
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from .forms import MovieForm  # Nous allons créer ce formulaire après
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
# Liste des films
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

@login_required
# Détails d’un film
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

@login_required
# Ajouter un film
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie-list-page')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form})

@login_required
# Modifier un film
def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie-detail-page', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_update.html', {'form': form, 'movie': movie})

@login_required
# Supprimer un film
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie-list-page')
    return render(request, 'movies/movie_delete.html', {'movie': movie})

@login_required
#filtrage films par catégorie
def movie_list(request):
    query = request.GET.get('q')
    rating = request.GET.get('rating')
    movies = Movie.objects.all().order_by('-rating')  # Trier par note décroissante

    if query:
        movies = movies.filter(title__icontains=query)

    if rating:
        movies = movies.filter(rating__gte=rating)

    return render(request, 'movies/movie_list.html', {'movies': movies})


@login_required
#Ajout d API
def movie_list_api(request):
    movies = Movie.objects.all()
    movies_data = [
        {
            'id': movie.id,
            'title': movie.title,
            'description': movie.description,
            'director': movie.director,
            'duration': movie.duration,
            'release_date': movie.release_date,
            'rating': movie.rating,
            'actors': movie.actors.split(','),
        }
        for movie in movies
    ]
    return JsonResponse({'movies': movies_data})

#formulaire d'inscription
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'movies/signup.html', {'form': form})