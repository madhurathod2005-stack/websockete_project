from django.db import models

class Message(models.Model):
    room = models.CharField(max_length=100)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)