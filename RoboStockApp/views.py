from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def landing_page(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def about_us(request):
    template = loader.get_template('about_us.html')
    context = {}
    return HttpResponse(template.render(context, request))


def help(request):
    template = loader.get_template('help.html')
    context = {}
    return HttpResponse(template.render(context, request))

def sign_up(request):
    template = loader.get_template('sign_up.html')
    context = {}
    return HttpResponse(template.render(context, request))

def sign_in(request):
    template = loader.get_template('sign_in.html')
    context = {}
    return HttpResponse(template.render(context, request))