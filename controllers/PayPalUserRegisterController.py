from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from plugins.basic.basic import Basic
from plugins.userregister.TestUserNormalRegister import Test_User_Normal_Register
from plugins.userregister.TestUserPaymentRegister import Test_User_Payment_Register
from plugins.driver.DriverAction import Driver_Action
from plugins.xpath.AdminMenuPath import Admin_Menu_Path

from plugins.paypal.PayPalAddNewOne import Pay_Pal_Add_New_One
from plugins.paypal.PayPalCreatePage import Pay_Pal_Create_Page

class PayPal_User_Register_Controller:

	def __init__(self, driver, target_url):
		self.chrome = driver
		self.target_url = target_url

		self.admin_xpath_list_func = Admin_Menu_Path()
		self.basic_func = Basic()
		self.driver_action_func = Driver_Action( driver )
		self.paypal_add_new_func = Pay_Pal_Add_New_One( driver )
		self.paypal_carete_page_func = Pay_Pal_Create_Page( driver )

		# 管理画面のメニューのパスを返す
		self.admin_xpath_lists = self.admin_xpath_list_func.get_admin_menu_xpath()

		# 管理画面メニュー内の新規追加や編集などのパーツのパスを返す。
		self.admin_list_parts_xpath = self.admin_xpath_list_func.get_admin_menu_list_parts_xpath()

	def start( self ):
		#PayPal設定ページに移動
		self.go_to_paypal_setting_page()

		#PayPalボタン作成画面に移動
		self.paypal_add_new_func.go_to_pay_pal_register_page()
		#継続課金のボタン作成
		self.paypal_add_new_func.add_normal_subscription_payment()

		payapl_short_code = self.paypal_carete_page_func.get_new_pay_pal_short_code()

		#固定ページ一覧に移動
		self.go_to_page_list()

		#新規追加ページへ移動
		self.driver_action_func.go_to_add_new_page()

		#ペイパルのページを作成
		self.paypal_carete_page_func.create_normal_subscription_page( payapl_short_code )

		#公開ボタンをクリックする。
		self.driver_action_func.click_publish_btn()

		#ペイパルのテスト
		self.test_pay_pal_regsiter()

		#トップページへ移動
		self.go_to_admin_top_page()


	def test_pay_pal_regsiter(self):

		paypal_page_link = self.driver_action_func.edit_page_link()

		new_paypal_register_driver = webdriver.Chrome(ChromeDriverManager().install())
		new_paypal_register_driver.get( paypal_page_link )

		# 新しいブラウザでインスタンス作成
		paypal_register_func = Test_User_Normal_Register( new_paypal_register_driver )
		paypal_register_func.nomarl_put_user_info_to_form()

		payment_register_func = Test_User_Payment_Register( new_paypal_register_driver )
		payment_register_func.click_register_page_pay_pal_btn()
		#payment_register_func.click_new_register_page_pay_pal_btn()

		self.driver_action_func.quit( new_paypal_register_driver )

	def go_to_paypal_setting_page( self ):
		admin_guild_press_page_path = self.admin_xpath_lists['admin_guild_press_page_path']
		admin_guild_press_paypal_page_path = self.admin_xpath_lists['admin_guild_press_paypal_page_path']

		self.driver_action_func.move_admin_page( admin_guild_press_page_path, admin_guild_press_paypal_page_path )

	def go_to_admin_top_page(self):
		self.driver_action_func.move_to_page_by_link( self.chrome, self.target_url + 'wp-admin/' )

	def go_to_page_list(self):
		admin_page_path = self.admin_xpath_lists['admin_page_path']
		admin_list_page_path = self.admin_xpath_lists['admin_list_page_path']

		self.driver_action_func.move_admin_page( admin_page_path, admin_list_page_path )










