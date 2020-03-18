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

class Admin_Lesson_Lock:

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


    def set_block_page( self ):

        lesson_details = {
            'beginner_lesson_details' : {
                'first_lesson_details' : {
                    'post_title' : '英語文法(初級講座)',
                    'page_lock' : '1',
                },
                'second_lesson_details' : {
                    'post_title' : '英語リスニング(初級講座)',
                    'page_lock' : '2',
                },
                'third_lesson_details' : {
                    'post_title' : '英語リーディング(初級講座)',
                    'page_lock' : '2',
                },
                'fourth_lesson_details' : {
                    'post_title' : '英語スピーキング(初級講座)',
                    'page_lock' : '2',
                },
                'fifth_lesson_details' : {
                    'post_title' : '英語単語(初級講座)',
                    'page_lock' : '2',
                }
            },
            'normal_lesson_details' : {
                'first_lesson_details' : {
                    'post_title' : '英語文法(中級講座)',
                    'page_lock' : '1',
                },
                'second_lesson_details' : {
                    'post_title' : '英語リスニング(中級講座)',
                    'page_lock' : '1',
                },
                'third_lesson_details' : {
                    'post_title' : '英語リーディング(中級講座)',
                    'page_lock' : '2',
                },
                'fourth_lesson_details' : {
                    'post_title' : '英語スピーキング(中級講座)',
                    'page_lock' : '2',
                },
                'fifth_lesson_details' : {
                    'post_title' : '英語単語(中級講座)',
                    'page_lock' : '1',
                }
            },
            'advanced_lesson_details' : {
                'first_lesson_details' : {
                    'post_title' : '英語文法(上級講座)',
                    'page_lock' : '1',
                },
                'second_lesson_details' : {
                    'post_title' : '英語リスニング(上級講座)',
                    'page_lock' : '2',
                },
                'third_lesson_details' : {
                    'post_title' : '英語リーディング(上級講座)',
                    'page_lock' : '1',
                },
                'fourth_lesson_details' : {
                    'post_title' : '英語スピーキング(上級講座)',
                    'page_lock' : '1',
                },
                'fifth_lesson_details' : {
                    'post_title' : '英語単語(上級講座)',
                    'page_lock' : '1',
                }
            }
        }

        lesson_details_test = {
            'beginner_lesson_details' : {
                'second_lesson_details' : {
                    'post_title' : '英語リスニング(初級講座)',
                    'page_lock' : '2',
                }
            }
        }

        page_list_xpath = self.admin_parts_xpath['page_list_xpath']
        page_list_elem = self.driver_func.get_elements_by_xpath( page_list_xpath )

        for details_item_name, details_item_value in lesson_details.items():
            for list_name,lesson_details_lists in details_item_value.items():
                self.add_info( lesson_details_lists )

    def add_info( self, lesson_details_lists ):

        page_list_xpath = self.admin_parts_xpath['page_list_xpath']
        page_list_elem = self.driver_func.get_elements_by_xpath( page_list_xpath )
        page_lock_radio_xpath = self.admin_parts_xpath['page_lock_radio_xpath']
        current_page_btn_xpath = self.admin_parts_xpath['current_page_btn_xpath']
        update_post_btn_xpath = self.admin_parts_xpath['update_post_btn']

        target_text = lesson_details_lists['post_title']

        target_elem = self.basic_func.get_target_element( page_list_elem, target_text )
        self.driver_func.click_item( target_elem )


        if( lesson_details_lists['page_lock'] == '2' ):
            self.driver_func.scroll_down( self.chrome )
            guild_press_lock_page_elem = self.driver_func.get_element_by_xpath( page_lock_radio_xpath )
            self.driver_func.click_item( guild_press_lock_page_elem )

        self.driver_func.scroll_top( self.chrome )

        update_post_btn_elem = self.driver_func.get_element_by_xpath( update_post_btn_xpath )
        self.driver_func.click_item( update_post_btn_elem )

        self.driver_func.stop( 1 )

        #投稿リストを表示する
        current_page_btn_elem = self.driver_func.get_element_by_xpath( current_page_btn_xpath )
        self.driver_func.click_item( current_page_btn_elem )










