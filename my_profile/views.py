from django.shortcuts import render
from .models import Project

def home(request):
    # Get all projects from the DB
    projects = Project.objects.all().order_by('-created_at')
    # Send them to the 'index.html' template
    return render(request, 'index.html', {'projects': projects})

def domains(request):
    domains = [
        {'name': 'Web Development', 'description': 'Building responsive and dynamic websites using Django, React, and more.'},
        {'name': 'services', 'description': 'Offering a range of services including web development, consulting, and training.'},
        {'name': 'Blog', 'description': 'Content & news platforms'},
    ]
    return render(request, 'domains.html', {'domains': domains})