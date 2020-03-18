from selenium import webdriver
from plugins.basic.basic import Basic
from plugins.driver.DriverAction import Driver_Action
from plugins.xpath.AdminMenuPath import Admin_Menu_Path
from plugins.manycalendars.AdminManyCalendar import Admin_Many_Calendar
from plugins.singlepage.InitSettings import Init_Settings

class Admin_Many_Calendars_Controller:

    def __init__(self, driver, target_url):
        self.chrome = driver
        self.target_url = target_url

        self.admin_xpath_list_func = Admin_Menu_Path()
        self.basic_func = Basic()
        self.driver_action_func = Driver_Action( driver )
        self.admin_many_calendar = Admin_Many_Calendar( driver )
        self.init_settings_func = Init_Settings( driver )

        self.calendar_titles = []

        # 管理画面のメニューのパスを返す
        self.admin_xpath_lists = self.admin_xpath_list_func.get_admin_menu_xpath()

        # 管理画面メニュー内の新規追加や編集などのパーツのパスを返す。
        self.admin_list_parts_xpath = self.admin_xpath_list_func.get_admin_menu_list_parts_xpath()

        #カレンダーを登録できるリンクのパス
        self.admin_calendar_parts_xpath = self.admin_xpath_list_func.get_many_calendar_parts()

    def start( self ):
        #固定ページ一覧へ移動
        self.go_to_page_list()

        # カレンダー一覧ページへ移動する。
        self.go_to_calendar_page()

        #カレンダーデータの登録
        self.register_many_calendar()

        #トップページへ戻る
        self.go_to_admin_top_page()

    def get_calendar_titles( self ):
        return self.calendar_titles

    def register_many_calendar(self):

        for calendar_register_list_name, calendar_register_list_xpath in self.admin_calendar_parts_xpath.items():
            self.admin_many_calendar.go_to_register_calendar_list_page()
            result = self.admin_many_calendar.go_to_register_calendar_page( calendar_register_list_xpath )

            if result :
                for x in range( 5 ):
                    try:

                        calendar_title = self.admin_many_calendar.put_calendar_info()
                        self.admin_many_calendar.edit_calendar_info_page( calendar_title )
                        self.add_calendar_title_to_list( calendar_title )

                    except Exception as e:
                        print('error')

                    self.admin_many_calendar.go_to_register_calendar_list_page()
                    self.admin_many_calendar.go_to_register_calendar_page( calendar_register_list_xpath )


    def go_to_page_list( self ):
        admin_page_path = self.admin_xpath_lists['admin_page_path']
        admin_list_page_path = self.admin_xpath_lists['admin_list_page_path']

        self.driver_action_func.move_admin_page( admin_page_path, admin_list_page_path )

    def add_calendar_title_to_list( self, calendar_title ):
        self.calendar_titles.append( calendar_title )

    def go_to_calendar_page( self ):
        lesson_detail_page_path = self.admin_xpath_lists['admin_guild_press_lesson_detail_page_path']
        calendar_page_path = self.admin_xpath_lists['admin_guild_press_lesson_calendar_page_path']

        self.driver_action_func.move_admin_page( lesson_detail_page_path, calendar_page_path )

    def go_to_admin_top_page(self):
        self.driver_action_func.move_to_page_by_link( self.chrome, self.target_url + 'wp-admin/' )











