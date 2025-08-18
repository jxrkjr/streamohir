from django.db import models

from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class TimeStempModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(TimeStempModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/images/", null=True)
    video = models.URLField(blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Like(TimeStempModel):
    post = models.ForeignKey("Post",on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    class Meta:
       ordering = ['-created_at']
       unique_together = ['user','post']

    def __str__(self):
        return f"{self.user.username}:{self.post.title}"


