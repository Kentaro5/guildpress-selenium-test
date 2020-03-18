from selenium import webdriver
from plugins.basic.basic import Basic
from plugins.driver.DriverAction import Driver_Action
from plugins.xpath.AdminMenuPath import Admin_Menu_Path
from plugins.many.lesson.ManyLessonDetailPosts import Many_Lesson_Detail_Posts

class Many_Lesson_Detail_Posts_Controller:

    def __init__(self, driver, target_url):
        self.chrome = driver
        self.target_url = target_url

        self.admin_xpath_list_func = Admin_Menu_Path()
        self.basic_func = Basic()
        self.driver_action_func = Driver_Action( driver )
        self.many_lesson_detail_posts_func = Many_Lesson_Detail_Posts( driver )

        # 管理画面のメニューのパスを返す
        self.admin_xpath_lists = self.admin_xpath_list_func.get_admin_menu_xpath()

        # 管理画面メニュー内の新規追加や編集などのパーツのパスを返す。
        self.admin_list_parts_xpath = self.admin_xpath_list_func.get_admin_menu_list_parts_xpath()

    def start( self ):

        #GuildPress各レッスン登録一覧新規追加ページへ移動
        self.go_to_add_new_lesson_overview_page()

        # #レッスンの概要を詰める
        self.many_lesson_detail_posts_func.add_lesson_detail_page()

        # #トップページへ戻る
        self.go_to_admin_top_page()

    def go_to_admin_top_page(self):
        self.driver_action_func.move_to_page_by_link( self.chrome, self.target_url + 'wp-admin/' )

    def go_to_add_new_lesson_overview_page( self ):
        admin_guild_press_lesson_detail_page_path = self.admin_xpath_lists['admin_guild_press_lesson_detail_page_path']
        admin_guild_press_lesson_detail_list_page_path = self.admin_xpath_lists['admin_guild_press_lesson_detail_list_page_path']

        self.driver_action_func.move_admin_page( admin_guild_press_lesson_detail_page_path, admin_guild_press_lesson_detail_list_page_path )










