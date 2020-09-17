web: gunicorn hooslistening.wsgi
release:
    python manage.py makemigrations
    python manage.py migrate --run-syncdb