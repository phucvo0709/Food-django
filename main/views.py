from curses.ascii import HT
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse


def test(req):
    return HttpResponse('test')


def index(req):
    return render(req, 'index.html')
