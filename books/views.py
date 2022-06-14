from django.shortcuts import render
from .models import Category, Book

# Create your views here.

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_books(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})
