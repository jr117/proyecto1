from django.urls import path
from apps.clientes.views import index, plantilla, especial, ViewClientes, nuevoRegistro, editarRegistro, eliminarRegistro

app_name = 'clientes'
urlpatterns = [
    path('index', index),
    path('', index),
    path('plantilla', plantilla, name="plantilla"),
    path('especial', especial, name="listaClientes"),
    path('verClientes', ViewClientes.as_view(), name="vistaClientes"),
    path('nuevoRegistro', nuevoRegistro, name="nuevoRegistro"),
    path('editarRegistro/<idCliente>', editarRegistro, name="editarRegistro"),
    path('eliminarRegistro/<idCliente>', eliminarRegistro, name="eliminarRegistro"),
]
