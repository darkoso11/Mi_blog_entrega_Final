# Simulación de despliegue en Render

Este documento describe una simulación reproducible del despliegue de Blog. No representa una URL activa permanente, pero deja preparados los archivos y valores que Render necesita.

Para una demostración temporal también puede utilizarse Ngrok con `ngrok http 8000`.

## 1. Subir el proyecto a GitHub

```bash
git clone https://github.com/darkoso11/Mi_blog_entrega_Final.git
cd Mi_blog_entrega_Final
```

## 2. Dependencias

El proyecto incluye `gunicorn` y `whitenoise` en `requirements.txt`.

## 3. Configuracion importante

En `settings.py` ya están definidos:

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

También se incluye WhiteNoise en `MIDDLEWARE` para servir archivos estáticos. La clave secreta, el modo debug y los hosts se leen de variables de entorno.

Variables recomendadas en Render:

```text
DJANGO_SECRET_KEY=<una clave larga y aleatoria>
DJANGO_DEBUG=False
```

Render proporciona `RENDER_EXTERNAL_HOSTNAME` automáticamente y el proyecto lo agrega a `ALLOWED_HOSTS`.

## 4. Render

Crear un nuevo Web Service en Render conectado al repositorio.

Build Command:

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

Start Command:

```bash
gunicorn MiblogFinal.wsgi:application
```

Después del primer despliegue se crea el usuario administrador desde la consola del servicio:

```bash
python manage.py createsuperuser
```

## 5. Resultado esperado

Render generará una URL parecida a:

```text
https://miblogfinal.onrender.com
```

La URL generada debe colocarse en la presentación junto con el enlace del repositorio público.

## 6. Archivos media

WhiteNoise sirve archivos estáticos, pero no conserva las imágenes subidas por usuarios. En un despliegue permanente se debe conectar almacenamiento persistente, como Cloudinary o un servicio compatible con S3. Para la demostración local o mediante Ngrok, `MEDIA_ROOT` es suficiente.
