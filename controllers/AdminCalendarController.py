from selenium import webdriver
from plugins.basic.basic import Basic
from plugins.driver.DriverAction import Driver_Action
from plugins.xpath.AdminMenuPath import Admin_Menu_Path
from plugins.calendar.AdminCalendar import Admin_Calendar
from plugins.singlepage.InitSettings import Init_Settings

class Admin_Calendar_Controller:

	def __init__(self, driver, target_url):
		self.chrome = driver
		self.target_url = target_url

		self.admin_xpath_list_func = Admin_Menu_Path()
		self.basic_func = Basic()
		self.driver_action_func = Driver_Action( driver )
		self.admin_calendar_func = Admin_Calendar( driver )
		self.init_settings_func = Init_Settings( driver )

		self.calendar_title = ''

		# 管理画面のメニューのパスを返す
		self.admin_xpath_lists = self.admin_xpath_list_func.get_admin_menu_xpath()

		# 管理画面メニュー内の新規追加や編集などのパーツのパスを返す。
		self.admin_list_parts_xpath = self.admin_xpath_list_func.get_admin_menu_list_parts_xpath()

	def start( self ):
		#固定ページ一覧へ移動
		self.go_to_page_list()

		#カレンダーの固定ページが作成されているチェックする。
		is_page_created = self.admin_calendar_func.create_public_calendar_page()

		if not is_page_created :
			#カレンダーページ作成
			self.driver_action_func.go_to_add_new_page()
			self.init_settings_func.create_new_guild_press_shortcode_page( 'カレンダーページ', '[guild_press_calender]' )
			self.driver_action_func.click_publish_btn()

		# カレンダー一覧ページへ移動する。
		self.go_to_calendar_page()

		# カレンダー登録ページへ移動する
		self.admin_calendar_func.go_to_register_calendar_page()

		#カレンダー登録ページへカレンダー情報を入力.
		self.calendar_title = self.admin_calendar_func.put_calendar_info()

		#カレンダー編集ページへ移動する
		self.admin_calendar_func.edit_calendar_info_page( self.calendar_title )

		# カレンダーメール編集ページへ移動する。
		self.admin_calendar_func.go_to_calendar_email_page()

		# カレンダーメールの内容を入力する。
		self.admin_calendar_func.put_calendar_email_info()

		#トップページへ戻る
		self.go_to_admin_top_page()

	def get_calendar_title( self ):
		return self.calendar_title

	def go_to_page_list( self ):
		admin_page_path = self.admin_xpath_lists['admin_page_path']
		admin_list_page_path = self.admin_xpath_lists['admin_list_page_path']

		self.driver_action_func.move_admin_page( admin_page_path, admin_list_page_path )

	def go_to_calendar_page( self ):
		lesson_detail_page_path = self.admin_xpath_lists['admin_guild_press_lesson_detail_page_path']
		calendar_page_path = self.admin_xpath_lists['admin_guild_press_lesson_calendar_page_path']

		self.driver_action_func.move_admin_page( lesson_detail_page_path, calendar_page_path )

	def go_to_admin_top_page(self):
		self.driver_action_func.move_to_page_by_link( self.chrome, self.target_url + 'wp-admin/' )











