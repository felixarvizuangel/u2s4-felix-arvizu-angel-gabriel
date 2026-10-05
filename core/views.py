# render: función que combina una plantilla con datos y arma la respuesta HTTP
from django.shortcuts import render
# connection: objeto de Django que expone la configuración de la base de datos activa
from django.db import connection
# Servicio: el modelo importado desde la app local para consultar la BD
from .models import Servicio

# Vista principal que muestra la conexión a la base de datos
def inicio(request):
    info_bd = connection.settings_dict
    contexto = {
        'motor': info_bd['ENGINE'],
        'host': info_bd['HOST'],
    }
    return render(request, 'core/inicio.html', contexto)

# Vista de servicios conectada directamente a MySQL
def servicios(request):
    # Pide todos los registros guardados en la tabla de servicios
    lista_servicios = Servicio.objects.all()
    return render(request, 'core/servicios.html', {'servicios': lista_servicios})