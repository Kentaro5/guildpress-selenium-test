from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from plugins.singlepage.InitSettings import Init_Settings
import time
import datetime

class Pay_Pal_Create_Page:

    def __init__(self, driver):
        self.chrome = driver

    #paypalのショートコード取得
    def get_new_pay_pal_short_code( self ):

        short_xpath = '//tbody[@id="the-list"]/tr[1]/td[@class="shortcode column-shortcode"]'
        short_code = self.chrome.find_element_by_xpath(short_xpath).text

        return short_code

    def create_normal_subscription_page( self, short_code ):

        dt_now = datetime.datetime.now()

        #インスタンス作成
        init_settings = Init_Settings( self.chrome )

        init_settings.create_new_guild_press_shortcode_page( 'PayPalTestPage'+str( dt_now.microsecond ), short_code )

        register_page_check_box = self.chrome.find_element_by_name( 'guild_press_register_page_check' )
        register_page_check_box.click()


    def create_member_subscription_page( self, short_code ):

        dt_now = datetime.datetime.now()

        #インスタンス作成
        init_settings = Init_Settings( self.chrome )

        init_settings.create_new_guild_press_shortcode_page( 'PayPalゴールド会員Page'+str( dt_now.microsecond ), short_code )

        register_page_check_box = self.chrome.find_element_by_name( 'guild_press_register_page_check' )
        register_page_check_box.click()


        









