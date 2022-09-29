from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.order_by("priority")
    context = {
        "todos": todos,
    }
    return render(request, "day5/index.html", context)


def create(request):
    content = request.GET.get("content")
    created_at = request.GET.get("created_at")
    deadline = request.GET.get("deadline")
    priority = request.GET.get("priority")

    Todo.objects.create(
        content=content,
        created_at=created_at,
        deadline=deadline,
        priority=priority,
    )
    context = {
        "content": content,
        "created_at": created_at,
        "deadline": deadline,
        "priority": priority,
    }

    return redirect("day5:index")


def change(request, pk_):
    target = Todo.objects.get(id=pk_)
    if target.completed:
        target.completed = False
    else:
        target.completed = True
    target.save()
    return redirect("day5:index")


def delete(request, pk):
    # pk에 해당하는 글 삭제
    target = Todo.objects.get(id=pk)
    target.delete()
    return redirect("day5:index")
