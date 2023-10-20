FROM python:3.10

RUN mkdir /code

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

COPY ./app /code/app

ENV APP_PORT=8080

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8080"]