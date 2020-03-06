from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()
    image = models.ImageField(upload_to="posts", blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # likes = models.ManyToManyField(User, related_name='likes')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    



class Comment(models.Model):
    comment = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class LikeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    
