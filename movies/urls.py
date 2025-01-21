from django.urls import path
from . import views
from .views import movie_list_api  
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.movie_list, name='movie-list-page'),
    path('create/', views.movie_create, name='movie-create-page'),
    path('<int:pk>/', views.movie_detail, name='movie-detail-page'),
    path('<int:pk>/update/', views.movie_update, name='movie_update'),
    path('<int:pk>/delete/', views.movie_delete, name='movie_delete'),
    path('api/movies/', movie_list_api, name='movie-list-api'),  # Utiliser la vue API
    path('login/', auth_views.LoginView.as_view(template_name='movies/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='movies/logout.html'), name='logout'),
    path('signup/', views.signup, name='signup'),
]
