
from django.shortcuts import render, redirect
from django.urls import path
from todolist_app.forms import TaskForm
from todolist_app.models import Details
from django.db.models import Q
import random
# Create your views here.
def rand_num():
    rand = random.randint(1, 16)
    return rand

def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)

        if form.is_valid():
            form.save()
            #messages.success(request, "Succefully created !")


        return redirect('todolist')
    else :
        form = TaskForm()
        allTasks = Details.objects.all()

        return render(request, 'index.html', {'allTasks': allTasks, 'form':form})

def register(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
           # messages.success(request, "Succefully created !")

        return redirect('todolist')
    else :

        allTasks = TaskForm()

        return render(request, 'register.html' , {'allTasks':allTasks})# 'rand':rand})

def delete_task(request, task_id):
    task = Details.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

def update(request, task_id):
    if request.method == 'POST':
        task = Details.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
        #messages.success(request, "Succefully Updated !")

        return redirect('todolist')
    else :
        allTasks = Details.objects.all()
        task_obj = Details.objects.get(pk=task_id)
        rand = rand_num()
        return render(request, 'index.html', {'task_obj':task_obj,  'allTasks':allTasks, 'rand':rand})
        #return r
        # edirect('todolist')


def search(request):
    if request.method == 'POST':
        srch = request.POST['srch']
        if srch :
            match = Details.objects.filter(Q(firstName__icontains=srch) |
                                            Q(lastName__icontains=srch) |
                                            Q(emailAddress__icontains=srch) |
                                            Q(displayName__icontains=srch) |
                                            Q(homePhone__icontains=srch)
                                            )
            if match :

                return render(request, 'search.html', {'sr': match})

    rand = rand_num()
    return render(request, 'search.html', {'rand':rand})


def index(request):
    context = {
        'index_text':"Welcome Index Page.",
        }
    return render(request, 'index.html', context)


