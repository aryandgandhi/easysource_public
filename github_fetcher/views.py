from django.shortcuts import render
from django.http import JsonResponse
from .models import Project, Issue, StarredProject
from random import shuffle

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.forms.models import model_to_dict






@login_required
def starred_projects(request):
    starred_projects = StarredProject.objects.filter(user=request.user)
    project_list = []
    for starred_project in starred_projects:
        project = starred_project.project
        project_dict = model_to_dict(project)
        project_dict['issues'] = list(Issue.objects.filter(project_id=project.id).values())
        project_list.append(project_dict)
    return render(request, 'github_fetcher/starred_projects.html', {'projects': project_list})



@login_required
@require_POST
def toggle_star(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    starred_project, created = StarredProject.objects.get_or_create(user=request.user, project=project)

    if not created:  # if the user has already starred this project
        starred_project.delete()  # unstar the project

    return JsonResponse({'starred': created})  # JsonResponse with the new star status

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in
            return redirect('index')  # or wherever you want to redirect to check the rendering here
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



def index(request):
    return render(request, 'github_fetcher/index.html')  

def projects_view(request):
    projects = Project.objects.all()[:10] #returns top 10 projects
    return render(request, 'github_fetcher/projects.html', {'projects': projects})


def api_projects(request, difficulty=None):
    # If a difficulty was specified, filter the issues by that difficulty
    if difficulty is not None:
        projects = list(Project.objects.filter(issue__difficulty=difficulty).values())
    else: # If no difficulty was specified, return all projects
        projects = list(Project.objects.values())
    
    shuffle(projects)
    for project in projects:
        project_obj = Project.objects.get(id=project['id'])
        project['issues'] = list(Issue.objects.filter(project_id=project['id']).values())
        project['readme'] = project_obj.readme
        project['summary'] = project_obj.summary
        if request.user.is_authenticated:
            project['starred'] = StarredProject.objects.filter(user=request.user, project=project_obj).exists()
        else:
            project['starred'] = False


    return JsonResponse(projects, safe=False)

def api_project_detail(request, project_id): #
    project = Project.objects.get(id=project_id)
    
        
    data = {
        'name': project.name,
        'description': project.description,
        'readme': project.readme,
        'summary': project.summary,
        'issues': list(Issue.objects.filter(project_id=project.id).values()),
    }
    if request.user.is_authenticated:
        data['starred'] = StarredProject.objects.filter(user=request.user, project=project).exists()
    else:
        data['starred'] = False
    return JsonResponse(data)

def api_issues(request, project_id):
    issues = list(Issue.objects.filter(project_id=project_id).values())
    for issue in issues: 
        issue_obj = Issue.objects.get(id=issue['id'])
        issue['bard_summary'] = issue_obj.bard_summary
    return JsonResponse(issues, safe=False)

def api_issue_detail(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    data = {
        'title': issue.title,
        'description': issue.description,
        'bard_summary': issue.bard_summary
    }
    return JsonResponse(data)





def easy_projects(request):
    response = api_projects(request, 'easy')
 
    return render(request, 'github_fetcher/easy_projects.html', {'projects': response})

def medium_projects(request):
    response = api_projects(request, 'medium')

    return render(request, 'github_fetcher/medium_projects.html', {'projects': response})

def hard_projects(request):
    response = api_projects(request, 'hard')

    return render(request, 'github_fetcher/hard_projects.html', {'projects': response})
# And remove the other 3 views (easy_projects, medium_projects, hard_projects)
