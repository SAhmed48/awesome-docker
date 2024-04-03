FROM python:3.8

LABEL maintainer="salmanahmed4858@gmail.com"

RUN apt update

COPY . /flask-app

WORKDIR /flask-app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["main.py"]
