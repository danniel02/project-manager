from django.db import models

# Create your models here.
class project(models.Model):
    project_name = models.CharField(max_length = 64)
    project_desc = models.TextField(max_length=500, blank=True)
    project_id = models.BigAutoField(primary_key=True)
    project_start_date = models.DateField(auto_now_add=True)
    project_goal_date = models.DateField(blank=True)
    def __str__(self):
        return self.project_name


