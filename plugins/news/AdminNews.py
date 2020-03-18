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

class Admin_News:

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

    def get_normal_short_code( self, content_elem ):

        #テキストエリアのテキストを改行でリスト方にする。
        content_texts = content_elem.text.splitlines()
        last_index = len(content_texts) - 1

        content_texts[last_index] = content_texts[last_index]+'\n'+'[guild_press_news posts_num="" title=""]'
        return content_texts

    def put_content( self, content_elem, content_texts ):

        for content_text in content_texts:
            self.driver_func.put_item_info( content_elem, content_text+'\n' )

    def add_news_code( self ):
        content_elem = self.driver_func.get_element_by_name( 'content' )
        #テキストエリアのテキストを改行でリスト方にする。
        content_texts = content_elem.text.splitlines()
        last_index = len(content_texts) - 1

        content_texts[last_index] = content_texts[last_index]+'\n'+'[guild_press_news posts_num="" title=""]'
        
        self.driver_func.clear_item_info( content_elem )
        self.put_content( content_elem, content_texts )
        self.submit()

    def submit( self ):
        update_post_btn_xpath = self.admin_parts_xpath['update_post_btn']
        update_post_btn_elem = self.driver_func.get_element_by_xpath( update_post_btn_xpath )

        self.driver_func.click_item( update_post_btn_elem )

    def add_three_news_code( self ):
        content_elem = self.driver_func.get_element_by_name( 'content' )

         #テキストエリアのテキストを改行でリスト方にする。
        content_texts = content_elem.text.splitlines()
        last_index = len(content_texts) - 1

        content_texts[last_index] = content_texts[last_index].replace('posts_num=""', 'posts_num="3"', 1)

        self.driver_func.clear_item_info( content_elem )
        self.put_content( content_elem, content_texts )
        self.submit()

    def add_test_title_news_code( self ):
        content_elem = self.driver_func.get_element_by_name( 'content' )

         #テキストエリアのテキストを改行でリスト方にする。
        content_texts = content_elem.text.splitlines()
        last_index = len(content_texts) - 1

        content_texts[last_index] = content_texts[last_index].replace('title=""', 'title="selnium_test"', 1)

        self.driver_func.clear_item_info( content_elem )
        self.put_content( content_elem, content_texts )
        self.submit()

















