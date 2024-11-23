# 



 
<h1 align="center"> Optimización de la Gestión de Reportes en Redes Eléctricas mediante Inteligencia Artificial </h1>
 
 
# Descripción
 
Este proyecto tiene como objetivo desarrollar un modelo de inteligencia artificial para gestionar y categorizar reportes de fallas en las redes eléctricas de manera eficiente. Utilizando la metodología Scrum, se garantiza un enfoque ágil para el desarrollo del modelo, priorizando la colaboración, la adaptabilidad y la mejora continua. Se espera que el sistema automatice procesos, reduzca costos operativos y mejore la calidad del servicio 

# Ejecucion Usuario Final

El proyecto esta desplegado en un AKS (Azure Kubernetes) el cual se puede ejecutar desde la siguiente IP Pública:

http://4.200.97.223/

solo se requiere conexión a internet.

 
# Instalación y uso en modo local
 
Para ejecutar la aplicacion en modo local debe tener instaladas las siguientes aplicaciones:

Python 3.10 o superior
Gitbash o Github Desktop
Docker desktop
visual Studio Code
 
Desde tu editor de código de preferencia:
- clonar proyecto<br>
    git clone
    https://github.com/camoreno368/Clasificador_CelsiaHF.git --- comando en consola
 
- Acceder a ubicación del proyecto<br>
    cd 'url carpeta' --- comando en consola    
  
- Habilitar ambiente virtual<br>
$ source <ruta>/venv/Scripts/activate
 
- Ejecutar instalación de liberías<br>
$ pip install -r requirements.txt

- Ejecutar la aplicacion<br>
$ python main.py

en la consola mostrara un link a las siguiente IP 127.0.0.1:7860, al dar clic le abrira el navegador con la interfaz de aplicacion


# Ejecucion en Docker
 
- Iniciar ejecución proyecto<br>
    docker build -t nombre_archivo .<br><br>
 
    docker run -it nombre_archivo<br>

en la consola mostrara un link a las siguiente IP 127.0.0.1:7860, al dar clic le abrira el navegador con la interfaz de aplicacion
 

 
# Librerías
 
pandas |
scikit-learn |
torch |
transformers |
gradio |
chardet 
 
 
 
# Autores
 
Cesar Moreno <br>
Rober Borja <br>
Camilo Ortiz <br>
Diego Parra <br>
UAO
 

 
 
