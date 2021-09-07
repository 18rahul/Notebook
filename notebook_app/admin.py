from django.contrib import admin

from notebook_app.models import Todo, Note

admin.site.register(Todo)
admin.site.register(Note)
