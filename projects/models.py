from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    # Cloudinary handles this automatically via settings.py
    profile_image = models.ImageField(upload_to="profile_images/", blank=True, null=True)
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
    image = models.ImageField(upload_to="project_images/", blank=True, null=True)
    
    # NEW: The field for our Google Drive magic link
    apk_url = models.URLField(
        blank=True, 
        null=True, 
        verbose_name="Direct APK Download URL",
        help_text="Paste the Google Drive direct link here to bypass Vercel/Cloudinary size limits."
    )
    
    # Keep this for small utilities (<10MB) that might fit on Cloudinary
    apk_file = models.FileField(upload_to="apks/", blank=True, null=True)
    
    version = models.CharField(max_length=20, default="v1.0.0")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.version})"

class Skill(models.Model):
    # For a professional look, let's add categories
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('mobile', 'Mobile'),
        ('tools', 'Tools'),
    ]
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='backend')
    proficiency = models.IntegerField(default=80, help_text="Enter a value from 0 to 100")
    icon_class = models.CharField(max_length=50, default="fab fa-python", help_text="FontAwesome class e.g., 'fab fa-flutter'")

    def __str__(self):
        return self.name