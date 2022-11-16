FROM python:alpine3.16

COPY ./main.py /app/

WORKDIR /app/

ENV nth=-h

ENTRYPOINT "python" "main.py" $nth