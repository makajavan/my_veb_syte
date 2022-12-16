from django.shortcuts import render
from django.http import HttpResponse
from .models import Fruits
from .models import FruitForm


def index(request):
    fruits = Fruits.objects.all()
    return render(request, 'fruits.html', {'fruits': fruits})



def create(request):
    if request.method == 'POST':
        print(request.POST['name'])
        print(request.POST['description'])
        print(request.POST['img'])

    form = FruitForm()

    data = {
        'form': form
    }
    return render(request, 'create.html', data)
