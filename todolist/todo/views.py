
from django.shortcuts import render, redirect

from django.contrib import messages

from .models import Todo

from datetime import *

import sys

from operator import attrgetter

todo = Todo.objects.all()
sortpk = 'id'

# Create your views here.
def index(request):
    global todo,sortpk
    todo = Todo.objects.all()
    if request.method=='POST': 

        l = ['', "Not Completed"]
        if ((request.POST['startdateplanned'] not in l) and (request.POST['completiondateplanned'] not in l) and (request.POST['title'] != '')) :
            new_todo = Todo(
                title = request.POST['title'], 
                startdateplanned = datetime.strptime(request.POST['startdateplanned'],'%Y-%m-%d'),
                completiondateplanned = datetime.strptime(request.POST['completiondateplanned'],'%Y-%m-%d')
                )

            if new_todo.startdateplanned <= new_todo.completiondateplanned:
                new_todo.save()
            else:
                new_todo.delete()
            return redirect('/')
            

    return render(request, 'index.html', {'todos': todo, 'sortpk': sortpk})
    

def delete(request, pk):
    todotemp = Todo.objects.get(id=pk)
    todotemp.delete()
    return redirect('/')
    
def complete(request,pk):
    todotemp = Todo.objects.get(id = pk)
    todotemp.completiondateactual = datetime.today()
    todotemp.save()
    return redirect('/')


def sort(request, pk):
    global sortpk,todo
    for t in todo:
        t.completiondateactual_text()
    if pk == 'completiondateactual':
        sortpk = 'completiondateactualtext'
    else:
        sortpk = pk

    return redirect('/')




