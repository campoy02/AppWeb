Para el correcto funcionamento de la aplicacion web es necesario cumplir con requisitos previos
Este archivo esta escrito considerando que se está utilizando MySQL Workbench y Visual Studio Code para manipular la BDD y el código respectivamente.

En Visual Studio Code, se hara lo siguiente:
1.- Activar entorno virtual de Python (CTRL + Shift + P -> Escribir Python -> Seleccionar "Activar Entorno" / "Activate Enviroment")

2.- Escribir en terminal los siguientes comandos:

pip install flask
pip install flask_login
pip install flask_mysqldb
pip install functools

-En caso de que siga sin funcionar, Cerrar y abrir Visual Studio
Posteriormente, abrir una nueva terminal y escribir los comandos de "pip install" de nuevo 
A Veces el IDE no reconoce el entorno virtual hasta que haces esto por lo que en ocasiones es necesario hacerlo 

- Aqui terminan los pasos necesarios para el funcionamiento de App.Py-

Para el funcionamiento de la Base de Datos:

Para crear el usuario: 
1.-El primer paso para poder utilizar la base de datos es dar click en "+" en la seccion que dice "MySQL Connections"

2.-Se abrira una interfaz, en "Connection Name" se puede colocar cualquier nombre 

3.- Dejar tal como estan todos los otros campos y dar click a OK 

4.- Se creará una conexión para el usuario root 

5.- Entrar y en el recuadro izquierdo dar click en "Administration" 

6.- Click en "Users and Privileges"

7.- Se abrira una nueva pestaña, abajo a la izquierda dar click en "add account" 

8.- En el campo "Login Name" Escribir Python

9.- En el campo "Password" y "Confirm Password" escribir 123 

10.- Ir a la pestaña "Administrative Roles" y hacer click en el recuadro "DBA"

11.- Hacer click en "Apply" abajo a la derecha 


Para crear la conexión: 

1.-El primer paso para poder utilizar la base de datos es dar click en "+" en la seccion que dice "MySQL Connections"

2.-Se abrira una interfaz, en "Connection Name" se puede colocar cualquier nombre 

3.-"Hostname" y "Port" se dejaran igual

4.-Username: Python 

5.-Password -> Dar click en store in vault -> 123 

6.-Dar click en OK 

7.-Ingresar a la base de datos a traves de el usuario creado 




Para importar la base de datos que esta en la carpeta llamada BASE DE DATOS(Importar)

1.-Una vez dentro, Click en Server 

2.-Data Import 

3.- Click en "..." y buscar la carpeta de este proyecto 

4.- Elegir la carpeta llamada "BASE DE DATOS(Importar)"

5.-En el recuadro izquierdo debe de aparecer un schema llamado "tiendarecetitas"

6.- En la seccion que dice "Default Targe Schema", dar click en el boton que dice "New..." 

7.- Se abrira una ventana con un campo de texto, Escribir tiendarecetitas en ella y click en OK 

8.-Click en Start Import 

9.-La base de datos ya está importada 

10.- Dar click en file y seleccionar New Query Tab  

11.- Copiar y Pegar el contenido de "Procedimientos.sql"  

12.- Click en el boton del rayo 


