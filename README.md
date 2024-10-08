# Proyecto de Reconocimiento Facial

Este proyecto utiliza OpenCV y PyQt6 para crear una aplicación de reconocimiento facial. Permite capturar imágenes, entrenar un modelo de reconocimiento y probar el reconocimiento de imágenes.

## Requisitos

Asegúrate de tener instalado Python 3.x. Este proyecto utiliza las siguientes bibliotecas:

- OpenCV
- NumPy
- imutils
- PyQt6

## Instalación

1. **Clona el repositorio** (si es aplicable) o descarga los archivos del proyecto.
2. **Crea un entorno virtual** y actívalo:

   ```bash
   python -m venv tutorial-env
   cd tutorial-env\Scripts\activate.bat
   ```

3. **Instala las dependencias** utilizando `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   O puedes instalar las dependencias manualmente:

   ```bash
   pip install opencv-contrib-python
   pip install imutils
   pip install opencv-python
   python -m pip install pyqt6
   pip install numpy
   ```

## Uso

1. **Capturar Imágenes**: Ingresa un nombre y haz clic en "Capturar Imagen" para tomar fotos que se almacenarán en la carpeta `imagenes`.
2. **Entrenar el Modelo**: Haz clic en "Entrenar Imagen" para entrenar el modelo de reconocimiento facial con las imágenes capturadas.
3. **Probar el Reconocimiento**: Haz clic en "Probar Imagen" para verificar el reconocimiento facial con las imágenes almacenadas.

## Estructura del Proyecto

```
src/
│
├── repository/
│   ├── CapturarImagen.py
│   ├── EntrenamientoImagen.py
│   ├── ProbarImagen.py
│   ├── Window.py
│   └── main.py
│
├── instalar.txt
├── entorno.txt
└── requirements.txt
```

## Notas

- Asegúrate de tener una cámara conectada y funcionando para capturar imágenes.
- Las imágenes se almacenarán en la carpeta `imagenes`, que se creará automáticamente si no existe.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
