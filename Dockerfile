FROM python:3.9-alpine

# Dependencies 
COPY requirements.txt /opt/steam-exporter/requirements.txt
RUN pip install -r /opt/steam-exporter/requirements.txt

# SOURCE
COPY ./server.py /opt/steam-exporter/server.py


ENV STEAM_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENV STEAM_USER=ZZZZZZZZZZZZZZZZZ
ENV STEAM_SLEEP=300
ENV STEAM_PORT=8000

EXPOSE 8000

ENTRYPOINT ["python", "/opt/steam-exporter/server.py"]
