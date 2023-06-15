from django.shortcuts import render,redirect
from .models import TodoList


# Create your views here.


def todoview(request):
    return render(request,'todolist.html')


def addtodo(request):
    if request.method=='POST':
        content = request.POST['content']


        x = TodoList(content=content)
        x.save()
        return redirect('todolist')
    

def todolist(request):
    todo = TodoList.objects.all()
    return render(request,'todolist.html',{'todos':todo})


def delete_todo(request,pk):
    p = TodoList.objects.get(id=pk)
    p.delete()
    return redirect('todolist')