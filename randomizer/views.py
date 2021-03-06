import random
from django.shortcuts import render
from django.views.generic.base import TemplateView
from randomizer.models import Restaurant


class HomeView(TemplateView):
    """home page"""
    template_name = 'home.html'

    def get_context_data(self):
        context = super().get_context_data()
        count = Restaurant.objects.count()
        if count > 0:
            index   = random.randint(0, count - 1)
            context['restaurant'] = Restaurant.objects.all()[index]
        return context
