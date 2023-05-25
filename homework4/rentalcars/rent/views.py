from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import *

class AboutView(TemplateView):
    template_name = "rent/about.html"

class CarListView(ListView):
    model = Car

class CarUpdateView(UpdateView):
    model = Car
    fields = ["name", "dealership"]
    success_url = "/"

class CarCreateView(CreateView):
    model = Car
    fields = ["name", "dealership"]
    success_url = "/"

class CarDeleteView(DeleteView):
    model = Car
    success_url = "/"
