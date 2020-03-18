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

class Public_Member_Rank:

    def __init__(self, driver):

        self.chrome = driver
        self.driver_func = Driver_Action( driver )
        self.admin_xpath_list_func = Admin_Menu_Path()
        self.basic_func = Basic()
        # 管理画面のメニューのパスを返す
        self.admin_xpath_lists = self.admin_xpath_list_func.get_admin_menu_xpath()

        # 管理画面メニュー内の新規追加や編集などのパーツのパスを返す。
        self.admin_list_parts_xpath = self.admin_xpath_list_func.get_admin_menu_list_parts_xpath()

        # 管理画面内の項目に関するパス(作成した固定ページリストとか)
        self.admin_parts_xpath = self.admin_xpath_list_func.get_admin_parts()

        #ユーザー画面内の項目に関するパス
        self.public_parts_xpath = self.admin_xpath_list_func.get_public_parts()

        self.base_dir = self.basic_func.get_base_dir_path()

        self.lesson_list_page_url = self.basic_func.get_lesson_list_page()

    def go_to_lesson_list_page( self ):
        self.driver_func.move_to_page_by_link( self.chrome, self.lesson_list_page_url )


    def check_element_page( self ):

        self.go_to_element_lesson_list_page()

        all_lesson_title_list_xpath = self.public_parts_xpath['all_lesson_title_list_xpath']
        lesson_detail_link = self.public_parts_xpath['lesson_detail_lists']

        block_page_list = [
            '英語リスニング(初級講座)',
            '英語スピーキング(初級講座)'
            ]
        for block_page_text in block_page_list:
            lesson_detail_elem = self.driver_func.get_elements_by_xpath( lesson_detail_link )
            all_lesson_title_lists_elem = self.driver_func.get_elements_by_xpath( all_lesson_title_list_xpath )

            lesson_detail_page_link = self.basic_func.get_target_link_element( all_lesson_title_lists_elem, lesson_detail_elem, block_page_text )

            self.driver_func.click_item( lesson_detail_page_link )

            self.driver_func.stop(2)

            self.go_to_lesson_list_page()
            self.go_to_element_lesson_list_page()

    def check_is_user_get_ranked(self):

        try:
            pay_pal_btn_xpath = '//button[@id="paypal_btn"]'
            pay_pal_btn = self.driver_func.get_element_by_xpath(pay_pal_btn_xpath)

        except NoSuchElementException:
            #特に問題ない場合はtrueを返す。
            return True
        else:
            #ボタンが存在する場合は、ユーザーが会員楽を取得できていないので、falseを返してもう一度処理させる。
            return False

    def go_to_element_lesson_list_page( self ):
        all_lesson_list = self.public_parts_xpath['all_lesson_list_xpath']
        all_lesson_list_link = self.public_parts_xpath['all_lesson_list_link_xpath']
        all_lesson_lists_elem = self.driver_func.get_elements_by_xpath( all_lesson_list )
        all_lesson_lists_link_elem = self.driver_func.get_elements_by_xpath( all_lesson_list_link )

        #概要ページから該当する名前順にリンクの要素を取得
        link_elem = self.basic_func.get_target_link_element( all_lesson_lists_elem, all_lesson_lists_link_elem, '英語初級講座' )

        #リンクを取得
        lesson_detail_link = self.driver_func.get_link( link_elem )

        #リンクに飛ぶ
        self.driver_func.move_to_page_by_link( self.chrome, lesson_detail_link )

    def check_advanced_page( self ):

        self.go_to_advanced_lesson_list_page()

        all_lesson_title_list_xpath = self.public_parts_xpath['all_lesson_title_list_xpath']
        lesson_detail_link = self.public_parts_xpath['lesson_detail_lists']

        block_page_list = [
            '英語リスニング(上級講座)',
            '英語スピーキング(上級講座)'
            ]
        for block_page_text in block_page_list:

            lesson_detail_elem = self.driver_func.get_elements_by_xpath( lesson_detail_link )
            all_lesson_title_lists_elem = self.driver_func.get_elements_by_xpath( all_lesson_title_list_xpath )

            lesson_detail_page_link = self.basic_func.get_target_link_element( all_lesson_title_lists_elem, lesson_detail_elem, block_page_text )

            self.driver_func.click_item( lesson_detail_page_link )

            self.driver_func.stop(2)

            self.go_to_lesson_list_page()
            self.go_to_advanced_lesson_list_page()


    def go_to_advanced_lesson_list_page( self ):
        all_lesson_list = self.public_parts_xpath['all_lesson_list_xpath']
        all_lesson_list_link = self.public_parts_xpath['all_lesson_list_link_xpath']
        all_lesson_lists_elem = self.driver_func.get_elements_by_xpath( all_lesson_list )
        all_lesson_lists_link_elem = self.driver_func.get_elements_by_xpath( all_lesson_list_link )
        #概要ページから該当する名前順にリンクの要素を取得
        link_elem = self.basic_func.get_target_link_element( all_lesson_lists_elem, all_lesson_lists_link_elem, '英語上級講座' )

        #リンクを取得
        lesson_detail_link = self.driver_func.get_link( link_elem )

        #リンクに飛ぶ
        self.driver_func.move_to_page_by_link( self.chrome, lesson_detail_link )


    def check_lesson_overview_block_page( self ):
        all_lesson_list = self.public_parts_xpath['all_lesson_list_xpath']
        all_lesson_list_link = self.public_parts_xpath['all_lesson_list_link_xpath']

        self.driver_func.stop(2)
        all_lesson_lists_elem = self.driver_func.get_elements_by_xpath( all_lesson_list )
        all_lesson_lists_link_elem = self.driver_func.get_elements_by_xpath( all_lesson_list_link )

        #概要ページから該当する名前順にリンクの要素を取得
        link_elem = self.basic_func.get_target_link_element( all_lesson_lists_elem, all_lesson_lists_link_elem, '英語上級講座' )

        #リンクを取得
        lesson_detail_link = self.driver_func.get_link( link_elem )

        #リンクに飛ぶ
        self.driver_func.move_to_page_by_link( self.chrome, lesson_detail_link )


    def set_user_status_to_gold( self, target_user_name ):
        self.go_to_user_list_page()

        user_list_path = "//form/table[@class='wp-list-table widefat fixed striped users']/tbody[@id='the-list']/tr/td[@class='username column-username has-row-actions column-primary']/strong/a"
        users_lists_path = self.driver_func.get_elements_by_xpath( user_list_path )

        target_user_link = self.basic_func.get_target_element( users_lists_path, target_user_name )

        self.driver_func.click_item(target_user_link);

        self.driver_func.scroll_down(self.chrome)

        self.select_registered_status()

        self.select_gold_rank()

        submit_btn = "//p[@class='submit']/input[@id='submit']"

        submit_btn_elem = self.driver_func.get_element_by_xpath( submit_btn )

        self.driver_func.click_item(submit_btn_elem);

    def go_to_user_list_page( self ):
        admin_user_list_page_path = self.admin_xpath_lists['admin_user_list_page_path']
        admin_user_list_sub_page_path = self.admin_xpath_lists['admin_user_list_sub_page_path']

        # ユーザー一覧ページへ移動
        self.driver_func.move_admin_page( admin_user_list_page_path, admin_user_list_sub_page_path )

    def select_registered_status( self ):
        user_register_status_path = "//div[@id='wpbody-content']/div[@id='profile-page']/form[@id='your-profile']/table[@class='form-table'][6]/tbody/tr[2]/td/select[@id='user_status']";

        user_register_status_element = self.driver_func.get_element_by_xpath( user_register_status_path )
        self.driver_func.select_item_by_text( user_register_status_element, "本登録" )

    def select_gold_rank( self ):
        select_box_rank = "//div[@id='wpcontent']/div[@id='wpbody']/div[@id='wpbody-content']/div[@id='profile-page']/form[@id='your-profile']/table[@class='form-table'][8]/tbody/tr[1]/td/select[@id='gp_user_rank']";

        rank_select_element = self.driver_func.get_element_by_xpath( select_box_rank )
        self.driver_func.select_item_by_text( rank_select_element, "ゴールド会員" )

    def go_to_admin_top_page(self, target_url):
        self.driver_func.move_to_page_by_link( self.chrome, target_url + 'wp-admin/' )










