import os

from django.http import HttpResponse
from django.shortcuts import render


def convert_file(temp_file_path, new_file_path, form):
    if form == 'pdf':
        # Преобразование docx в pdf
        if temp_file_path.endswith('.docx'):
            pass


def converter(request):
    if request.method == 'POST' and request.FILES['file']:
        # Получаем загруженный файл
        file = request.FILES['file']
        # Получаем формат, выбранный при отправке формы
        form = request.POST['format']
        # Получаем расширение загруженного файла
        ext = os.path.splitext(file.name)[1]
        # Создаём временный файл
        temp_file_path = 'temp_file{}'.format(ext)
        with open(temp_file_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        # Конвертируем файл в новое расширение
        new_file_path = 'new_file.{}'.format(form)
        convert_file(temp_file_path, new_file_path, form)
        os.remove(temp_file_path)
        # Отправляем конвертированный файл на скачивание
        with open(new_file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/{}'.format(form))
            response['Content-Disposition'] = 'attachment; filename={}'.format(os.path.basename(new_file_path))
            return response
    return render(request, 'converter.html')
