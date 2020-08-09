from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Blogpost(models.Model):
    title=models.TextField(default="blog title",null=True,blank=True)
    content=models.TextField(default="blog content")
    def __str__(self):
        return self.title

    def get_absolute_url(self):
    	return reverse("main:detailview", kwargs={"id": self.id})

