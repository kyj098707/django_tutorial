FROM python:3.10.7

WORKDIR /home/

RUN git clone https://github.com/kyj098707/django_tutorial.git

WORKDIR /home/django_tutorial/

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput && python manage.py migrate --settings=pinterest_project.settings.deploy && gunicorn pinterest_project.wsgi --env DJANGO_SETTINGS_MODULE=pinterest_project.settings.deploy --bind 0.0.0.0:8000"]
