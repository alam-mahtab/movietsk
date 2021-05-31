from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    # path('',views.movieList, name='movie'),
    # path('detail/<str:pk>/', views.movieDetails, name='detail'),
    # path('create', views.createMovie, name='create'),
    # path('update/<str:pk>/', views.updateMovie, name='update'),
    # path('delete/<str:pk>/',views.deleteMovie, name='delete')
    path('movie/', views.movie_list, name='movie_list'),
    path('movie/<int:pk>', views.movie_detail, name='movie_detail'),
]

#urlpatterns = format_suffix_patterns(urlpatterns)