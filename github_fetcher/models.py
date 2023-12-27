from django.db import models
from django.contrib.auth.models import User
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    github_url = models.URLField()
    summary = models.TextField(default="")
    readme = models.TextField(default="")
    starred_by = models.ManyToManyField(User, through='StarredProject', related_name='starred_projects') #allows user.starred_projects to be called to pull xyz projects

class Issue(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_url = models.URLField()
    bard_summary = models.TextField(null=True, blank=True)
    difficulty = models.CharField(max_length=10, default="")



class StarredProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_starred = models.DateTimeField(auto_now_add=True)