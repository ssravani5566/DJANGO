from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def  home(request):
    temp=loader.get_template('home.html')
    return HttpResponse(temp.render())
def  page_101(request):
    temp=loader.get_template('101.html')
    return HttpResponse(temp.render())
def  page_102(request):
    temp=loader.get_template('102.html')
    return HttpResponse(temp.render())
def  page_103(request):
    temp=loader.get_template('103.html')
    return HttpResponse(temp.render())
def  page_104(request):
    temp=loader.get_template('104.html')
    return HttpResponse(temp.render())
def  page_105(request):
    temp=loader.get_template('105.html')
    return HttpResponse(temp.render())
def  page_106(request):
    temp=loader.get_template('106.html')
    return HttpResponse(temp.render())
def  page_107(request):
    temp=loader.get_template('107.html')
    return HttpResponse(temp.render())
def  page_108(request):
    temp=loader.get_template('108.html')
    return HttpResponse(temp.render())




