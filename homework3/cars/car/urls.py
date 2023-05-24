from django.urls import path
from .views import *

urlpatterns = [
    path('', CarListView.as_view()),
    path('car/new', CarCreateView.as_view()),
    path('car/<int:pk>', CarUpdateView.as_view()),
    path('car/<int:pk>/delete', CarDeleteView.as_view()),
]
