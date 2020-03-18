from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from plugins.driver.DriverAction import Driver_Action

class Admin_Login:

    def __init__(self, driver, target_url):

        self.chrome = driver
        self.target_url = target_url
        self.driver_func = Driver_Action( driver )

    def login_to_admin(self):

        self.chrome.get(self.target_url+'wp-login.php')


        target_element = ['log', 'pwd', 'rememberme']

        strings = ['test', 'test', '']

        for element, string in zip( target_element, strings ) :

            target_box = self.chrome.find_element_by_name(element)

            if element == 'rememberme':
                target_box.click()
            else:
                self.driver_func.clear_item_info( target_box )
                target_box.send_keys(string)

        target_box.submit()

    #無事ログインできたかチェックする
    def is_login_page( self ):

        self.driver_func.stop(2)
        current_url = self.chrome.current_url
        if( 'wp-login.php' in current_url ):
            self.login_to_admin()
        elif( 'wp-admin' in current_url  ):
            pass
        else:
            self.is_login_page()











