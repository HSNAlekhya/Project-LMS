from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book, Student, IssueBook
from django.contrib.auth.models import User

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'app1/login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard
@login_required
def dashboard(request):
    books = Book.objects.all()
    return render(request, 'app1/dashboard.html', {'books': books})

# Books page
@login_required
def books(request):
    books = Book.objects.all()
    return render(request, 'app1/books.html', {'books': books})
    
@login_required
def issue_book(request):
    if request.method == "POST":
        student = Student.objects.get(id=request.POST['student'])
        book = Book.objects.get(id=request.POST['book'])
        IssueBook.objects.create(student=student, book=book)
        book.quantity -= 1
        book.save()
        return redirect('dashboard')
    
    students = Student.objects.all()
    books = Book.objects.filter(quantity__gt=0)
    return render(request, 'app1/issue_book.html', {'students': students, 'books': books})