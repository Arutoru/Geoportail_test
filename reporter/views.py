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
        return Aot.objects.order_by('amodiataire')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Récupération des données avec date d'expiration encore loin
        query1 = Aot.objects.filter(date_fin__gt=timezone.now()+timedelta(days=120)).order_by('date_fin')
        # Récupération des données avec date d'expiration presque atteinte
        query2 = Aot.objects.filter(date_fin__lte=timezone.now()+timedelta(days=120)).filter(date_fin__gt=timezone.now()).order_by('date_fin')
        # Récupération des données avec date d'expiration dépassée
        query3 = Aot.objects.filter(date_fin__lte=timezone.now()).order_by('date_fin')

        context["green"] = query1
        context["orange"] = query2
        context["red"] = query3

        # Récupération des montants cautions inférieur à 2000000
        query4 = Aot.objects.filter(montant_caution__lt=2000000).values('montant_caution').annotate(Count('montant_caution')).order_by()
        # Récupération des montants cautions supérieur à 2000000 et inférieur à 3000000
        query5 = Aot.objects.filter(montant_caution__gte=2000000).filter(montant_caution__lt=3000000).values('montant_caution').annotate(Count('montant_caution')).order_by()
        # Récupération des montants cautions supérieur à 3000000
        query6 = Aot.objects.filter(montant_caution__gte=3000000).values('montant_caution').annotate(Count('montant_caution')).order_by()

        context["low_caut"] = query4
        context["mid_caut"] = query5
        context["high_caut"] = query6

        # Récupération des remarques positives
        query7 = Aot.objects.filter(statut="green")
        # Récupération des remarques positives
        query8 = Aot.objects.filter(statut="orange")
        # Récupération des remarques positives
        query9 = Aot.objects.filter(statut="red")

        context["bon"] = query7
        context["intermediaire"] = query8
        context["critique"] = query9
        return context
