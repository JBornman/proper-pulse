FROM python:3.10.13

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    pip install --upgrade pip

WORKDIR /app

COPY . /app

COPY ./src /app

RUN python -m pip install -r requirements.txt

EXPOSE 5000

CMD [ "python","main.py" ]