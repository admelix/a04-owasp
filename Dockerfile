FROM python:latest

RUN apt update 
    

WORKDIR /api

COPY . /api/

RUN pip install flask

EXPOSE 8000

CMD [ "python", "app.py" ]
