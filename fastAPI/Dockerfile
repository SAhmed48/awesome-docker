FROM python:3.10

RUN pip install --upgrade pip

COPY . /code

WORKDIR /code

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3001