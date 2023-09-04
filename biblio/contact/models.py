from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"massage from: {self.name}"