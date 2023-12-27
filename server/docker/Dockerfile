FROM python:alpine3.19

WORKDIR /server
COPY . .
RUN pip install -r /server/requirenments.txt 
CMD [ "python3",  "/server/manage.py", "runserver" ]


