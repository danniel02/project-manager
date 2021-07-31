from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "view/index.html")

def project(request, project_id):
    #todo
    return HttpResponse(f"WIP: returns the project page of project id: {project_id}")