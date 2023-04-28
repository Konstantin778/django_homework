from todo_app.models import TodoTask


def todo_count(request):
    return {
        'todo_count': len(TodoTask.objects.all()),
    }