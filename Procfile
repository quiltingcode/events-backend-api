release: python manage.py makemigrations && python manage.py migrate
web: gunicorn events_api.wsgi