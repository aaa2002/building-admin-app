FROM python:alpine3.19

WORKDIR /server
COPY . .
RUN pip install -r /server/requirenments.txt 

EXPOSE 8000

RUN python /server/manage.py migrate \
    && python /server/manage.py createsuperuser --email someemail@provider.com --noinput

CMD [ "python3",  "/server/manage.py", "runserver", "0.0.0.0:8000" ]
# CMD ["/bin/sh"]


