from django.db import models
from projects.models import Project


class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    order = models.IntegerField()
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title