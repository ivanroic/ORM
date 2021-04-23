from django.shortcuts import render, redirect
from .models import Book, Author

def book_main(request):
    context = {
        'all_books': Book.objects.all(),
    }
    return render(request, "books_authors_app/book_main.html", context)

def add_book(request):
    Book.objects.create(title = request.POST['title'], description = request.POST['description'])
    return redirect('/book_main')

def book_view(request, id):
        context = {
        'all_books': Book.objects.all(),
        'all_authors': Author.objects.all(),
        'chosen_book': Book.objects.get(id=id)
        }
        print(id)
        return render(request, "books_authors_app/book_view.html", context)

def add_to_book(request):
        chosen_book = Book.objects.get(id=request.POST['bookid'])
        chosen_author = Author.objects.get(id=request.POST['author_id'])
        id = chosen_book.id
        chosen_book.authors.add(chosen_author)
        print(id)
        return redirect('book_view', id=id)
        # return render(request, "books_authors_app/book_view.html", context)

# def delete(request):
#     c = Book.objects.get(id=17)
#     c.delete
#     return redirect('/book_main')

def author_main(request):
    context = {
        'all_authors': Author.objects.all(),
    }
    return render(request, "books_authors_app/author_main.html", context)

def add_author(request):
    Author.objects.create(name = request.POST['first_name'] + " " + request.POST['last_name'], notes = request.POST['notes'])
    return redirect('/author_main')

def author_view(request, id):
        context = {
        'all_books': Book.objects.all(),
        'chosen_author': Author.objects.get(id=id)
        }
        print(id)
        return render(request, "books_authors_app/author_view.html", context)

def add_to_author(request, id):
        chosen_author.books.add(id=id)
        context = {
        'chosen_author': Author.objects.all(id=id),
        'chosen_book': Book.objects.get(id=id)
        }
        print(id)
        return render(request, "books_authors_app/author_view.html", context)