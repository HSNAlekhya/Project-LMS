from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('books/', views.books, name='books'),
    path('issue/', views.issue_book, name='issue_book'),
    path('logout/', views.logout_view, name='logout'),
]
