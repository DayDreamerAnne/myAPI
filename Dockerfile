FROM python:2.7
LABEL author="anne.zhang"

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt
RUN pip install gunicorn gevent
RUN pip install flask

EXPOSE 80
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
