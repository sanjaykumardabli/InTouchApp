
from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_views.todolist, name='index'),
    path('task/', include('todolist_app.urls')),

]
