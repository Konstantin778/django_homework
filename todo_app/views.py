from datetime import datetime

from django.shortcuts import render

from todo_app.models import TodoTask, TodoStatus, TodoList


def index(request):
    if request.method == 'POST':
        action_type = request.POST.get('type')
        if action_type == 'create':
            __create_task(request)

        if action_type == 'destroy':
            task_id = request.POST.get('task_id')
            TodoTask.objects.get(pk=task_id).delete()

        if action_type == 'clear':
            __clear_completed(request)

    else:
        action_type = request.GET.get('type')
        if action_type == 'change':
            __change_todo_status(request)

    tasks = TodoTask.objects.filter(todo_list__user=request.user)
    if request.GET.get('status') == 'yes':
        tasks = tasks.filter(status_id=TodoStatus.C_COMPLETED)
    elif request.GET.get('status') == 'no':
        tasks = tasks.filter(status_id=TodoStatus.C_NOT_COMPLETED)

    return render(request, 'todo_main.html', {
        'tasks_array': tasks.order_by('-id'),
    })


def __change_todo_status(request):
    task = TodoTask.objects.get(pk=request.GET.get('task_id'))
    if task.status == TodoStatus.objects.get(pk=TodoStatus.C_NOT_COMPLETED):
        task.status = TodoStatus.objects.get(pk=TodoStatus.C_COMPLETED)
    else:
        task.status = TodoStatus.objects.get(pk=TodoStatus.C_NOT_COMPLETED)
    task.save()

def __clear_completed(request):
    tasks = TodoTask.objects.\
        filter(todo_list__user=request.user).\
        filter(status_id=TodoStatus.C_COMPLETED).\
        delete()


def __create_task(request):
    todo_list = TodoList.objects.get(user=request.user)
    if todo_list is None:
        todo_list = TodoList(user=request.user, date=datetime.now())
        todo_list.save()
    todo = TodoTask()
    todo.title = request.POST.get('title')
    todo.status = TodoStatus.objects.get(pk=TodoStatus.C_NOT_COMPLETED)
    todo.create_at = datetime.now()
    todo.text = ''
    todo.todo_list = todo_list
    todo.save()