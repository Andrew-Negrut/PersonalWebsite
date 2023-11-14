from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)

    description = models.TextField()

    github_link = models.URLField()

    youtube_link = models.URLField(blank=True, null=True)

    order = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    
class Experience(models.Model):
    name = models.CharField(max_length=250)

    start_date = models.CharField(max_length=50)

    end_date = models.CharField(max_length=50)

    description = models.TextField()

    def __str__(self):
        return self.name