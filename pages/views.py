# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'
class AboutPageView(TemplateView):
    template_name = 'about.html'
class PaymentPageView(TemplateView):
    template_name = 'payment.html'
