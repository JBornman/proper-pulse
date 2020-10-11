FROM python:3.7

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    pip install --upgrade pip

WORKDIR /app

COPY . /app

COPY ./src /app

RUN pip install -r requirements.txt

RUN ls -a

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]