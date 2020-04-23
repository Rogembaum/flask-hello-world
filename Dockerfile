FROM python:latest
RUN apt-get update && pip3 install flask && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY cmd.sh /
CMD ["/cmd.sh"]