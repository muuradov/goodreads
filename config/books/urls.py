from django.urls import path
from .views import books_list, BookDetailView

urlpatterns = [
    path('books/', books_list, name='books_list'),
    path('<int:book_id>/', BookDetailView.as_view(), name='books_detail'),
]
