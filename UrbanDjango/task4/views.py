from django.shortcuts import render


def home(request):
    return render(request, 'fourth_task/home')


def shop(request):
    return render(request, 'fourth_task/shop', {
        'toys': ["Мишка", "Зайчик", "Котёнок"]
    })


def cart(request):
    return render(request, 'fourth_task/cart')