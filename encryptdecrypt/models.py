from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    data = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.data