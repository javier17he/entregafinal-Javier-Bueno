EntregaFinal-javier Bueno
Catering - Pagina Web

Pagina web en desarrollo con el fin de crear y ver usuarios, consultas y proyectos de arquitectura
Instalacion requerida

Para ver este proyecto es necesario tener instalado Django y en un principio ejecutar las siguientes lineas de codigo para evitar posibles errores.

1- Para asegurarnos que el proyecto funcione correctamente se ha creado un archivo llamado requirements.txt que contiene todo lo necesario para que el proyecto se ejecute de forma correcta. Para hacer uso de esta facilidad siemplemente en terminal (ubicado en el directorio donde se encuentra el archivo) hay que escribir:

windows

  pip install -r requirements.txt

MacOS

  pip3 install -r requirements.txt

De esta forma nos aseguramos que tendremos instalado todo lo necesario para ejecutar de forma correcta el proyecto.

2- Para que se cree la base de datos en donde haremos la interaccion, posicionandose en terminal en la carpeta que contiene el archivo manage.py haremos:

windows

  python manage.py makemigrations 

  python manage.py migrate 

MacOS

  python3 manage.py makemigrations 

  python3 manage.py migrate 

3- Para ejecutar el servidor que nos permitirá ver la pagina en un navegador habra que ejecutar el siguiente codigo:

windows

  python manage.py runserver 

MacOS

  python3 manage.py runserver

Para acceder a la pagina en el navegador se debe escribir la siguiente url:

  localhost:8000/ 

Esto mostrara disponible dos Apps, la correspondiente a la seccion de admin y a la App de la pagina en desarrollo.

4- Se recomienda hacer una base de datos nueva y la creacion de un superuser. Para ello en terminal habra que escribir lo siguiente, y seguir las instrucciones: windows

  python manage.py createsuperuser 

MacOS

  python3 manage.py createsuperuser

Admin Page

Se puede acceder a la pagina de admin (previa la creacion del superuser) mediante la url:

  localhost:8000/admin

AppCat - Catering

Se puede acceder a la pagina de admin mediante la url:

  localhost:8000/AppCat/

