from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title=models.TextField()

    def __str__(self):
        return self.title

