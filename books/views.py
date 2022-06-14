from django.shortcuts import render, get_object_or_404
from .models import Category, Book

# Create your views here.

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_books(request):
    books = Book.objects.all()
    return render(request, 'library/home.html', {'books': books})

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'library/books/detail.html', {'book': book})
