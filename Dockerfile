FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/kyj098707/django_tutorial.git

WORKDIR /home/django_tutorial/

RUN pip install -r requirements.txt

RUN echo { "SECRET_KEY": "django-insecure-z*q$#la+z_+!t($td3@wej6%paxe##!zfz+xnrqjw9@bh)vk4j" } > secrets.json

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
