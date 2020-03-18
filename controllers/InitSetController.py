from selenium import webdriver
from plugins.basic.basic import Basic
from plugins.singlepage.InitSettings import Init_Settings
from plugins.driver.DriverAction import Driver_Action
from plugins.xpath.AdminMenuPath import Admin_Menu_Path
from plugins.userregister.UserRegisterSetting import User_Register_Setting

class Init_Set_Controller:

    def __init__(self, driver, target_url):
        self.chrome = driver
        self.target_url = target_url

        self.admin_xpath_list_func = Admin_Menu_Path()
        self.basic_func = Basic()
        self.driver_action_func = Driver_Action( driver )
        self.init_settings_func = Init_Settings( driver )
        self.user_register_setting_func = User_Register_Setting( driver )

        # 管理画面のメニューのパスを返す
        self.admin_xpath_lists = self.admin_xpath_list_func.get_admin_menu_xpath()

        # 管理画面メニュー内の新規追加や編集などのパーツのパスを返す。
        self.admin_list_parts_xpath = self.admin_xpath_list_func.get_admin_menu_list_parts_xpath()

    def get_page_list( self ):

        page_lists = {
            '新規登録ページ' : '[guild_press_user_register]',
            'マイぺージ' : '[guild_press_my_page]',
            'ログインページ' : '[guild_press_login_page]',
            'ユーザー情報編集ページ' : '[guild_press_edit_user_info]',
            '動画一覧ページ' : '[guild_press_all_lesson]',
            '教材一覧ページ' : '[guild_press_list_texts_docs]',
        }

        return page_lists

    def start( self ):
        admin_main_setting_path = self.admin_xpath_lists['admin_main_setting_path']
        admin_sub_setting_path = self.admin_xpath_lists['admin_sub_setting_path']
        page_lists = self.get_page_list()

        for page_title, page_shortcode in page_lists.items():
            #固定ページリストへ移動
            self.go_to_page_list()

            #ページの作成
            self.driver_action_func.go_to_add_new_page()
            self.init_settings_func.create_new_guild_press_shortcode_page( page_title, page_shortcode )

            #公開ボタンをクリック
            self.driver_action_func.click_publish_btn()

            self.driver_action_func.stop(3)
            #一度トップページへ移動
            self.go_to_admin_top_page()

        #設定の保存　
        self.init_settings_func.move_to_guild_press_setting_page()
        self.init_settings_func.set_up_guild_press_settings()

        #一般設定に移動
        self.driver_action_func.move_admin_page( admin_main_setting_path, admin_sub_setting_path )

        #一般設定がちゃんとされているかチェックする。
        self.user_register_setting_func.check_membership_setting()

        #トップページへ移動
        self.go_to_admin_top_page()

    def go_to_admin_top_page(self):
        self.driver_action_func.move_to_page_by_link( self.chrome, self.target_url + 'wp-admin/' )

    def go_to_page_list( self ):
        admin_page_path = self.admin_xpath_lists['admin_page_path']
        admin_list_page_path = self.admin_xpath_lists['admin_list_page_path']

        self.driver_action_func.move_admin_page( admin_page_path, admin_list_page_path )






