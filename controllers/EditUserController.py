from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from plugins.basic.basic import Basic
from plugins.driver.DriverAction import Driver_Action
from plugins.xpath.AdminMenuPath import Admin_Menu_Path
from plugins.edituserinfo.PublicEditUser import Public_Edit_User
from plugins.userregister.UserRegisterSetting import User_Register_Setting
from plugins.userregister.TestUserNormalRegister import Test_User_Normal_Register
from plugins.userregister.TestUserPaymentRegister import Test_User_Payment_Register
from plugins.paypal.PayPalAddNewOne import Pay_Pal_Add_New_One
from plugins.lessonprogress.LessonProgress import Lesson_Progress
from plugins.paypal.PayPalCreatePage import Pay_Pal_Create_Page

class Edit_User_Controller:

	def __init__(self, driver, target_url):
		self.chrome = driver
		self.target_url = target_url

		self.admin_xpath_list_func = Admin_Menu_Path()
		self.basic_func = Basic()
		self.driver_action_func = Driver_Action( driver )
		self.user_register_func = User_Register_Setting( driver )
		self.paypal_add_new_func = Pay_Pal_Add_New_One( driver )
		self.paypal_carete_page_func = Pay_Pal_Create_Page( driver )

		# 管理画面のメニューのパスを返す
		self.admin_xpath_lists = self.admin_xpath_list_func.get_admin_menu_xpath()

		# 管理画面メニュー内の新規追加や編集などのパーツのパスを返す。
		self.admin_list_parts_xpath = self.admin_xpath_list_func.get_admin_menu_list_parts_xpath()

	def start( self ):

		#固定ページ一覧に移動
		self.go_page_list()

		#固定ページの中から、新規登録ページに移動する。
		self.go_to_new_register_page()

		#普通に登録して、ユーザー情報を編集できるかチェックする。
		self.check_edit_user_info()

		#トップページへ戻る
		self.go_to_admin_top_page()

	def check_edit_user_info( self ):

		new_link = self.user_register_func.get_new_register_page_link()

		# 普通にbasicに新しく開く処理をするとなぜか、新しくひらいたクロームが落ちてしまうのでここで普通に新しく作成。
		new_normal_register_driver = webdriver.Chrome(ChromeDriverManager().install())
		new_normal_register_driver.get( new_link )

		# 新しいブラウザでインスタンス作成
		normal_register_func = Test_User_Normal_Register( new_normal_register_driver )

		# ユーザー情報を入れて、新しくユーザーを登録
		normal_register_func.nomarl_put_user_info_to_form()

		public_edit_user_func = Public_Edit_User( new_normal_register_driver )
		public_edit_user_func.go_to_my_page()

		public_edit_user_func.go_to_edit_page()

		public_edit_user_func.edit_user_info()

		self.driver_action_func.stop(5)

		self.driver_action_func.quit( new_normal_register_driver )

	def go_to_lesson_detail_page( self ):
		admin_guild_press_lesson_detail_page_path = self.admin_xpath_lists['admin_guild_press_lesson_detail_page_path']
		admin_guild_press_lesson_detail_list_page_path = self.admin_xpath_lists['admin_guild_press_lesson_detail_list_page_path']

		self.driver_action_func.move_admin_page( admin_guild_press_lesson_detail_page_path, admin_guild_press_lesson_detail_list_page_path )

	def go_to_my_page( self ):
		admin_go_to_mypage_path = self.admin_xpath_lists['admin_go_to_mypage_path']

		self.driver_action_func.single_move_admin_page( admin_go_to_mypage_path )


	def go_to_paypal_setting_page(self):
		admin_guild_press_page_path = self.admin_xpath_lists['admin_guild_press_page_path']
		admin_guild_press_paypal_page_path = self.admin_xpath_lists['admin_guild_press_paypal_page_path']

		self.driver_action_func.move_admin_page( admin_guild_press_page_path, admin_guild_press_paypal_page_path )


	def go_to_new_register_page( self ):
		admin_new_regsiter_page_path = self.admin_xpath_lists['admin_new_regsiter_page_path']

		self.driver_action_func.single_move_admin_page( admin_new_regsiter_page_path )


	def go_page_list( self ):
		admin_page_path = self.admin_xpath_lists['admin_page_path']
		admin_list_page_path = self.admin_xpath_lists['admin_list_page_path']

		self.driver_action_func.move_admin_page( admin_page_path, admin_list_page_path )

	def go_to_lesson_over_view_page( self ):
		lesson_over_view_page_path = self.admin_xpath_lists['admin_guild_press_lesson_over_view_page_path']
		lesson_over_view_list_page_path = self.admin_xpath_lists['admin_guild_press_lesson_over_view_list_page_path']

		self.driver_action_func.move_admin_page( lesson_over_view_page_path, lesson_over_view_list_page_path )

	def go_to_member_rank_page( self ):
		admin_guild_press_page_path = self.admin_xpath_lists['admin_guild_press_page_path']
		admin_guild_press_member_rank_page_path = self.admin_xpath_lists['admin_guild_press_member_rank_page_path']

		self.driver_action_func.move_admin_page( admin_guild_press_page_path, admin_guild_press_member_rank_page_path )

	def go_to_admin_top_page(self):
		self.driver_action_func.move_to_page_by_link( self.chrome, self.target_url + 'wp-admin/' )











