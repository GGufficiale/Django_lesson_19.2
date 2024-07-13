from django.shortcuts import render


def index(request):
    """Метод для обработки данных, получаемых на фротэнде при вводе пользователем"""
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'main/index.html')
