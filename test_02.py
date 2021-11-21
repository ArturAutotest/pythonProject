from PageObject import Find_element_click
import time

def test_waiting(browser):
    ive_one_main_page = Find_element_click(browser)
    ive_one_main_page.go_to_site()
    ive_one_main_page.waited_func_2()
    ive_one_main_page.continue_button_1()
    ive_one_main_page.company_button()
    ive_one_main_page.continue_button_1()
    ive_one_main_page.ok_button()
    ive_one_main_page.invest_vogeman_green_ship()
    ive_one_main_page.log_in_button()
    ive_one_main_page.email_field()
    ive_one_main_page.password_field()
    ive_one_main_page.log_in_button()
    ive_one_main_page.invest_vogeman_green_ship()
    ive_one_main_page.switch_page_2()
    ive_one_main_page.next_button()
    time.sleep(1)
    ive_one_main_page.next_button()
    
    ive_one_main_page.purchase_order_confirmations()
    
    ive_one_main_page.purchase_order_button()
    time.sleep(5)
