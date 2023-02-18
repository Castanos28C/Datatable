from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Programmer

from .forms import ProgrammerForm

def index(request):
    return render(request, 'index.html')

def programmer_delete(request, codigo):
    programmer = programmer.objects.get(codigo=codigo)
    programmer.delete()
    
    return redirect('/programmer/')

def programmer_edit(request, codigo):
    programmer = programmer.objects.get(codigo=codigo)
    programmer.delete()
    
    return redirect('/programmer/')

def programmer(request):
    return render(request, 'programmer.html')

def programmer_create(request):
    if request.method == "GET":
        return render(request, 'programmer_create.html', {"form": ProgrammerForm})
    else:
        try:
            form = ProgrammerForm(request.POST)
            new_programmer= form.save(commit=False)
            new_programmer.save()
            return redirect('programmer')
        except ValueError:
                return render(request, 'programmer_create.html', {"form": ProgrammerForm, "error": "Error creando al programador."})


def list_programmers(_request):
    programmers = list(Programmer.objects.values())
    data = {'programmers': programmers}
    return JsonResponse(data)
