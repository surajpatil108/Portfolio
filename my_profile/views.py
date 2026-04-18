from django.shortcuts import render
from .models import Project

def home(request):
    # Get all projects from the DB
    projects = Project.objects.all().order_by('-created_at')
    # Send them to the 'index.html' template
    return render(request, 'index.html', {'projects': projects})