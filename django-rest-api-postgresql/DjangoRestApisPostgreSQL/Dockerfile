FROM python:3.7

WORKDIR /app

ADD requeriments.txt /app

RUN pip install -r requeriments.txt

ADD . /app

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
