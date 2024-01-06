FROM python:alpine3.19

WORKDIR /server
COPY . .
RUN pip install -r /server/requirenments.txt 

EXPOSE 8000

CMD [ "python3",  "/server/manage.py", "runserver", "0.0.0.0:8000" ]


