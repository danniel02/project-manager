from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import generic
from .models import project, tasks
from django.urls import reverse


# Create your views here.
class IndexView(generic.TemplateView):

    template_name = 'view/index.html'



class ProjectView(generic.DetailView):
    model = project
    template_name = 'view/project.html'

class TaskView(generic.DetailView):
    model = tasks
    template_name = 'view/tasks.html'

    