FROM python:3.10

WORKDIR /MiniMarket
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=MiniMarket.settings