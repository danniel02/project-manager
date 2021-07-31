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

class tasks(models.Model):
    task_id = models.BigAutoField(primary_key=True)
    task_name = models.CharField(max_length=64)
    task_desc = models.TextField(max_length=500)
    task_start_date = models.DateField(auto_now_add=True)
    task_end_date = models.DateField
    def __str__(self):
        return self.task_name

class users(models.Model):
    users_id = models.BigAutoField(primary_key=True)
    users_first = models.CharField(max_length=64)
    users_last = models.CharField(max_length=64)
    users_username = models.CharField(max_length=64)
    users_password = models.CharField(max_length=64)
    users_bio = models.TextField(max_length=500)
    users_email = models.CharField(max_length=64)
    def __str__(self):
        return self.users_username