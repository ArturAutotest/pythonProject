from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://investment.test.ive.one/"

    def go_to_site(self):
        return self.driver.get(self.base_url)