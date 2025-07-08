from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    file = models.FileField(upload_to='project_files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    downloads = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
