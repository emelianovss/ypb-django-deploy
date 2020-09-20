from django.shortcuts import render
from files.models import MyModel


def list_view(request):
    items = MyModel.objects.all()
    return render(request, 'index.html', {'items': items})

