# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render
from django.http import Http404
from library.models import Book
from library.models import Author


def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context)


def book(request, book_id):
    if not(book_id.isdigit()) or book_id <= 0:
        raise Http404
    try:
        book = Book.objects.get(id=book_id)
    except Exception, e:
        raise Http404
    else:
        context = {'book': book}
        return render(request, 'book.html', context)


def authors(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'authors.html', context)


def author(request, author_id):
    if not(author_id.isdigit()) or author_id <= 0:
        raise Http404
    try:
        author = Author.objects.get(id=author_id)
    except Exception, e:
        raise Http404
    else:
        context = {'author': author}
        return render(request, 'author.html', context)
