from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail

class Home(TemplateView):
    # send_mail("Testing","this is a empty mail by","sender@gmail.com",
    #           ["receiver@gmail.com"],
    #           fail_silently=False)
    template_name = 'home.html'
