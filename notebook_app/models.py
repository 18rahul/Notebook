from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200, blank=False, null=False)
    date_created = models.DateField(auto_now=True, blank=False, null=False)

    def __str__(self):
        return self.content


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(null=False, blank=False)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.heading
