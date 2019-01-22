FROM python:3.6-alpine
MAINTAINER Maxim Zhovanik
WORKDIR /service/GET-POST
COPY . /service/GET-POST
RUN pip install -r requirements.txt
CMD ["python", "/service/GET-POST/app/app.py"]
