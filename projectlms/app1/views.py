from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book, Student, IssuedBook
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
 # ADD STUDENT
    if request.method == "POST" and "add_student" in request.POST:
        Student.objects.create(
            full_name=request.POST.get("full_name"),
            student_id=request.POST.get("student_id"),
            grade=request.POST.get("grade"),
        )
        return redirect("issue_books")

    # ADD BOOK
    if request.method == "POST" and "add_book" in request.POST:
        Book.objects.create(
            title=request.POST.get("title"),
            author=request.POST.get("author"),
            quantity=request.POST.get("quantity"),
        )
        return redirect("issue_books")

    # ISSUE BOOK
    if request.method == "POST" and "issue_book" in request.POST:
        student = Student.objects.get(id=request.POST.get("student"))
        book = Book.objects.get(id=request.POST.get("book"))

        IssuedBook.objects.create(student=student, book=book)

        book.quantity -= 1
        book.save()

        return redirect("issue_books")

    context = {
        "students": Student.objects.all(),
        "books": Book.objects.filter(quantity__gt=0),
        "issued_books": IssuedBook.objects.all()
    }

    return render(request, "app1/issuebooks.html", context)
