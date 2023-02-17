from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import Programmer

from .forms import ProgrammerForm

def index(request):
    return render(request, 'index.html')

def programmer_edit(request):
    return render(request, 'programmer_edit.html')

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