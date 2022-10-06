from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # 이런 식으로 사용하면 db에서 제목, 내용, 만든시간, 수정시간을 admin페이지 나타나게 한다.
    list_display = ("title", "content", "created_at", "updated_at")


admin.site.register(Article, ArticleAdmin)
