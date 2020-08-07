from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.books, name='books'),
    path('', views.authors, name='author'),
]
