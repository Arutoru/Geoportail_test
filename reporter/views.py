from django.shortcuts import render
from django.views.generic import TemplateView, DetailView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'
