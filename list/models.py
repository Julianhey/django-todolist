from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Todo(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    deadline_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(blank=True, null=True)
    completed = False

    def complete(self):
        self.completed_date = timezone.now()
        self.completed = True
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    todo = models.ForeignKey('list.Todo', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class GameInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    platform = models.CharField(default="Not specified", max_length=200)

    def __str__(self):
        return self.title
