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

class Admin_Calendar:

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

        self.base_dir = self.basic_func.get_base_dir_path()


    def create_public_calendar_page( self ) :

        page_lists = self.driver_func.get_elements_by_xpath( self.admin_parts_xpath['page_list_xpath'] )

        is_page_created = self.basic_func.check_page_is_created( 'カレンダーページ', page_lists )

        return is_page_created

    def go_to_register_calendar_page( self ):
        guild_press_register_calendar_elements = self.driver_func.get_elements_by_xpath( self.admin_parts_xpath['guild_press_tab_xpath'] )

        self.driver_func.click_item( guild_press_register_calendar_elements[1] )

        register = self.driver_func.get_element_by_xpath( self.admin_parts_xpath['guild_press_regsiter_link_xpath'] )

        self.driver_func.click_item( register )

    def go_to_calendar_email_page( self ):

        guild_press_register_calendar_elements = self.driver_func.get_elements_by_xpath( self.admin_parts_xpath['guild_press_tab_xpath'] )

        self.driver_func.click_item( guild_press_register_calendar_elements[2] )


    def put_calendar_info( self ):
        dt_now = datetime.datetime.now()

        calendar_title_element = self.driver_func.get_element_by_name( 'title' )
        self.driver_func.put_item_info( calendar_title_element, 'カレンダー予約'+str(dt_now.microsecond) )

        calendar_max_element = self.driver_func.get_element_by_name( 'max_num' )
        self.driver_func.put_item_info( calendar_max_element, '4' )

        calendar_date_time1_element = self.driver_func.get_element_by_name( 'date_time1' )
        self.driver_func.put_item_info( calendar_date_time1_element, '10:00' )

        calendar_date_time2_element = self.driver_func.get_element_by_name( 'date_time2' )
        self.driver_func.put_item_info( calendar_date_time2_element, '19:00' )

        submit_btn_element = self.driver_func.get_element_by_name( 'submit' )
        self.driver_func.click_item( submit_btn_element )

        return 'カレンダー予約'+str(dt_now.microsecond)

    def put_calendar_email_info( self ):

        self.put_calendar_email_user_info()

        self.put_calendar_email_admin_info()

        submit_btn_element = self.driver_func.get_element_by_name( 'submit' )
        self.driver_func.click_item( submit_btn_element )

    def put_calendar_email_user_info(self):

        guild_press_personal_from_name = self.driver_func.get_element_by_name( 'guild_press_personal_from_name' )
        self.driver_func.clear_item_info( guild_press_personal_from_name )
        self.driver_func.put_item_info( guild_press_personal_from_name, 'ユーザー側カレンダーテスト' )

        guild_press_personal_from_email = self.driver_func.get_element_by_name( 'guild_press_personal_from_email' )
        self.driver_func.clear_item_info( guild_press_personal_from_email )
        self.driver_func.put_item_info( guild_press_personal_from_email, 'メールアドレス記載' )

        guild_press_personal_from_cc_email = self.driver_func.get_element_by_name( 'guild_press_personal_CC_email' )
        self.driver_func.clear_item_info( guild_press_personal_from_cc_email )
        self.driver_func.put_item_info( guild_press_personal_from_cc_email, 'メールアドレス記載' )

        guild_press_personal_from_bcc_email = self.driver_func.get_element_by_name( 'guild_press_personal_BCC_email' )
        self.driver_func.clear_item_info( guild_press_personal_from_bcc_email )
        self.driver_func.put_item_info( guild_press_personal_from_bcc_email, 'メールアドレス記載' )

        guild_press_personal_from_subject_email = self.driver_func.get_element_by_name( 'guild_press_personal_from_subject' )
        self.driver_func.clear_item_info( guild_press_personal_from_subject_email )
        self.driver_func.put_item_info( guild_press_personal_from_subject_email, 'メールテスト(ユーザー側)' )



        guild_press_personal_from_text_email = self.driver_func.get_element_by_name( 'guild_press_personal_email_message' )
        self.driver_func.clear_item_info( guild_press_personal_from_text_email )
        content_text = self.basic_func.get_file_text( self.base_dir+'/assets/texts/calendar/calendar_email_user.txt' )
        self.driver_func.put_item_info( guild_press_personal_from_text_email, content_text )

    def put_calendar_email_admin_info(self):

        guild_press_admin_from_text_name = self.driver_func.get_element_by_name( 'guild_press_admin_from_name' )
        self.driver_func.clear_item_info( guild_press_admin_from_text_name )
        self.driver_func.put_item_info( guild_press_admin_from_text_name, 'ユーザー側カレンダーテスト' )

        guild_press_admin_from_email = self.driver_func.get_element_by_name( 'guild_press_admin_from_email' )
        self.driver_func.clear_item_info( guild_press_admin_from_email )
        self.driver_func.put_item_info( guild_press_admin_from_email, 'メールアドレス記載' )


        guild_press_admin_from_cc_email = self.driver_func.get_element_by_name( 'guild_press_admin_CC_email' )
        self.driver_func.clear_item_info( guild_press_admin_from_cc_email )
        self.driver_func.put_item_info( guild_press_admin_from_cc_email, 'メールアドレス記載' )

        guild_press_admin_from_bcc_email = self.driver_func.get_element_by_name( 'guild_press_admin_BCC_email' )
        self.driver_func.clear_item_info( guild_press_admin_from_bcc_email )
        self.driver_func.put_item_info( guild_press_admin_from_bcc_email, 'メールアドレス記載' )

        guild_press_admin_from_subject_email = self.driver_func.get_element_by_name( 'guild_press_admin_from_subject' )
        self.driver_func.clear_item_info( guild_press_admin_from_subject_email )
        self.driver_func.put_item_info( guild_press_admin_from_subject_email, 'ユーザーイベント登録メール(管理者側)' )

        guild_press_admin_from_admin_email = self.driver_func.get_element_by_name( 'guild_press_admin_email_message' )
        self.driver_func.clear_item_info( guild_press_admin_from_admin_email )
        content_text = self.basic_func.get_file_text( self.base_dir+'/assets/texts/calendar/calendar_email_admin.txt' )
        self.driver_func.put_item_info( guild_press_admin_from_admin_email, content_text )


    def edit_calendar_info(self, target_title):
        dt_now = datetime.datetime.now()

        calendar_title_element = self.driver_func.get_element_by_name( 'title' )
        self.driver_func.clear_item_info( calendar_title_element )
        self.driver_func.put_item_info( calendar_title_element, target_title )

        calendar_max_element = self.driver_func.get_element_by_name( 'max_num' )
        self.driver_func.clear_item_info( calendar_max_element )
        self.driver_func.put_item_info( calendar_max_element, '5' )

        calendar_date_time1_element = self.driver_func.get_element_by_name( 'date_time1' )
        self.driver_func.clear_item_info( calendar_date_time1_element )
        self.driver_func.put_item_info( calendar_date_time1_element, '12:00' )

        calendar_date_time2_element = self.driver_func.get_element_by_name( 'date_time2' )
        self.driver_func.clear_item_info( calendar_date_time2_element )
        self.driver_func.put_item_info( calendar_date_time2_element, '22:00' )

        submit_btn_element = self.driver_func.get_element_by_name( 'submit' )
        self.driver_func.click_item( submit_btn_element )


    #put_calendar_infoで作ったやつを編集するために、リンクを探してクリックする。
    def edit_calendar_info_page( self, target_title ):
        guild_press_register_calendar_elements = self.driver_func.get_elements_by_xpath( '//div[@class="reservation-view"]/a[@class="calendar-title"]' )
        for calendar_title_element in guild_press_register_calendar_elements:

            if( target_title == calendar_title_element.text ):
                self.driver_func.click_item( calendar_title_element )
                self.edit_calendar_info( target_title )





