from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, default='Write stuff here...')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)