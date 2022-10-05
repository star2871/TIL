from django.db import models

# Create your models here.
"""
게시판 기능
- 제목(50글자이내)
- 내용(긴 글)
- 글 작성시간/수정시간(자동으로 기록, 날짜/기록)
"""


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
