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

class Public_Edit_User:

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

        self.my_page_url = self.basic_func.get_my_page_url()

    def go_to_my_page( self ):
        self.chrome.get( self.my_page_url )

    def go_to_edit_page( self ):
        edit_btn_xpath = self.public_parts_xpath['edit_btn_xpath']
        edit_btn_elem = self.driver_func.get_element_by_xpath( edit_btn_xpath )
        self.driver_func.click_item( edit_btn_elem )

    def edit_user_info( self ):

        first_name_elem = self.driver_func.get_element_by_name( 'first_name' )
        last_name_elem = self.driver_func.get_element_by_name( 'last_name' )
        user_email_elem = self.driver_func.get_element_by_name( 'user_email' )
        submit_elem = self.driver_func.get_element_by_id( 'submit' )
        
        self.driver_func.clear_item_info( first_name_elem )
        self.driver_func.put_item_info( first_name_elem, 'edit_first_name_test' )

        self.driver_func.clear_item_info( last_name_elem )
        self.driver_func.put_item_info( last_name_elem, 'edit_last_name_test' )

        self.driver_func.click_item( submit_elem )




