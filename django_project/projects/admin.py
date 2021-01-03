from django.contrib import admin
from .models import Project, Status, ProjectTags, Task

admin.site.register(Project)
admin.site.register(Status)
admin.site.register(ProjectTags)
admin.site.register(Task)
