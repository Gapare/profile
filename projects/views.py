from django.shortcuts import render
from .models import Profile, Project, Skill

def projects_list(request):
    projects = Project.objects.all().order_by('-is_featured', '-created_at')
    skills = Skill.objects.all()
    profile = Profile.objects.first()
    return render(request, 'projects/list.html', {
        'projects': projects,
        'skills': skills,
        'profile': profile
    })