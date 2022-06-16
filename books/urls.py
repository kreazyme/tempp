from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_all, name='book_all'),
    path('book/<slug:slug>/', views.book_detail, name='book_detail'),
    path('category/<slug:slug>/', views.book_filter_by_category, name='book_filter_by_category'),
]
