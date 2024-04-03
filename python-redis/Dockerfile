FROM python:alpine3.10

ADD app.py requirements.txt code/

WORKDIR /code

RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "app.py"]