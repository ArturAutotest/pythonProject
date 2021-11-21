from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Find_element_click(BasePage):

    def proffesional_investor_button(self):
        search_field = self.driver.find_element(By.XPATH, "//p[contains(text(),'Professional investor')]")
        search_field.click()
    
    def confirm_button(self):
        search_field = self.driver.find_element(By.XPATH, "//span[contains(text(),'Continue')]")
        search_field.click()
        time.sleep(1)

    @allure.feature('Click on Individual_investor button')
    def individual_investor_button(self):
        search_field = self.driver.find_element(By.XPATH, "//p[contains(text(),'Company')]")
        search_field.click()
        with allure.step('Делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        time.sleep(2)

    @allure.feature('Click on sign in button')
    def sign_in_button(self):
        search_field = self.driver.find_element(By.XPATH, "//span[contains(text(),'Sign in')]")
        search_field.click()
        with allure.step('Делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        time.sleep(2)

    def log_in_button(self):
        search_field = self.driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]")
        search_field.click()
        time.sleep(1)
    
    def email_field(self):
        search_box = self.driver.find_element(By.XPATH, "//input[@name='email']")
        search_box.send_keys("a.korotkiy@ive.one")
        time.sleep(1)
    
    def password_field(self):
        search_box = self.driver.find_element(By.XPATH, "//input[@name='password']")
        search_box.send_keys("Qbug.151?200")
        time.sleep(1)

    def waited_func_2(self):
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.XPATH, "//p[contains(text(),'Professional investor')]")
        search_box.click()
    
    def continue_button_1(self):
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.XPATH, "//span[contains(text(),'Continue')]")
        search_box.click()

    def company_button(self):
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.XPATH, "//p[contains(text(),'Company')]")
        search_box.click()
        
    def invest_vogeman_green_ship(self):
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.XPATH, "//p[contains(text(),'Vogemann Green Ship')]/..//..//span[text()='Invest']")
        search_box.click()
        

    def ok_button(self):
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.XPATH, "//span[contains(text(),'OK')]")
        search_box.click()
    
    def switch_page_2(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
    
    def next_button(self):
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
        search_box.click()
    
    def purchase_order_button(self):
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.XPATH, "//span[contains(text(),'Purchase order')]")
        search_box.click()

    def purchase_order_confirmations(self):
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.XPATH, "//label[@for='checkbox-document-item-0']//div")
        search_box.click()
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.XPATH, "//label[@for='checkbox-document-item-1']//div")
        search_box.click()
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.XPATH, "//label[@for='checkbox-document-item-2']//div")
        search_box.click()
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.XPATH, "//label[@for='checkbox-document-item-3']//div")
        search_box.click()
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.XPATH, "//label[@for='checkbox-document-item-4']//div")
        search_box.click()