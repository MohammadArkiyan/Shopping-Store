from django.contrib.auth.models import User
from django.db import models

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}"
