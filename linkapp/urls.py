
from django.urls import path
from . import views

app_name = 'linkapp'
urlpatterns = [
    path('',views.home, name='home'),
    path('agregar/', views.agregar, name='agregar'),
    path('editar/<str:pk>', views.editar, name='editar'),
    path('eliminar/<str:pk>', views.eliminar, name='eliminar'),
    

]