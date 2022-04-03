FROM python:3.9.7-slim-buster
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/app
CMD [ "python", "app.py", "--host=0.0.0.0", "-p 3020"]