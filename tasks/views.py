from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import TaskForm
from .models import Task


# Create your views here.

def task_list(request):
    # 从数据库获取Task对象列表
    tasks = Task.objects.all()

    # 指定渲染模板并向模板传递数据
    return render(request, 'tasks/task_list.html', {"tasks": tasks})


def task_create(request):
    if request.method == "POST":
        # 将用户提交数据与TaskForm表单绑定
        form = TaskForm(request.POST)

        if form.is_valid():
            # 保存数据
            form.save()

            # 重定向到任务列表
            return redirect(reverse("tasks:task_list"))
    else:
        # 否则空表单
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form, })


def task_detail(request, pk):
    # 从url里获取单个任务的pk值，然后查询数据库获得单个对象
    task = get_object_or_404(Task, pk=pk)

    # 指定渲染模板并向模板传递数据
    return render(request, "tasks/task_detail.html", {"task": task, })


def task_update(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        # 将用户提交数据与TaskForm表单绑定
        form = TaskForm(data=request.POST, instance=task_obj)

        if form.is_valid():
            # 保存数据
            form.save()

            # 重定向到任务列表
            return redirect(reverse("tasks:task_detail", args=[pk, ]))
    else:
        form = TaskForm(instance=task_obj)
    return render(request, "tasks/task_form.html", {"form": form, "object": task_obj})


def task_delete(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    task_obj.delete()  # 删除然后跳转
    return redirect(reverse("tasks:task_list"))
