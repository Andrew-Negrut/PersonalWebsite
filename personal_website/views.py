from django.http import HttpResponse
from django.shortcuts import render

from .models import Project, Experience

def home_page_view(request):
    projects = Project.objects.all().order_by('order')
    return render(request, "home.html", {"projects":projects})

def experience_page_view(request):
    experiences = Experience.objects.all()
    return render(request, "experience.html", {"experiences":experiences})

def resume_page_view(request):
    return render(request, "resume.html")

def about_page_view(request):
    return render(request, "about.html")