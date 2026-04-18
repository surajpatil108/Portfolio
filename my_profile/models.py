from django.db import models

class TechStack(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.ManyToManyField(TechStack)
    github_link = models.URLField()
    live_demo = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title