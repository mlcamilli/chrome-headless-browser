FROM orchardup/python:2.7
RUN apt-get update --fix-missing
RUN apt-get install -y chromium-browser python python-pip python-dev git
RUN apt-get install -y unzip wget xvfb
RUN wget http://chromedriver.storage.googleapis.com/2.19/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d /usr/bin/
RUN chmod a+x /usr/bin/chromedriver
RUN pip install git+https://github.com/mlcamilli/chrome-headless-browser.git#egg=chrome-headless-browser==0.0.1
