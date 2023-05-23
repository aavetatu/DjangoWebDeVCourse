from django.views.generic import TemplateView, ListView
from .models import *

#class AboutView(TemplateView):
#   template_name = 'bookstore/books.html'

class BookListView(ListView):
    model = Book
