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

class Public_Calendar:

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

        self.calendar_page_url = self.basic_func.get_calendar_page_url()

    def go_to_calendar_page( self ):

        self.driver_func.move_to_page_by_link( self.chrome, self.calendar_page_url )


    def click_calendar( self, target_calendar_name ):
        calendar_cell_xpath = self.public_parts_xpath['calendar_cell_list_xpath']
        calendar_cells = self.driver_func.get_elements_by_xpath( calendar_cell_xpath )

        calendar_cell_elem = self.basic_func.get_target_element( calendar_cells, target_calendar_name )
        self.driver_func.click_item( calendar_cell_elem )


    def go_to_calendar_register_page( self ):
        calendar_register_xpath = self.public_parts_xpath['calendar_cell_register_xpath']
        calendar_register_elem = self.driver_func.get_element_by_xpath( calendar_register_xpath )
        self.driver_func.click_item( calendar_register_elem )


    def put_calendar_register_info( self ):

        date_time1_elem = self.driver_func.get_element_by_name( 'date_time1' )
        date_time2_elem = self.driver_func.get_element_by_name( 'date_time2' )
        comment_elem = self.driver_func.get_element_by_name( 'comment' )
        submit_btn_elem = self.driver_func.get_element_by_id( 'submit' )

        self.driver_func.put_item_info( date_time1_elem, '13:00' )
        self.driver_func.put_item_info( date_time2_elem, '16:00' )
        self.driver_func.put_item_info( comment_elem, 'かれんだーてすと' )

        self.driver_func.click_item( submit_btn_elem )


    def go_to_calendar_edit_page( self ):
        calendar_edit_xpath = self.public_parts_xpath['calendar_cell_edit_xpath']
        calendar_edit_elem = self.driver_func.get_element_by_xpath( calendar_edit_xpath )
        self.driver_func.click_item( calendar_edit_elem )


    def put_calendar_edit_info( self ):

        date_time1_elem = self.driver_func.get_element_by_name( 'date_time1' )
        date_time2_elem = self.driver_func.get_element_by_name( 'date_time2' )
        comment_elem = self.driver_func.get_element_by_name( 'comment' )
        submit_btn_elem = self.driver_func.get_element_by_id( 'submit' )

        self.driver_func.clear_item_info( date_time1_elem )
        self.driver_func.put_item_info( date_time1_elem, '13:00' )

        self.driver_func.clear_item_info( date_time2_elem )
        self.driver_func.put_item_info( date_time2_elem, '16:00' )

        self.driver_func.clear_item_info( comment_elem )
        self.driver_func.put_item_info( comment_elem, 'かれんだーてすと' )

        self.driver_func.click_item( submit_btn_elem )









