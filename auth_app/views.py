from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.core.validators import validate_email
from django.shortcuts import render, redirect


def login_view(request: WSGIRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next_page = request.GET.get('next')

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

        if next_page is not None:
            return redirect(next_page)

        return render(request, 'info.html', {
            'content': 'Вы вошли в систему',
        })
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
        user.set_password(password)
        user.email = email
        try:
            user.save()
            login(request, user)
        except Exception as e:
            return render(request, 'registration.html', {
                'error_message': 'Ошибка сервера',
            })

        return render(request, 'info.html', {
                'content': 'Регистрация прошла успешно',
            })

    return render(request, 'registration.html')


def logout_view(request: WSGIRequest):
    logout(request)
    return redirect('login')


def user_list(request: WSGIRequest):
    if not request.user.is_superuser:
        return render(request, 'info.html', {
            'content': 'Недостаточно прав для просмотра этой страницы',
        })

    users = User.objects.all()
    return render(request, 'user_list.html', {
        'users': users
    })


def login_in_system(request: WSGIRequest):
    user = User.objects.get(pk=request.POST['user_id'])
    login(request, user)
    return redirect('login')


def delete_user(request: WSGIRequest):
    user = User.objects.get(pk=request.POST['delete_id'])
    try:
        user.delete()
        return render(request, 'info.html', {
            'content': f'Пользователь {user.username} удалён',
        })

    except User.DoesNotExist:
        return render(request, 'user_list.html', {
            'error_message': 'Такого пользователя не существует',
        })

    except Exception as e:
        return render(request, 'user_list.html', {
            'error_message': 'Ошибка сервера',
        })

    # return render(request, 'user_list.html')


