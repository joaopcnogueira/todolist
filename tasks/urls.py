from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="task-index"),
    path('task/', views.index, name="task-index"),
    path('task/<int:id>', views.show, name="task-show"),
    path('task/create', views.create, name="task-create"),
    path('task/store', views.store, name="task-store"),
]