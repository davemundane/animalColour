FROM python:3.6-alpine

RUN pip install slackclient

RUN mkdir /app

WORKDIR /app

COPY animalColour.py .

CMD ["python", "animalColour.py"]