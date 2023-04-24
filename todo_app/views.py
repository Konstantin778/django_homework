from datetime import datetime

from django.shortcuts import render

from todo_app.models import TodoTask, TodoStatus, TodoList


def __create_task(request):
    todo = TodoTask()
    todo.title = request.POST.get('title')
    todo.status = TodoStatus.objects.get(pk=TodoStatus.C_NOT_COMPLETED)
    todo.create_at = datetime.now()
    todo.text = ''
    todo.todo_list = TodoList.objects.get(pk=1)
    todo.save()


def index(request):
    if request.method == 'POST':
        action_type = request.POST.get('type')
        if action_type == 'create':
            __create_task(request)

        if action_type == 'destroy':
            task_id = request.POST.get('task_id')
            TodoTask.objects.get(pk=task_id).delete()

    return render(request, 'todo_main.html', {
        'tasks_array': TodoTask.objects.all().order_by('-id')
    })
