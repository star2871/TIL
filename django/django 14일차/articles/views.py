from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from articles.models import Article
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


def create(request):
    if request.method == "POST":
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/new.html", context=context)


def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # template에 객체 전달
    context = {
        "article": article,
        "comments": article.comment_set.all(),
        "comment_form": comment_form,
    }
    return render(request, "articles/detail.html", context)


def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect("articles:detail", article.pk)
