from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('book/<slug:slug>/', views.book_detail, name='book_detail'),
    path('category/<slug:slug>/', views.category_list, name='category_list'),
]
