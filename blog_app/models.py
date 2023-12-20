from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    img=models.ImageField(upload_to="posts/")
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
    