FROM python:3.6-alpine
MAINTAINER Viacheslav Kryvous
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["postservice.py"]