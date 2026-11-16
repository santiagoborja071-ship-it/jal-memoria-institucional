# Memoria institucional de la JAL Comuna 12

Proyecto de servicio social desarrollado por **Santiago Borja** para facilitar la consulta de actas y otros documentos de la Junta Administradora Local. El objetivo es buscar por tema en español y recuperar fragmentos junto con el nombre del archivo de origen.

## Qué hace esta versión

| Archivo | Función |
| --- | --- |
| [`db.py`](db.py) | Crea la base local `conocimiento.db` y la tabla de fragmentos con SQLite. |
| [`ingest.py`](ingest.py) | Lee PDF con texto seleccionable y párrafos de Word (`.docx`). Guarda fragmentos de hasta 500 caracteres y su nombre de archivo. |
| [`index.py`](index.py) | Genera un vector por cada fragmento pendiente con FastEmbed y lo guarda en SQLite como bytes de NumPy. |
| [`documentos/`](documentos/) | Carpeta de entrada. Incluye la guía de estudio para hacer una prueba inicial. |

## Probar el flujo en Windows

Abre PowerShell en la raíz del repositorio, donde están los tres scripts. Comprueba que `python --version` muestre Python 3.12 para seguir el entorno de este ejemplo.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install pdfplumber python-docx numpy fastembed
```

Puedes usar la [guía de estudio incluida](documentos/Guia_de_estudio_para_Santi_v2.docx) como entrada o poner documentos ficticios en `documentos/`. Ejecuta los pasos en este orden:

```powershell
.\.venv\Scripts\python.exe db.py
.\.venv\Scripts\python.exe ingest.py
.\.venv\Scripts\python.exe index.py
```

- La ingestión muestra cuántos fragmentos guarda por archivo. Los PDF escaneados que solo contienen imágenes requieren OCR, una capacidad pendiente.
- La primera ejecución de `index.py` puede requerir internet para descargar el modelo. El script informa cuántos fragmentos indexó.
- Ejecuta `ingest.py` una sola vez por conjunto de documentos en una base de prueba. Si vuelves a cargar los mismos archivos, esta versión agrega sus fragmentos de nuevo.

## Documentos locales

El repositorio es público. Para las pruebas compartidas, usa archivos ficticios. Los documentos adicionales de `documentos/`, la carpeta `documentos_reales/` y las bases SQLite locales se excluyen de Git. El script lee `documentos/` y la guía incluida sigue versionada.

## Hoja de ruta

- Detectar documentos que ya se cargaron.
- Buscar por similitud en español y mostrar los tres fragmentos más pertinentes con su archivo de origen.
- Incorporar una interfaz, exportar a Obsidian y empaquetar la aplicación para Windows.
