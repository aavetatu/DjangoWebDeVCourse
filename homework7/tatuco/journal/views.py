from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

class AboutView(TemplateView):
    template_name = "journal/about.html"

class LogListView(LoginRequiredMixin, ListView):
    model = Log
    template_name = "journal/log_list.html"

class LogUpdateView(LoginRequiredMixin, UpdateView):
    model = Log
    fields = ["name", "status", "created", "description"]
    success_url = "/"

class LogCreateView(LoginRequiredMixin, CreateView):
    model = Log
    fields = ["name", "status", "created", "description"]
    success_url = "/"

class LogDeleteView(LoginRequiredMixin, DeleteView):
    model = Log
    success_url = "/"


class TaskListView(LoginRequiredMixin, ListView):
    model = Log
    template_name = "journal/todo.html"
