from django.shortcuts import render, redirect

from articles.models import Article

# Create your views here.
def index(request):
    articles = Article.objects.order_by("-pk")
    context = {"articles": articles}
    return render(request, "articles/index.html", context)


def new(request):
    return render(request, "articles/new.html")


def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    Article.objects.create(title=title, content=content)
    return redirect("articles:index")
