FROM python:3.6-alpine
MAINTAINER Maxim Zhovanik
WORKDIR /service/POST-SERV
COPY . /service/POST-SERV
RUN pip install -r requirements.txt
CMD ["python", "/service/POST-SERV/app/app.py"]
