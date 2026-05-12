from django.shortcuts import render
from django.http import JsonResponse
from blog.models import Post
from django.shortcuts import get_object_or_404, redirect
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


def download_app(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if project.apk_url:
        return redirect(project.apk_url)
    elif project.apk_file:
        return redirect(project.apk_file.url)
    return redirect('projects_list') # Fallback if no file exists





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
                    # Provide the clean fiks.co.zw download link to the terminal
                    "download_url": f"https://fiks.co.zw/download/{p.id}/" if (p.apk_url or p.apk_file) else None,
                    "version": p.version
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

