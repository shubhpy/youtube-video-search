FROM python:3.6.7-slim

RUN pip3 install --upgrade setuptools && \
	apt-get update && \
	apt-get install -y libpq-dev build-essential cron procps zip vim wget

#add project files to the usr/src/code folder
COPY . /usr/src/code

RUN pip3 install --no-cache-dir -r /usr/src/code/requirements.txt

#set directoty where CMD will execute
WORKDIR /usr/src/code

# Expose ports
EXPOSE 8000

RUN python manage.py crontab add

# default command to execute
CMD python manage.py runserver