from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    Account_owner = models.ForeignKey(User,related_name="messages" , on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Account_owner.username + ": " + self.content[:50]