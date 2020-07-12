FROM python:3.6.7-slim

RUN pip3 install --upgrade pip

RUN apt-get update && apt-get install -y cron vim

#add project files to the usr/src/code folder
COPY . /usr/src/code

RUN pip3 install --no-cache-dir -r /usr/src/code/requirements.txt

#set directoty where CMD will execute
WORKDIR /usr/src/code

# Expose ports
EXPOSE 8000

# default command to execute
CMD python manage.py makemigrations && python manage.py migrate && python manage.py crontab add && python manage.py runserver 0.0.0.0:8000
