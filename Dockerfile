FROM stackbrew/ubuntu:precise
RUN apt-get update
RUN apt-get install -y chromium-browser python python-pip python-dev
RUN apt-get install -y unzip wget xvfb
RUN wget http://chromedriver.storage.googleapis.com/2.12/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d /usr/bin/
RUN chmod a+x /usr/bin/chromedriver
