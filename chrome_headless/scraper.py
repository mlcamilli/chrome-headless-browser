from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class ChromeScraper(object):

    def __init__(self, proxy=None):
        self.service_args = []
        if proxy:
            self.service_args.append('--proxy={}'.format(proxy))
            # Can be http or socks5
            self.service_args.append('--proxy-type=http')
        self.desired = dict(DesiredCapabilities.PHANTOMJS)
        self.desired["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
            "(KHTML, like Gecko) Chrome/15.0.87"
        )
        self.initialize()

    def initialize(self):
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.browser = webdriver.Chrome(desired_capabilities=self.desired)

    def quit(self):
        self.browser.quit()
        self.display.stop()

    @property
    def html(self):
        return self.browser.page_source.encode('utf-8')

    def get(self, url):
        self.browser.get(url)

    def get_frame(self, selector):
        self.browser.switch_to.frame(selector)

    def by_id(self, selector):
        return self.browser.find_element_by_id(selector)

    def by_css(self, selector, multiple=False):
        if multiple:
            return self.browser.find_elements_by_css_selector(selector)
        else:
            return self.browser.find_element_by_css_selector(selector)

    def select_dropdown_option(self, element, value):
        select = Select(element)
        select.select_by_value(value)

    def __enter__(self):
        self.initialize()
        return self

    def __exit__(self, type, value, traceback):
        self.quit()
