web: gunicorn config.wsgi --log-file -
release: python manage.py migrate
worker: celery -A config worker -B -l INFO