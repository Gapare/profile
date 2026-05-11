from django.shortcuts import render
from django.http import JsonResponse
from blog.models import Post
from projects.models import Project, Skill, Profile

def projects_list(request):
    projects = Project.objects.all().order_by('-is_featured', '-created_at')
    skills = Skill.objects.all()
    profile = Profile.objects.first()
    return render(request, 'projects/list.html', {
        'projects': projects,
        'skills': skills,
        'profile': profile
    })

def custom_500_view(request):
    return render(request, '500.html', status=500)








def terminal_api(request):
    command = request.GET.get('command', '').lower()

    if command == "projects":
        projects = Project.objects.all()
        data = {
            "projects": [
                {
                    "title": p.title,
                    "description": p.description,
                    "tech_used": p.tech_used,
                    "github_url": p.github_url,
                    "live_url": p.live_url
                } for p in projects
            ]
        }
        return JsonResponse(data)

    elif command == "skills":
        skills = Skill.objects.all()
        data = {
            "skills": [
                {"name": s.name, "proficiency": s.proficiency} for s in skills
            ]
        }
        return JsonResponse(data)

    elif command == "about":
        profile = Profile.objects.first()
        data = {"about": profile.bio if profile else ""}
        return JsonResponse(data)

    elif command == "contact":
        profile = Profile.objects.first()
        if profile:
            data = {
                "contact": f"Email: {profile.email}\nGitHub: {profile.github_url}\nLinkedIn: {profile.linkedin_url}"
            }
        else:
            data = {"contact": ""}
        return JsonResponse(data)

    elif command == "blog":
        posts = Post.objects.filter(is_published=True)
        data = {
            "posts": [
                {"title": p.title, "author": p.author.username, "created_at": p.created_at, "excerpt": p.excerpt}
                for p in posts
            ]
        }
        return JsonResponse(data)

    return JsonResponse({"error": "Command not found"}, status=404)






def terminal_view(request):
    """Render the interactive terminal UI"""
    return render(request, 'terminal/terminal.html')

