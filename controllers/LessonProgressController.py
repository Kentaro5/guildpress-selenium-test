from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from plugins.basic.basic import Basic
from plugins.driver.DriverAction import Driver_Action
from plugins.xpath.AdminMenuPath import Admin_Menu_Path
from plugins.singlepage.InitSettings import Init_Settings
from plugins.userregister.UserRegisterSetting import User_Register_Setting
from plugins.userregister.TestUserNormalRegister import Test_User_Normal_Register
from plugins.lessonprogress.LessonProgress import Lesson_Progress

class Lesson_Progress_Controller:

	def __init__(self, driver, target_url):
		self.chrome = driver
		self.target_url = target_url

		self.admin_xpath_list_func = Admin_Menu_Path()
		self.basic_func = Basic()
		self.driver_action_func = Driver_Action( driver )
		self.user_register_func = User_Register_Setting( driver )

		# 管理画面のメニューのパスを返す
		self.admin_xpath_lists = self.admin_xpath_list_func.get_admin_menu_xpath()

		# 管理画面メニュー内の新規追加や編集などのパーツのパスを返す。
		self.admin_list_parts_xpath = self.admin_xpath_list_func.get_admin_menu_list_parts_xpath()

	def start( self ):
		#固定ページ一覧に移動
		self.go_to_page_list()

		#固定ページの中から、新規登録ページに移動する。
		self.go_to_new_register_page()

		new_link = self.user_register_func.get_new_register_page_link()

		# 普通にbasicに新しく開く処理をするとなぜか、新しくひらいたクロームが落ちてしまうのでここで普通に新しく作成。
		new_normal_register_driver = webdriver.Chrome(ChromeDriverManager().install())
		new_normal_register_driver.get( new_link )

		# 新しいブラウザでインスタンス作成
		normal_register_func = Test_User_Normal_Register( new_normal_register_driver )

		# ユーザー情報を入れて、新しくユーザーを登録
		normal_register_func.nomarl_put_user_info_to_form()

		lesson_progress_func = Lesson_Progress( new_normal_register_driver )

		#動画一覧ページに移動して、そのリンクの要素を取得
		lesson_progress_func.go_to_lesson_list_page()

		#各動画の完了ボタンをクリックして、進捗を進めていく
		lesson_progress_func.progress_each_lesson()

		#トップページへ移動　
		self.go_to_admin_top_page()


	def go_to_new_register_page( self ):
		admin_new_regsiter_page_path = self.admin_xpath_lists['admin_new_regsiter_page_path']
		self.driver_action_func.single_move_admin_page( admin_new_regsiter_page_path )

	def go_to_page_list( self ):
		admin_page_path = self.admin_xpath_lists['admin_page_path']
		admin_list_page_path = self.admin_xpath_lists['admin_list_page_path']

		self.driver_action_func.move_admin_page( admin_page_path, admin_list_page_path )

	def go_to_admin_top_page(self):
		self.driver_action_func.move_to_page_by_link( self.chrome, self.target_url + 'wp-admin/' )











