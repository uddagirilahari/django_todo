from django.urls import path

from ToDOList.views import *

urlpatterns =[
    path('', ListTodo.as_view()),
    path('create/', CreateTodo.as_view()),
    path('view/<int:pk>/', DetailTodo.as_view()),
    path('delete/<int:pk>/', DeleteTodo.as_view()),
]