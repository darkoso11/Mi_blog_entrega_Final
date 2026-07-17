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

## Usuario administrador

El repositorio no incluye `db.sqlite3`, por lo que cada evaluador debe crear su propio usuario:

```bash
python manage.py createsuperuser
```

Despues se puede entrar al panel en:

```text
http://127.0.0.1:8000/admin/
```

## Archivos estaticos y media

Para preparar archivos estaticos en un entorno de despliegue:

```bash
python manage.py collectstatic --noinput
```

Las imagenes subidas por usuarios se guardan en `media/`.

## Despliegue o URL publica

El proyecto esta preparado para documentar una URL publica usando Render, PythonAnywhere, Railway o Ngrok.

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

## Repositorio en GitHub

Antes de compartir el enlace:

```bash
git status
python manage.py test
python manage.py check
git add .
git commit -m "Preparar entrega final"
git branch -M main
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
```

El repositorio debe ser publico para que el evaluador pueda revisarlo desde la presentacion.

## Entrega

La entrega final debe hacerse con una presentacion de Google Slides que incluya:

- Enlace publico al repositorio de GitHub.
- Descripcion del proyecto.
- Funcionalidades principales.
- Evidencia visual del admin, registro, login, perfil, listado, detalle y formularios.
- Instrucciones resumidas de ejecucion local.
- URL publica real o simulacion documentada del despliegue.

Tambien se incluye una guia de armado en `docs/google-slides-outline.md` y una lista de verificacion en `docs/entrega-checklist.md`.
