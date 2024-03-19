# AppWeb-ObjectRecognition

Este proyecto consiste en una aplicación web que utiliza la cámara web de tu dispositivo para realizar reconocimiento de objetos en tiempo real. Hace uso de la combinación de tecnologías como OpenCV, YOLO (You Only Look Once) y Flask para lograr esta funcionalidad.

## Requerimientos
Se recomienda crear un entorno virutal para trabajar y no tener ningun problema.
- Python 3.11.7
- YOLO
- OpenCV-Python
- Flask

## Instalación de Requerimientos

Para instalar los requerimientos, puedes ejecutar el siguiente comando:

```bash
pip install -r requirements.txt

```
## Uso

Una vez que hayas instalado los requerimientos, puedes iniciar la aplicación ejecutando el siguiente comando en tu terminal:

```bash
python app.py

```
Esto iniciará el servidor Flask. Luego, puedes acceder a la aplicación desde tu navegador web visitando la dirección http://localhost:5000.

## Referencias de Bibliotecas

Este proyecto hace uso de las siguientes bibliotecas:

- **OpenCV**: OpenCV es una biblioteca de visión por computadora de código abierto que proporciona herramientas y algoritmos para procesar imágenes y videos.
  - [Sitio web oficial](https://opencv.org/)


- **YOLO (You Only Look Once)**: YOLO es un modelo de detección de objetos en tiempo real que detecta objetos en imágenes y videos.
  - [Sitio web oficial](https://docs.ultralytics.com/es/models/yolov5/)

- **Flask**: Flask es un framework web ligero de Python que permite construir aplicaciones web rápidamente y con un mínimo de líneas de código.
  - [Sitio web oficial](https://flask.palletsprojects.com/)


## Trabajos a Futuro

Este proyecto está en constante evolución. A continuación se enumeran algunas mejoras y características que podrían implementarse en el futuro:

- **Mejora del Aspecto Visual de la Web:** Actualmente, la interfaz de usuario de la aplicación web puede ser mejorada para proporcionar una experiencia más atractiva y fácil de usar para los usuarios. Esto puede incluir mejoras en el diseño, la disposición de los elementos y el uso de estilos modernos.

- **Implementación en Plataformas en la Nube:** Considera la posibilidad de implementar esta aplicación en plataformas en la nube como Google Cloud Platform (GCP), Amazon Web Services (AWS) o Microsoft Azure. La migración a una plataforma en la nube puede proporcionar escalabilidad, disponibilidad y rendimiento mejorados, así como integraciones con servicios adicionales que puedan enriquecer la aplicación.
