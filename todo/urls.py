from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todoviews,name='todoviews'),
    path('addtodo/', views.addTodo, name='addTodo'),
    path('deletetodo/<int:todo_id>/', views.deleteTodo, name='deleteTodo'),

    
]
