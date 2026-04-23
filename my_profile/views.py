from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Project
import re 
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


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

def hire_me(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message and re.match(r"[^@]+@[^@]+\.[^@]+", email):
            send_mail(
                subject=f"New Hire request from {name}",
                message=f"Name: {name}\nEmail: {email}\nMessage: {message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["surajpatil9197@zohomail.in"]
            )
            messages.success(request, "✅ Message sent! I'll get back to you soon.")
        else:
            messages.error(request, "⚠️ Please fill in all fields with valid information.")
        return redirect('hire_me')
    return render(request, "hire_me.html")

