from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from plugins.basic.basic import Basic
from plugins.driver.DriverAction import Driver_Action
from plugins.xpath.AdminMenuPath import Admin_Menu_Path
from plugins.memberrank.AdminMemberRank import Admin_Member_Rank
from plugins.memberrank.PublicMemberRank import Public_Member_Rank
from plugins.userregister.UserRegisterSetting import User_Register_Setting
from plugins.userregister.TestUserNormalRegister import Test_User_Normal_Register
from plugins.userregister.TestUserPaymentRegister import Test_User_Payment_Register
from plugins.paypal.PayPalAddNewOne import Pay_Pal_Add_New_One
from plugins.lessonprogress.LessonProgress import Lesson_Progress
from plugins.paypal.PayPalCreatePage import Pay_Pal_Create_Page

class Member_Rank_Detail_Posts_Controller:

	def __init__(self, driver, target_url):
		self.chrome = driver
		self.target_url = target_url

		self.admin_xpath_list_func = Admin_Menu_Path()
		self.basic_func = Basic()
		self.driver_action_func = Driver_Action( driver )
		self.admin_member_rank_func = Admin_Member_Rank( driver )
		self.user_register_func = User_Register_Setting( driver )
		self.paypal_add_new_func = Pay_Pal_Add_New_One( driver )
		self.paypal_carete_page_func = Pay_Pal_Create_Page( driver )


		# 管理画面のメニューのパスを返す
		self.admin_xpath_lists = self.admin_xpath_list_func.get_admin_menu_xpath()

		# 管理画面メニュー内の新規追加や編集などのパーツのパスを返す。
		self.admin_list_parts_xpath = self.admin_xpath_list_func.get_admin_menu_list_parts_xpath()

	def start( self ):
		##レッスン詳細ページにブロックを設定する。
		#GuildPressレッスン一覧新規追加ページへ移動
		self.go_to_lesson_detail_list_page()

		#ページブロックをそれぞれ行う。
		self.admin_member_rank_func.add_block_setting_detail_page()

		##別のタブを立ち上げて、普通にユーザー登録をして、表示を確認する。
		#固定ページ一覧に移動
		self.go_to_page_list()

		#固定ページの中から、新規登録ページに移動する。
		self.go_to_new_register_page()

		# 普通にbasicに新しく開く処理をするとなぜか、新しくひらいたクロームが落ちてしまうのでここで普通に新しく作成。
		self.check_block_page_by_normal_regsiter()

		##ゴールド会員で登録して、表示をチェックする。
		self.check_block_page_by_paypal_regsiter()

		#トップページへ戻る
		self.go_to_admin_top_page()

		#ブロックした項目をリセットする　
		self.reset_block_page()

		#トップページへ戻る
		self.go_to_admin_top_page()

	def check_block_page_by_paypal_regsiter(self):

		#ペイパル設定ページへ移動する
		self.go_to_paypal_setting_page()

		self.paypal_add_new_func.go_to_pay_pal_register_page()

		self.paypal_add_new_func.add_member_subscription_payment()

		payapl_short_code = self.paypal_carete_page_func.get_new_pay_pal_short_code()

		#固定ページ一覧に移動
		self.go_to_page_list()

		self.driver_action_func.go_to_add_new_page()

		self.paypal_carete_page_func.create_member_subscription_page( payapl_short_code )

		#公開ボタンをクリックする。
		self.driver_action_func.click_publish_btn()

		paypal_page_link = self.driver_action_func.edit_page_link()

		new_paypal_register_driver = webdriver.Chrome(ChromeDriverManager().install())
		new_paypal_register_driver.get( paypal_page_link )

		##今度はゴールド会員として登録して表示をチェックする。
		# 新しいブラウザでインスタンス作成
		paypal_register_func = Test_User_Normal_Register( new_paypal_register_driver )

		payment_register_func = Test_User_Payment_Register( new_paypal_register_driver )

		paypal_register_func.nomarl_put_user_info_to_form()

		payment_register_func.click_register_page_pay_pal_btn()
		#payment_register_func.click_new_register_page_pay_pal_btn()

		##PayPalで登録した後に、ページに移動して動作を確認する。
		paypal_public_member_rank_func = Public_Member_Rank( new_paypal_register_driver )

		#動画一覧ページに移動して、そのリンクの要素を取得
		paypal_public_member_rank_func.go_to_lesson_list_page()

		result = paypal_public_member_rank_func.check_is_user_get_ranked()

		if( result == False ):
			another_driver_action_func = Driver_Action( new_paypal_register_driver )
			xpath = "//ul[@id='wp-admin-bar-top-secondary']/li[@id='wp-admin-bar-my-account']/div[@class='ab-sub-wrapper']/ul[@id='wp-admin-bar-user-actions']/li[@id='wp-admin-bar-user-info']/a[@class='ab-item']/span[@class='display-name']"
			target_user_name = another_driver_action_func.get_element_by_xpath(xpath).get_attribute("innerHTML")

			#admin側を動かすために、あどみん側のドライバーを渡す。
			paypal_admin_member_rank_func = Public_Member_Rank( self.chrome )

			paypal_admin_member_rank_func.set_user_status_to_gold( target_user_name )

			paypal_admin_member_rank_func.go_to_admin_top_page( self.target_url )

			paypal_public_member_rank_func.go_to_lesson_list_page()

		paypal_public_member_rank_func.check_element_page()

		#レッスンリストページに戻る
		paypal_public_member_rank_func.go_to_lesson_list_page()

		#上級コースの表示もチェックする。
		paypal_public_member_rank_func.check_advanced_page()


		self.driver_action_func.stop(3)
		self.driver_action_func.quit( new_paypal_register_driver )


	def reset_block_page( self ):
		self.go_to_lesson_detail_list_page()

		self.admin_member_rank_func.reset_block_setting_detail_page()


	def check_block_page_by_normal_regsiter(self):

		new_link = self.user_register_func.get_new_register_page_link()

		new_normal_register_driver = webdriver.Chrome(ChromeDriverManager().install())
		new_normal_register_driver.get( new_link )

		# 新しいブラウザでインスタンス作成
		normal_register_func = Test_User_Normal_Register( new_normal_register_driver )

		# ユーザー情報を入れて、新しくユーザーを登録
		normal_register_func.nomarl_put_user_info_to_form()

		public_member_rank_func = Public_Member_Rank( new_normal_register_driver )

		#動画一覧ページに移動して、そのリンクの要素を取得
		public_member_rank_func.go_to_lesson_list_page()

		#レッスンリストページに戻る
		public_member_rank_func.go_to_lesson_list_page()

		#上級コースの表示もチェックする。
		public_member_rank_func.check_element_page()

		self.driver_action_func.stop(3)
		self.driver_action_func.quit( new_normal_register_driver )

	def go_to_lesson_detail_list_page( self ):
		admin_guild_press_lesson_detail_page_path = self.admin_xpath_lists['admin_guild_press_lesson_detail_page_path']
		admin_guild_press_lesson_detail_list_page_path = self.admin_xpath_lists['admin_guild_press_lesson_detail_list_page_path']

		self.driver_action_func.move_admin_page( admin_guild_press_lesson_detail_page_path, admin_guild_press_lesson_detail_list_page_path )



	def go_to_paypal_setting_page(self):
		admin_guild_press_page_path = self.admin_xpath_lists['admin_guild_press_page_path']
		admin_guild_press_paypal_page_path = self.admin_xpath_lists['admin_guild_press_paypal_page_path']

		self.driver_action_func.move_admin_page( admin_guild_press_page_path, admin_guild_press_paypal_page_path )


	def go_to_new_register_page( self ):
		admin_new_regsiter_page_path = self.admin_xpath_lists['admin_new_regsiter_page_path']

		self.driver_action_func.single_move_admin_page( admin_new_regsiter_page_path )


	def go_to_page_list( self ):
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











