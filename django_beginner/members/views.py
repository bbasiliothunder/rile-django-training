from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse as http_response
from django.template import loader


def index(request):
    main = loader.get_template("main.html")
    return http_response(main.render())

# Create your views here.
