from selenium import webdriver
from plugins.basic.basic import Basic
from plugins.driver.DriverAction import Driver_Action
from plugins.xpath.AdminMenuPath import Admin_Menu_Path
from plugins.originalformitems.CreateOriginalForm import Create_Original_Form

class Original_Form_Controller:

	def __init__(self, driver, target_url):
		self.chrome = driver
		self.target_url = target_url

		self.admin_xpath_list_func = Admin_Menu_Path()
		self.basic_func = Basic()
		self.driver_action_func = Driver_Action( driver )
		self.create_original_form_func = Create_Original_Form( driver )

		# 管理画面のメニューのパスを返す
		self.admin_xpath_lists = self.admin_xpath_list_func.get_admin_menu_xpath()

		# 管理画面メニュー内の新規追加や編集などのパーツのパスを返す。
		self.admin_list_parts_xpath = self.admin_xpath_list_func.get_admin_menu_list_parts_xpath()

	def start( self ):

		#GuildPressユーザー登録フォーム項目に移動。
		self.go_to_guild_press_original_register_form()

		#ユーザー登録フォームでオリジナルの項目を登録する、
		self.create_original_form_func.add_original_form_inputs()

		#トップページへ戻る
		self.go_to_admin_top_page()


	def go_to_admin_top_page(self):
		self.driver_action_func.move_to_page_by_link( self.chrome, self.target_url + 'wp-admin/' )

	def go_to_guild_press_original_register_form( self ):
		admin_guild_press_page_path = self.admin_xpath_lists['admin_guild_press_page_path']
		admin_guild_press_original_form_page_path = self.admin_xpath_lists['admin_guild_press_original_form_page_path']

		self.driver_action_func.move_admin_page( admin_guild_press_page_path, admin_guild_press_original_form_page_path )





