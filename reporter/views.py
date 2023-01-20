from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from .models import Aot
# from .forms import PostForm, CommentForm

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class AotListView(ListView):
    model = Aot
    template_name = "aot_list.html"

    def get_queryset(self):
        return Aot.objects.order_by('amodiatair')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Récupération des données avec date d'expiration encore loin
        query1 = Aot.objects.filter(date_caut__gt=timezone.now()+timedelta(days=120)).order_by('date_caut')
        # Récupération des données avec date d'expiration presque atteinte
        query2 = Aot.objects.filter(date_caut__lte=timezone.now()+timedelta(days=120)).filter(date_caut__gt=timezone.now()).order_by('date_caut')
        # Récupération des données avec date d'expiration dépassée
        query3 = Aot.objects.filter(date_caut__lte=timezone.now()).order_by('date_caut')

        context["green"] = query1
        context["orange"] = query2
        context["red"] = query3
        return context
