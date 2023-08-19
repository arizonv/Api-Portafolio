# Proyecto ARIZONA

Bienvenido al proyecto NombreDelProyecto. Este archivo proporciona pasos claros sobre cómo configurar el proyecto correctamente.

## Pasos de configuración

1. Ejecuta las migraciones para preparar la base de datos:

```Terminal.
python manage.py makemigrations accounts cliente servicio
python manage.py migrate

2. funcionamiento de la api de cambio de estado de la resrva mediante el codigo :

```utl- /api/reserva/codigo/.

{
    'codigo':'codigo de la reserva que fue enviado al correo de pruebas'
}



├── 📁 accounts
│   ├── 📄 admin.py
│   ├── 📄 apps.py
│   ├── 📄 forms.py
│   ├── 📄 models.py
│   ├── 📁 templates
│   ├── 📄 tests.py
│   ├── 📄 urls.py
│   ├── 📄 views.py
│   ├── 📄 __init__.py
├── 📁 api
│   ├── 📄 admin.py
│   ├── 📄 apps.py
│   ├── 📄 models.py
│   ├── 📄 serializers.py
│   ├── 📄 tests.py
│   ├── 📄 transbank.py
│   ├── 📄 urls.py
│   ├── 📄 views.py
│   ├── 📄 __init__.py
├── 📁 cliente
│   ├── 📄 admin.py
│   ├── 📄 apps.py
│   ├── 📄 forms.py
│   ├── 📄 models.py
│   ├── 📁 templates
│   ├── 📄 tests.py
│   ├── 📄 transbank.py
│   ├── 📄 urls.py
│   ├── 📄 utils.py
│   ├── 📄 views.py
│   ├── 📄 __init__.py
├── 📁 core
│   ├── 📄 asgi.py
│   ├── 📄 settings.py
│   ├── 📄 urls.py
│   ├── 📄 wsgi.py
│   ├── 📄 __init__.py
|
├── 📁 servicio
│   ├── 📄 admin.py
│   ├── 📄 apps.py
│   ├── 📄 models.py
│   ├── 📁 templates
│   ├── 📄 tests.py
│   ├── 📄 urls.py
│   ├── 📄 views.py
│   ├── 📄 __init__.py
|   
├── 📁 static        
├── 📄 manage.py
├── 📄 proyecto.txt
├── 📄 proyecto_epicas.txt
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 db.sqlite3
|