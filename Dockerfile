FROM python:3.10.5-alpine3.16
RUN apk add --no-cache sqlite
WORKDIR /opt/app
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:3000"]
