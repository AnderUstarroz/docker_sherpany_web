FROM python:3.7.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /web
WORKDIR /web
COPY sherpany_events/. /web/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uwsgi", "--ini-paste", "sherpany_events/uwsgi.ini"]