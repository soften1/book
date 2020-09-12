from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# def index(request):
#     header_str = 'eiei'
#     template = loader.get_template('index.html')
#     context = {
#         'var1' : header_str
#     }
#     return HttpResponse(template.render(context, request))
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def quota(request):
    return render(request, 'quota.html')

def myquota(request):
    return render(request, 'myquota.html')

def admin(request):
    return render(request, 'admin.html')

def user(request):
    return render(request, 'user.html')