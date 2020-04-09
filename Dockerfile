FROM python:latest

RUN pip3 install flask
WORKDIR /app
COPY cmd.sh /
CMD ["/cmd.sh"]