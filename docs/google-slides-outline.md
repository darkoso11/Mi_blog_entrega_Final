# Guion para Google Slides

La entrega se realiza con una presentacion de Google Slides que funcione como README visual del proyecto.

## 1. Portada

- Proyecto: MiblogFinal.
- Curso: Proyecto final Django.
- Autor: Oswaldo.

## 2. Descripcion

MiblogFinal es una aplicacion web tipo blog creada con Django. Permite crear usuarios, administrar perfiles, publicar entradas, asignar autores, agregar etiquetas y consultar autores.

## 3. Repositorio

- Colocar la URL publica del repositorio de GitHub.
- Mencionar que incluye `README.md`, `requirements.txt`, `Procfile` y documentacion de deploy.

## 4. Tecnologias

- Python.
- Django.
- SQLite para desarrollo local.
- HTML, CSS y templates de Django.
- Gunicorn y WhiteNoise para despliegue.

## 5. Funcionalidades principales

- Registro, login y logout.
- Perfil editable.
- CRUD de entradas.
- Autores y etiquetas.
- Busqueda de autores.
- Panel administrativo.

## 6. Recorrido visual

Agregar evidencia visual de:

- Inicio/listado de entradas.
- Registro o login.
- Perfil.
- Crear entrada.
- Editar entrada.
- Eliminar entrada.
- Busqueda de autores.
- Panel admin.

## 7. Ejecucion local

```bash
git clone URL_DEL_REPOSITORIO
cd Proyecto-final-CoderHouse
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 8. Despliegue o URL publica

Incluir una de estas opciones:

- URL de Render/PythonAnywhere/Railway si queda desplegado.
- URL temporal de Ngrok si se usa tunel local.

## 9. Cierre

Mencionar que el proyecto cumple con la entrega porque tiene repositorio publico, documentacion, dependencias, app funcional y URL publica o simulada.
