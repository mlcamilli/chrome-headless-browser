# Chrome Headless Browser

This docker file installs python 2.7 and the necessary libraries and dependencies to use a Chrome Headless Browser. 

To use, inside the docker container bring up the python shell.


```python
>>> from chrome_headless import ChromeScraper
>>> scraper = ChromeScraper()
>>> scraper.get('http://www.google.com')
```
