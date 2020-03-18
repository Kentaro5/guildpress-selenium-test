from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from plugins.driver.DriverAction import Driver_Action
import time

class Test_User_Payment_Register:

    def __init__(self, driver):
        self.chrome = driver
        self.driver_func = Driver_Action( driver )

    #GuildPressのページで、PayPal決済ボタンをクリックした後にページが表示されているかチェックする関数
    def is_first_paypal_page_loaded( self ):

        try:
            self.driver_func.stop(10)
            payment_btn_xpath = '//button[@type="submit"]'
            target_click = '//a[text()="ここをクリックしてください"]'
            payment_btn = self.driver_func.get_element_by_xpath(payment_btn_xpath)
        except NoSuchElementException:
            print('no page')
            return self.is_first_paypal_page_loaded()
        else:
            print('page')
            return True

    def is_next_paypal_page_loaded( self ):

        try:
            self.driver_func.stop(10)

            login_email_elem = self.driver_func.get_element_by_name( 'login_email' )
            self.driver_func.clear_item_info( login_email_elem )
            self.driver_func.put_item_info( login_email_elem, 'paypalのメールアドレスを記載' )
        except NoSuchElementException:
            print('no is_next_paypal_page_loaded')
            return self.is_next_paypal_page_loaded()
        else:
            print('is_next_paypal_page_loaded')

            return True

    def is_third_paypal_page_loaded(self):

        try:
            self.driver_func.stop(10)
            login_password_elem = self.driver_func.get_element_by_name( 'login_password' )
            self.driver_func.clear_item_info( login_password_elem )
            self.driver_func.put_item_info( login_password_elem, 'passwordを記載' )

            btnLogin_elem = self.driver_func.get_element_by_name( 'btnLogin' )

        except NoSuchElementException:
            print('no is_third_paypal_page_loaded')
            return self.is_third_paypal_page_loaded()
        else:
            print('is_third_paypal_page_loaded')
            return True


    def is_last_paypal_page_loaded(self):

        try:
            self.driver_func.stop(10)
            confirmButtonTop_elem = self.driver_func.get_element_by_id( 'confirmButtonTop' )

        except NoSuchElementException:
            print('no is_last_paypal_page_loaded')
            return self.is_last_paypal_page_loaded()
        else:
            print('is_last_paypal_page_loaded')
            return True

    def click_new_register_page_pay_pal_btn( self ):

        pay_pal_btn_xpath = '//button[@id="paypal_btn"]'
        pay_pal_btn = self.driver_func.get_element_by_xpath(pay_pal_btn_xpath)
        pay_pal_btn.click()

        is_result = self.is_first_paypal_page_loaded()
        if( is_result == True ):
            self.driver_func.stop(15)
            payment_btn_xpath = '//button[@type="submit"]'
            payment_btn = self.driver_func.get_element_by_xpath(payment_btn_xpath)
            self.driver_func.click_item( payment_btn )

        is_thrid_result = self.is_new_paypal_page_loaded()
        if( is_thrid_result == True ):
            self.driver_func.stop(15)
            btnLogin_elem = self.driver_func.get_element_by_name( 'btnLogin' )
            self.driver_func.click_item( btnLogin_elem )

        is_last_result = self.is_last_paypal_page_loaded()
        if( is_last_result == True ):
            self.driver_func.get_element_by_id( 'confirmButtonTop' ).click()

        self.driver_func.stop(15)

    def is_new_paypal_page_loaded( self ):

        try:
            self.driver_func.stop(10)

            login_email_elem = self.driver_func.get_element_by_name( 'login_email' )
            self.driver_func.clear_item_info( login_email_elem )
            self.driver_func.put_item_info( login_email_elem, 'paypalのメールアドレスを記載' )

            login_password_elem = self.driver_func.get_element_by_name( 'login_password' )
            self.driver_func.clear_item_info( login_password_elem )
            self.driver_func.put_item_info( login_password_elem, 'passwordを記載' )

        except NoSuchElementException:
            print('no is_next_paypal_page_loaded')
            return self.is_next_paypal_page_loaded()
        else:
            print('is_next_paypal_page_loaded')

            return True

    def click_register_page_pay_pal_btn( self ):

        pay_pal_btn_xpath = '//button[@id="paypal_btn"]'
        pay_pal_btn = self.driver_func.get_element_by_xpath(pay_pal_btn_xpath)
        pay_pal_btn.click()

        is_result = self.is_first_paypal_page_loaded()
        if( is_result == True ):
            self.driver_func.stop(15)
            payment_btn_xpath = '//button[@type="submit"]'
            payment_btn = self.driver_func.get_element_by_xpath(payment_btn_xpath)
            self.driver_func.click_item( payment_btn )

        is_next_result = self.is_next_paypal_page_loaded()
        if( is_next_result == True ):
            self.driver_func.stop(15)
            next_payment_btn_xpath = '//button[@type="submit"][text()="次へ"]'
            next_payment_btn = self.driver_func.get_element_by_xpath(next_payment_btn_xpath)
            self.driver_func.click_item( next_payment_btn )

        self.driver_func.stop(15)
        result = self.check_paypal_login_email()

        if( result == True ):
            is_next_result = self.is_next_paypal_page_loaded()
            if( is_next_result == True ):
                next_payment_btn_xpath = '//button[@type="submit"][text()="次へ"]'
                next_payment_btn = self.driver_func.get_element_by_xpath(next_payment_btn_xpath)
                self.driver_func.click_item( next_payment_btn )


        is_thrid_result = self.is_third_paypal_page_loaded()
        if( is_thrid_result == True ):
            self.driver_func.stop(15)
            btnLogin_elem = self.driver_func.get_element_by_name( 'btnLogin' )
            self.driver_func.click_item( btnLogin_elem )

        is_last_result = self.is_last_paypal_page_loaded()
        if( is_last_result == True ):
            self.driver_func.get_element_by_id( 'confirmButtonTop' ).click()

        self.driver_func.stop(15)

    def check_paypal_login_email(self):
        try:
            email_input = self.driver_func.get_element_by_name('login_email')
        except NoSuchElementException:
            return False

        if( email_input.is_displayed() == True ):
            return True
        else :
            return False







