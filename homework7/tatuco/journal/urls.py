from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *


urlpatterns = [
    path('about', AboutView.as_view()),
    path('', TaskListView.as_view()),
    path('journal', LogListView.as_view()),
    path('journal/<int:pk>', LogUpdateView.as_view()),
    path('journal/new', LogCreateView.as_view()),
    path('journal/<int:pk>/delete', LogDeleteView.as_view()),
    
    path('login', LoginView.as_view(next_page="/")),
    path('accounts/login/', LoginView.as_view(next_page="/")),
    path('logout', LogoutView.as_view(next_page="/")),
]
