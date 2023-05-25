from django.urls import path
from .views import *


urlpatterns = [
    path('about', AboutView.as_view()),
    path('', CarListView.as_view()),
    path('rent/<int:pk>', CarUpdateView.as_view()),
    path('rent/new', CarCreateView.as_view()),
    path('rent/<int:pk>/delete', CarDeleteView.as_view()),
]
