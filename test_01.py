from PageObject import Find_element_click
import time



def test_entering_and_login(browser):
    ive_one_main_page = Find_element_click(browser)
    ive_one_main_page.go_to_site()
    ive_one_main_page.proffesional_investor_button()
    ive_one_main_page.confirm_button()
    ive_one_main_page.individual_investor_button()
    ive_one_main_page.confirm_button()
    ive_one_main_page.sign_in_button()
    ive_one_main_page.log_in_button()
    ive_one_main_page.email_field()
    ive_one_main_page.password_field()
    ive_one_main_page.log_in_button()
    time.sleep(7)

def test_vogeman_investing(browser):
    investmentHub = Find_element_click(browser)
    investmentHub.go_to_site()
    # def test_ive_one(browser):
    # ive_one_main_page = Find_element_click(browser)
    # ive_one_main_page.go_to_site()
    # ive_one_main_page.proffesional_investor_button()
    # ive_one_main_page.confirm_button()
    # ive_one_main_page.individual_investor_button()
    # ive_one_main_page.confirm_button()