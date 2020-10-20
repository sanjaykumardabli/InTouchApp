from django.urls import path
from todolist_app import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('register', views.register, name='register'),
    path('update/<task_id>', views.update, name='update'),
    path('delete_task/<task_id>', views.delete_task, name='delete_task'),
    path('search/', views.search, name='search'),

]
