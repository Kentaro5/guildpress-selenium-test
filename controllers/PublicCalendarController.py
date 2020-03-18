from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from plugins.basic.basic import Basic
from plugins.driver.DriverAction import Driver_Action
from plugins.xpath.AdminMenuPath import Admin_Menu_Path
from plugins.calendar.PublicCalendar import Public_Calendar
from plugins.userregister.UserRegisterSetting import User_Register_Setting
from plugins.userregister.TestUserNormalRegister import Test_User_Normal_Register

class Public_Calendar_Controller:

	def __init__(self, driver, target_url, calendar_title ):
		self.chrome = driver
		self.target_url = target_url

		self.admin_xpath_list_func = Admin_Menu_Path()
		self.basic_func = Basic()
		self.driver_action_func = Driver_Action( driver )
		self.user_register_func = User_Register_Setting( driver )

		self.calendar_title = calendar_title

		# 管理画面のメニューのパスを返す
		self.admin_xpath_lists = self.admin_xpath_list_func.get_admin_menu_xpath()

		# 管理画面メニュー内の新規追加や編集などのパーツのパスを返す。
		self.admin_list_parts_xpath = self.admin_xpath_list_func.get_admin_menu_list_parts_xpath()

	def start_many( self ):

		#固定ページ一覧へ移動
		self.go_to_page_list()

		#固定ページの中から、新規登録ページに移動する。
		self.go_to_new_register_page()

		#新規登録のURLを取得
		new_link = self.user_register_func.get_new_register_page_link()

		#新しくドライバーを作成
		new_normal_register_driver = webdriver.Chrome(ChromeDriverManager().install())

		#トップページへ移動
		new_normal_register_driver.get( new_link )

		# 新しいブラウザでインスタンス作成
		normal_register_func = Test_User_Normal_Register( new_normal_register_driver )

		# ユーザー情報を入れて、新しくユーザーを登録
		normal_register_func.nomarl_put_user_info_to_form()

		#インスタンス作成
		public_calendar_func = Public_Calendar( new_normal_register_driver )

		#カレンダーページへ移動
		public_calendar_func.go_to_calendar_page()

		for calendar_register_list_name in self.calendar_title:
			print(calendar_register_list_name)
			#カレンダーページの要素をクリックする。
			public_calendar_func.click_calendar( calendar_register_list_name )

			#カレンダーページ登録ページへ移動
			public_calendar_func.go_to_calendar_register_page()

			#カレンダー情報入力
			public_calendar_func.put_calendar_register_info()

			#カレンダー情報編集
			public_calendar_func.click_calendar( calendar_register_list_name )
			public_calendar_func.go_to_calendar_edit_page()
			public_calendar_func.put_calendar_edit_info()

			#カレンダーページへ移動
			public_calendar_func.go_to_calendar_page()

		self.driver_action_func.quit( new_normal_register_driver )

		self.go_to_admin_top_page()

	def start( self ):
		#固定ページ一覧へ移動
		self.go_to_page_list()

		#固定ページの中から、新規登録ページに移動する。
		self.go_to_new_register_page()

		#新規登録のURLを取得
		new_link = self.user_register_func.get_new_register_page_link()

		#新しくドライバーを作成
		new_normal_register_driver = webdriver.Chrome(ChromeDriverManager().install())

		#トップページへ移動
		new_normal_register_driver.get( new_link )

		# 新しいブラウザでインスタンス作成
		normal_register_func = Test_User_Normal_Register( new_normal_register_driver )

		# ユーザー情報を入れて、新しくユーザーを登録
		normal_register_func.nomarl_put_user_info_to_form()

		#インスタンス作成
		public_calendar_func = Public_Calendar( new_normal_register_driver )

		#カレンダーページへ移動
		public_calendar_func.go_to_calendar_page()

		#カレンダーページの要素をクリックする。
		public_calendar_func.click_calendar( self.calendar_title )

		#カレンダーページ登録ページへ移動
		public_calendar_func.go_to_calendar_register_page()

		#カレンダー情報入力
		public_calendar_func.put_calendar_register_info()

		#カレンダー情報編集
		public_calendar_func.click_calendar( self.calendar_title )
		public_calendar_func.go_to_calendar_edit_page()
		public_calendar_func.put_calendar_edit_info()

		self.driver_action_func.quit( new_normal_register_driver )

		self.go_to_admin_top_page()

	def go_to_page_list( self ):
		admin_page_path = self.admin_xpath_lists['admin_page_path']
		admin_list_page_path = self.admin_xpath_lists['admin_list_page_path']

		self.driver_action_func.move_admin_page( admin_page_path, admin_list_page_path )

	def go_to_admin_top_page(self):
		self.driver_action_func.move_to_page_by_link( self.chrome, self.target_url + 'wp-admin/' )


	def go_to_new_register_page( self ):
		admin_new_regsiter_page_path = self.admin_xpath_lists['admin_new_regsiter_page_path']
		self.driver_action_func.single_move_admin_page( admin_new_regsiter_page_path )











