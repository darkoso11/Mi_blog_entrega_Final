# Checklist de entrega

Usa esta lista antes de compartir la presentacion final.

## Proyecto

- [x] Proyecto Django llamado `MiblogFinal`.
- [x] Aplicacion tipo blog con modelos `Author`, `Tag` y `Post`.
- [x] Registro, login, logout y perfil de usuario.
- [x] Creacion, edicion, detalle, listado y eliminacion de entradas.
- [x] Entradas con autor, etiquetas, imagen y estado publicado.
- [x] Busqueda de autores.
- [x] Panel admin configurado.
- [x] Templates, herencia de `base.html`, CSS y paginas informativas.
- [x] Validaciones basicas en formularios.
- [x] Tests para blog y cuentas.

## Repositorio

- [x] `README.md` con instalacion, uso, deploy y entrega.
- [x] `requirements.txt` actualizado.
- [x] `Procfile` para despliegue con Gunicorn.
- [x] `.gitignore` excluye `.venv`, `db.sqlite3`, `media`, `staticfiles` y cache.
- [x] Sin screenshots ni archivos temporales versionados.

## Antes de subir a GitHub

```bash
python manage.py test
python manage.py check
python manage.py collectstatic --noinput
git status
git add .
git commit -m "Preparar entrega final"
git branch -M main
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
```

## Presentacion de Google Slides

- [ ] Portada con nombre del proyecto.
- [ ] URL del repositorio publico.
- [ ] URL publica de la app o evidencia de Ngrok.
- [ ] Resumen de funcionalidades.
- [ ] Evidencia visual del uso: registro, login, perfil, posts, autores, etiquetas y admin.
- [ ] Instrucciones resumidas para ejecutar localmente.
