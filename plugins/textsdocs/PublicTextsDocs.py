from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.support.ui import Select
from plugins.driver.DriverAction import Driver_Action
from plugins.xpath.AdminMenuPath import Admin_Menu_Path
from plugins.basic.basic import Basic
import time
import datetime

class Public_Texts_Docs:

    def __init__(self, driver):

        self.chrome = driver
        self.driver_func = Driver_Action( driver )
        self.admin_xpath_list_func = Admin_Menu_Path()
        self.basic_func = Basic()
        # 管理画面のメニューのパスを返す
        self.admin_xpath_lists_xpath = self.admin_xpath_list_func.get_admin_menu_xpath()

        # 管理画面メニュー内の新規追加や編集などのパーツのパスを返す。
        self.admin_list_parts_xpath = self.admin_xpath_list_func.get_admin_menu_list_parts_xpath()

        # 管理画面内の項目に関するパス(作成した固定ページリストとか)
        self.admin_parts_xpath = self.admin_xpath_list_func.get_admin_parts()

        #ユーザー画面内の項目に関するパス
        self.public_parts_xpath = self.admin_xpath_list_func.get_public_parts()

        self.base_dir = self.basic_func.get_base_dir_path()


    def go_to_texts_list_page( self ):
        self.driver_func.go_to_public_nav_menu( '教材一覧ページ' )

    def check_texts_docs_page( self ):
        self.driver_func.scroll_down( self.chrome )

        text_xpath = '//div[@class="col-xs-12 col-md-12"]/div[@class="dwd_background mb24"][11]/a'

        text_elem = self.driver_func.get_element_by_xpath( text_xpath )
        self.driver_func.click_item( text_elem )

        self.driver_func.stop(3)








