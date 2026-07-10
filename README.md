# MiblogFinal

MiblogFinal es una aplicacion web tipo blog desarrollada con Django para la entrega final del curso. Permite registrar usuarios, iniciar sesion, gestionar perfiles, administrar autores y etiquetas, y publicar entradas de blog con formularios validados.

## Funcionalidades

- Panel administrativo de Django en `/admin/`.
- Registro, login y logout de usuarios.
- Perfil de usuario con edicion de datos basicos, biografia y avatar.
- Administracion de autores y etiquetas desde Django Admin.
- Busqueda de autores por nombre.
- Listado y detalle de entradas publicadas.
- Creacion, edicion y eliminacion de entradas.
- Permisos para que solo el autor o un administrador edite o elimine una entrada.
- Paginas estaticas de acerca de y contacto.
- Context processor para mostrar el nombre del sitio.
- Template tags/filtros personalizados para formato de fecha.
- Manejo de archivos estaticos y media.
- Preparacion basica para deploy con WhiteNoise, Gunicorn y Procfile.

## Requisitos

- Python 3.13 o superior.
- pip.
- Entorno virtual recomendado.

## Instalacion local

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

Luego abre:

```text
http://127.0.0.1:8000/
```

## Archivos estaticos y media

Para preparar archivos estaticos en un entorno de despliegue:

```bash
python manage.py collectstatic
```

Las imagenes subidas por usuarios se guardan en `media/`.

## Despliegue o URL publica

El proyecto esta preparado para documentar una URL publica usando PythonAnywhere, Render, Railway, Ngrok o Render.

Para Render se incluye:

- `Procfile`
- `gunicorn`
- `whitenoise`
- `docs/deploy.md`

Para una demostracion temporal con Ngrok:

```bash
python manage.py runserver
ngrok http 8000
```

Despues se copia la URL generada por Ngrok y se coloca en la presentacion de Google Slides.

## Entrega

La entrega final debe hacerse con una presentacion de Google Slides que incluya:

- Enlace publico al repositorio de GitHub.
- Descripcion del proyecto.
- Funcionalidades principales.
- Capturas de pantalla del admin, registro, login, perfil, listado, detalle y formularios.
- Instrucciones resumidas de ejecucion local.
- URL publica real o simulacion documentada del despliegue.
