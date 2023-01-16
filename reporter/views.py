from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from .models import Borne, Region
# from .forms import PostForm, CommentForm

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class RegionListView(ListView):
    model = Region
    template_name = "region_list.html"

    def get_queryset(self):
        return Region.objects.order_by('nom')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Récupération des données avec date d'expiration encore loin
        query1 = Region.objects.filter(date__gt=timezone.now()+timedelta(days=120)).order_by('date')
        # Récupération des données avec date d'expiration presque atteinte
        query2 = Region.objects.filter(date__lte=timezone.now()+timedelta(days=120)).filter(date__gt=timezone.now()).order_by('date')
        # Récupération des données avec date d'expiration dépassée
        query3 = Region.objects.filter(date__lte=timezone.now()).order_by('date')

        context["green"] = query1
        context["orange"] = query2
        context["red"] = query3
        return context
