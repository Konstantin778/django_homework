from datetime import datetime

from django.shortcuts import render

from todo_app.models import TodoTask, TodoStatus, TodoList


def index(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        if type == 'create':
            todo = TodoTask()
            todo.title = request.POST.get('title')
            todo.status = TodoStatus.objects.get(pk=TodoStatus.C_NOT_COMPLETED)
            todo.create_at = datetime.now()
            todo.text = ''
            todo.todo_list = TodoList.objects.get(pk=1)
            todo.save()
        if type == 'destroy':
            task_id = request.POST.get('task_id')
            todo = TodoTask.objects.get(pk=task_id)
            todo.delete()

    return render(request, 'todo_main.html', {
        'tasks_array': TodoTask.objects.all().order_by('-id')
    })
