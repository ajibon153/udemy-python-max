from django.shortcuts import render
from .models import Book
from django.db.models import Avg

# Create your views here.


def index(request):
    books = Book.objects.all().order_by('-rating')
    return render(request, 'book_outlet/index.html', {
        'books': books,
        "total_books": books.count(),
        "average_rating": books.aggregate(Avg('rating'))['rating__avg']
    })


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'book_outlet/detail.html', {'book': book})
