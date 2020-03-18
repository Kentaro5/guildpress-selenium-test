from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from plugins.driver.DriverAction import Driver_Action
import time
import datetime



class Test_User_Normal_Register:

    def __init__(self, driver):
        self.chrome = driver
        self.driver_func = Driver_Action( driver )

    #普通に登録
    def nomarl_put_user_info_to_form( self ):


        dt_now = datetime.datetime.now()

        register_btn_path = '//input[@class="btn_design"][@value = "登録"]'

        last_name_input = self.driver_func.get_element_by_name('last_name')
        self.driver_func.clear_item_info( last_name_input )
        self.driver_func.put_item_info( last_name_input, 'test' )

        first_name_input = self.driver_func.get_element_by_name('first_name')
        self.driver_func.clear_item_info( first_name_input )
        self.driver_func.put_item_info( first_name_input, 'test' )

        user_name_input = self.driver_func.get_element_by_name('log')
        self.driver_func.clear_item_info( user_name_input )
        self.driver_func.put_item_info( user_name_input, 'test'+str( dt_now.microsecond ) )

        user_email_input = self.driver_func.get_element_by_name('user_email')
        self.driver_func.clear_item_info( user_email_input )
        self.driver_func.put_item_info( user_email_input, 'test'+str( dt_now.microsecond )+'@exaple.com' )

        password_input = self.driver_func.get_element_by_name('password')
        self.driver_func.clear_item_info( password_input )
        self.driver_func.put_item_info( password_input, 'passwordを記載' )

        register_btn = self.driver_func.get_element_by_xpath(register_btn_path)
        register_btn.submit()

    # ブラウザーを閉じる
    def quit_browser(self):
        self.chrome.quit()










