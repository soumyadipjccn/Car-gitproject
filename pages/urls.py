# urls.py
from django.urls import path
from . import views # Assuming the views.py is in the same directory as urls.py

urlpatterns = [
    path('', views.home, name='home'),
]
