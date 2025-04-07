from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.utils.autoreload import restart_with_reloader

from .forms import RegisterForm
from .forms import LoginForm
from .models import Author, Review


# Create your views here.
def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
         form = RegisterForm()
    return render(request, 'index.html', { 'form': form})

def Login(request):
    if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
    else:
          form = LoginForm()
    return render(request,'login.html',{'form':form})

def Home(request):
    authors = Author.objects.all()

    return render(request, 'home.html',{'authors': authors})
def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)  # Get the specific author or return 404
    books = Book.objects.filter(author=author)  # Get books by the author
    return render(request, 'author_detail.html', {'author': author, 'books': books})

from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm
from .models import Author, Book


def index(request, author_id, book_id):
    # Get the specific author or return 404
    author = get_object_or_404(Author, id=author_id)

    # Get the specific book or return 404
    book = get_object_or_404(Book, author=author, id=book_id)
    reviews=Review.objects.filter(book=book)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Save the review and associate it with the book
            review = form.save(commit=False)
            review.book = book  # Associate the review with the book
            review.save()  # Save the review
            return redirect('author_detail', author_id=author_id)  # Redirect back to the author's book list
    else:
        form = ReviewForm()
    if reviews.exists():
        totals=sum(data.review for data in reviews) / len(reviews)
        total=int(totals)
    else:
        totals=0
        total = int(totals)

    return render(request, 'last.html', {'form': form, 'book': book, 'author': author,'review':reviews,'total':total})
