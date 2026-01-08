from django.urls import path
from .views import issue_books
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('books/', views.books, name='books'),
    path('issue-books/', views.issue_books, name='issue_books'),
    path('logout/', views.logout_view, name='logout'),
]
