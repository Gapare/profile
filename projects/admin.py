from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Project, Skill, Profile

admin.site.register(Project)
admin.site.register(Skill)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location', 'image_preview')
    list_filter = ('location',)
    search_fields = ('name', 'bio', 'email')
    readonly_fields = ('image_preview',)
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'bio', 'profile_image', 'image_preview')
        }),
        ('Contact Info', {
            'fields': ('email', 'location')
        }),
        ('Social Links', {
            'fields': ('linkedin_url', 'github_url', 'twitter_url', 'personal_website_url'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        try:
            if obj.profile_image:
                print(f"Image name: {obj.profile_image.name}")
            super().save_model(request, obj, form, change)
        except Exception as e:
            import traceback
            raise

    def image_preview(self, obj):
        try:
            if obj.profile_image:
                return mark_safe(f'<img src="{obj.profile_image.url}" width="100" />')
            return "No Image"
        except Exception as e:
            return f"Error: {e}"
    image_preview.short_description = 'Preview'

    def image_preview(self, obj):
        if obj.profile_image:
            return mark_safe(f'<img src="{obj.profile_image.url}" width="100" />')
        return "No Image"
    image_preview.short_description = 'Preview'