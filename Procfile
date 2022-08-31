release:python manage.py migrate --noinput
release:python manage.py collectstatic --noinput
release:python manage.py makemigrations --noinput
web: gunicorn rest_api_course_three.wsgi