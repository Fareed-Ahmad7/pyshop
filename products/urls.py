from django.urls import path
from . import views

# mapping url( http://127.0.0.1:8000/products/ ) to view function index (view function is that which sends data(
#  response) when requested)

urlpatterns = [
    path('', views.index), #dont call function
    path('new', views.new)
]