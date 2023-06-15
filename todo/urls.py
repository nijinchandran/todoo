from django.urls import path
from . import views





urlpatterns = [

    path('',views.todoview,name='todoview'),
    path('addTodoView',views.todolist,name='todolist'),
    path('addtodo',views.addtodo,name='addtodo'),
   path('delete/<int:pk>/',views.delete_todo, name='delete_todo'),
]
