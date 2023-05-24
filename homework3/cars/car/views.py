from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import *

class CarListView(ListView):
    model = Car

class CarCreateView(CreateView):
    model = Car
    fields = ["name", "price"]
    success_url = "/"

class CarUpdateView(UpdateView):
    model = Car
    fields = ["name", "price"]
    success_url = "/"

class CarDeleteView(DeleteView):
    model = Car
    success_url = "/"
