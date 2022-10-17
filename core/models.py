

import uuid
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    added_at = models.DateTimeField('added_at')


class Command(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    command_text = models.CharField(max_length=200)
    added_at = models.DateTimeField('added_at')
    updated_at = models.DateTimeField('updated_at',null = True)
