# Descarga y Preparación del Padrón SUNAT

Este proyecto descarga el padrón SUNAT del día actual, lo descomprime y lo deja en un archivo `.txt` listo para ser usado o subido a una base de datos.

---

## Requisitos previos

- Descargar el driver de Microsoft Edge (EdgeDriver) compatible con tu versión de navegador desde [aquí](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) y colocar el ejecutable en la carpeta raíz del proyecto.

---

## Uso

1. Coloca el driver de Edge en la carpeta raíz del proyecto.

2. Ejecuta el script para que descargue automáticamente el padrón del día actual, lo descomprima y genere el archivo `.txt` correspondiente.

---

## Estructura de carpetas

```

/ (carpeta raíz)
\|-- msedgedriver.exe
\|-- main.py
\|-- Manage/
\|-- Output/
\|-- README.md

```

---

## Notas

- Asegúrate de que el EdgeDriver sea compatible con la versión de tu navegador Edge.
- El archivo `.txt` generado estará listo para su uso o carga en una base de datos.
- El proceso se basa en la descarga automática del padrón disponible en la fecha de ejecución.

---

Si tienes preguntas o sugerencias, no dudes en abrir un issue o contactarme.
```
