FROM python:3.9-slim-buster

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip \
&& pip install --user -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]