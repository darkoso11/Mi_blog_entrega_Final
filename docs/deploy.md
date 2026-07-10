# Deploy de MiblogFinal en Render

Esta guia resume una forma simple de obtener una URL publica para el proyecto.

## 1. Subir el proyecto a GitHub

```bash
git add .
git commit -m "Proyecto final Django"
git branch -M main
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
```

## 2. Dependencias

El proyecto incluye `gunicorn` y `whitenoise` en `requirements.txt`.

## 3. Configuracion importante

En `settings.py` ya estan definidos:

```python
ALLOWED_HOSTS = [...]
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Tambien se incluye WhiteNoise en `MIDDLEWARE` para servir archivos estaticos.

## 4. Render

Crear un nuevo Web Service en Render conectado al repositorio.

Build Command:

```bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
```

Start Command:

```bash
gunicorn MiblogFinal.wsgi:application
```

## 5. URL final

Render generara una URL parecida a:

```text
https://miblogfinal.onrender.com
```
