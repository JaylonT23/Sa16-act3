from django.shortcuts import render
from .models import Project, Skill

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects, 'skills': skills})

def about(request):
    # Add logic to fetch bio, education, etc.
    return render(request, 'portfolio/about.html')

def contact(request):
    # Add logic to handle contact form submission
    return render(request, 'portfolio/contact.html')
