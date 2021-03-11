from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView,DetailView
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class BookList(LoginRequiredMixin,ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'

class BookDetails(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'

class SearchBookList(LoginRequiredMixin,ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_book.html'
    login_url = 'account_login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(Q(title__icontains=query)|Q(author__icontains=query))

