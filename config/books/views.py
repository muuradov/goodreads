
from django.shortcuts import render
from django.views.generic import DetailView

from .models import Book


def books_list(request):
    books = Book.objects.all()
    return render(request, 'books_list.html', {'books': books})

class BookDetailView(DetailView):
    model = Book
    template_name = 'books_detail.html'
    context_object_name = 'book'
    pk_url_kwarg = 'book_id'