from django.shortcuts import render

# Create your views here.

tasks = ['check email',  'do homework']

def index(request):
    return render(request, "tasks/index.html", {
        "tasks" : tasks
    })
