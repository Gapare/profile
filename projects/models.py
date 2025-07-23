from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to="profile_images/")
    location = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    personal_website_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_used = models.CharField(max_length=200)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="project_images/")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(default=80)
    icon_class = models.CharField(max_length=50, default="fab fa-python")

    def __str__(self):
        return self.name