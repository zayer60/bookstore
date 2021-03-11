from django.shortcuts import render
from django.views.generic import TemplateView


class OrderProcess(TemplateView):
    template_name = 'orders/purchase.html'
