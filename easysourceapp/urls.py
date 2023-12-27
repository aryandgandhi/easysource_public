"""
URL configuration for easysourceapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from github_fetcher import views
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from github_fetcher.views import toggle_star

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects_view, name='projects_view'),
    path('api/projects/<str:difficulty>/', views.api_projects, name='api_projects'),

    path('starred/', views.starred_projects, name='starred_projects'),
    path('toggle_star/<int:project_id>/', toggle_star, name='toggle_star'),
    
    path('accounts/', include('django.contrib.auth.urls')),  # add this
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),

    path('accounts/profile/', RedirectView.as_view(url='/'), name='account_profile'),
    path('api/projects/', views.api_projects, name='api_projects'),
    path('api/project/<int:project_id>/', views.api_project_detail, name='project-detail'),
    path('api/project/<int:project_id>/issues/', views.api_issues, name='api_issues'),
    path('api/issue/<int:issue_id>/', views.api_issue_detail, name='issue-detail'),
    path('easy/', views.easy_projects, name='easy_projects'),
    path('medium/', views.medium_projects, name='medium_projects'),
    path('hard/', views.hard_projects, name='hard_projects'),
]
