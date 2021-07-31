from django.contrib import admin

from .models import project, tasks, users


# Register your models here.
admin.site.register(project)
admin.site.register(tasks)
admin.site.register(users)