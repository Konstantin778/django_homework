from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.core.validators import validate_email
from django.shortcuts import render, redirect


def login_view(request: WSGIRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user: User = authenticate(
            request,
            username=username,
            password=password
        )
        if user is None:
            return render(request, 'login.html', {
                'error_message': 'Неправильный логин или пароль',
            })
        login(request, user)
        return redirect('todo_main')
    return render(request, 'login.html')


def registration(request: WSGIRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        email = request.POST['email']

        if password != password_confirm:
            return render(request, 'registration.html', {
                'error_message': 'Пароли не совпадают',
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'registration.html', {
                'error_message': 'Пользователь с таким именем уже существует',
            })

        try:
            validate_email(email)
        except Exception as e:
            return render(request, 'registration.html', {
                'error_message': 'Некорректный email',
            })


        user = User()
        user.username = username
        user.password = password
        user.email = email
        try:
            user.save()
            login(request, user)
        except Exception as e:
            return render(request, 'registration.html', {
                'error_message': 'Ошибка сервера',
            })

        return render(request, 'info.html', {
                'content': 'Реистрация прошла успешно',
            })

    return render(request, 'registration.html')


def logout_view(request: WSGIRequest):
    logout(request)
    return redirect('login')
def user_list(request: WSGIRequest):
    return render(request, 'user_list.html')


