Oliver Garcia @oliverg09
Unai Uzquiza 
Jose Bueno 
Samuel de Leon

El trabajo empleado por el equipo se enfoca en una empresa de informática la cual desea tener una página web funcional y responsiva que puede utilizarse tanto por empleados como por clientes. El objetivo de la empresa es la posibilidad de comprar online si hablamos de los clientes, en cambio, si nos enfocamos en los empleados, tendrá funciones que irán derivadas sobre el control de stock, las compras que se realizan, etc. Será necesario registrarse para poder comenzar en la página web.

Para instalar la aplicación será necesario copiar el repositorio de github, con el comando “git clone (enlace de el repositorio)”. A continuación, deberás instalar las dependencias necesarias gracias a “poetry install”. Por último, para ejecutar la aplicación lo podremos hacer de dos maneras, ejecutando el main.py desde VisualCode o con el comando “poetry run flet run”.

Si deseamos ejecutarlo desde el móvil, dependerá del sistema operativo, ya que si es Android deberemos escribir “poetry run flet run —android”, sin embargo, si es IOS, el comando será “poetry run flet run —ios”.

Las dependencias necesarias para la aplicación las podremos observar en el archivo llamado “pyproject.toml”, las cuales en este caso serán necesarias las siguientes:

python = version "3.12" flet = version "0.25.1" pymongo = version "4.10.1"
