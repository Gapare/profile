from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from projects import views as project_views
from contact import views as contact_views

urlpatterns = [
    path('secure-admin/', admin.site.urls),
    path('', project_views.projects_list, name='home'),
    path('projects/', project_views.projects_list, name='projects'),
    path('contact/', contact_views.contact_view, name='contact'),
    path('blog/', include('blog.urls')),
    path('terminal/', project_views.terminal_view, name='terminal'),
    path("terminal/api/", project_views.terminal_api, name="terminal_api"),
]
handler500 = 'projects.views.custom_500_view'
