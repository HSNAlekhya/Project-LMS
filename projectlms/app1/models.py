from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10)
    grade = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}"


class IssuedBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} is issued to {self.student.full_name}"

# Create your models here.

