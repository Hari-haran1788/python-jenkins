from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Jenkins Docker Django 🚀")

urlpatterns = [
    path('', home),
]
