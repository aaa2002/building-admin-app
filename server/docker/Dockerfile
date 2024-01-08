FROM python:alpine3.19

WORKDIR /server
COPY . .
RUN pip install -r /server/requirenments.txt 

ENV DJANGO_SUPERUSER_EMAIL=admin@example.com
ENV DJANGO_SUPERUSER_USERNAME=root
ENV DJANGO_SUPERUSER_PASSWORD=asdfasdf

EXPOSE 8000

RUN python /server/manage.py migrate

RUN python3 manage.py createsuperuser --noinput

CMD [ "python3",  "/server/manage.py", "runserver", "0.0.0.0:8000" ]
# CMD ["/bin/sh"]


