from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/',blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/',blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #author : 추후 작성 예정
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 포스트의 작성자가 데이터베이스에서 삭제 되었을 때 작성자명을 빈 칸으로 둔다.
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]