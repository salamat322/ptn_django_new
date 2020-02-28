from django.db import models
from posts.models import Post
from django.urls import reverse 


class Tag(models.Model):
    title = models.CharField(max_length=255)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("tag-detail", kwargs={"pk": self.pk})
    

