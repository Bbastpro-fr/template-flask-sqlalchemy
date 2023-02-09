FROM alpine:3.17.1
RUN apk add --no-cache python3 py3-pip
COPY src /app
RUN pip install -r /app/requirements.txt
WORKDIR /app
CMD ["python3", "app.py"]