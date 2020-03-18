from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from plugins.driver.DriverAction import Driver_Action
from plugins.xpath.AdminMenuPath import Admin_Menu_Path
from plugins.basic.basic import Basic
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import datetime


class Google_Calendar_Setting:


	def __init__(self, driver):

		self.chrome = driver
		self.driver_func = Driver_Action( driver )
		self.admin_xpath_list_func = Admin_Menu_Path()
		self.basic_func = Basic()
		# 管理画面のメニューのパスを返す
		self.admin_xpath_lists_xpath = self.admin_xpath_list_func.get_admin_menu_xpath()

		# 管理画面メニュー内の新規追加や編集などのパーツのパスを返す。
		self.admin_list_parts_xpath = self.admin_xpath_list_func.get_admin_menu_list_parts_xpath()

		# 管理画面内の項目に関するパス(作成した固定ページリストとか)
		self.admin_parts_xpath = self.admin_xpath_list_func.get_admin_parts()

		self.base_dir = self.basic_func.get_base_dir_path()

		self.google_api_xpath = self.admin_xpath_list_func.get_google_calendar_api_parts()


	def go_to_google_calendar_setting_page( self ):

		guild_press_setting_tab_elements = self.driver_func.get_elements_by_xpath( self.admin_parts_xpath['guild_press_setting_tab_xpath'] )

		self.driver_func.click_item( guild_press_setting_tab_elements[0] )



	#GoogleカレンダーのIDやシークレットを設定する。
	def put_google_calendar_setting_info( self ):


		google_client_id_element = self.driver_func.get_element_by_name( 'guild_press_google_client_id' )
		self.driver_func.clear_item_info( google_client_id_element )
		self.driver_func.put_item_info( google_client_id_element, 'client_id' )

		google_client_secret_element = self.driver_func.get_element_by_name( 'guild_press_google_client_secret' )
		self.driver_func.clear_item_info( google_client_secret_element )
		self.driver_func.put_item_info( google_client_secret_element, 'secret記載' )

		#情報を保存する。
		save_btn_element = self.driver_func.get_element_by_name( 'set' )
		self.driver_func.click_item( save_btn_element )


	#Googleカレンダーの設定ページへ移動して設定する。
	def set_google_calendar_api( self ):

		#calendar_apiを設定するためのボタンをクリック。
		google_auth_btn_element = self.driver_func.get_element_by_id( 'google_auth_btn' )
		self.driver_func.click_item( google_auth_btn_element )

		try:
			WebDriverWait(self.chrome, 3).until(EC.alert_is_present(),
			'Timed out waiting for PA creation ' +
			'confirmation popup to appear.')

			alert = self.chrome.switch_to.alert
			alert.accept()
			print("alert accepted")
		except TimeoutException:
			print("no alert")

		emails = self.driver_func.get_element_by_name( 'identifier' )
		self.driver_func.clear_item_info( emails )
		self.driver_func.put_item_info( emails, 'メールアドレス記載' )

		next_btn_element = self.driver_func.get_element_by_id( 'identifierNext' )
		self.driver_func.click_item( next_btn_element )

		self.driver_func.stop(3)

		password = self.driver_func.get_element_by_name( 'password' )
		self.driver_func.clear_item_info( password )
		self.driver_func.put_item_info( password, 'パスワード記載' )

		next_btn_element = self.driver_func.get_element_by_id( 'passwordNext' )
		self.driver_func.click_item( next_btn_element )

		self.driver_func.stop(5)


		selector = self.driver_func.get_element_by_css_selector( 'div[class="U26fgb O0WRkf oG5Srb C0oVfc kHssdc M9Bg4d"]' )


		ActionChains(self.chrome ).move_to_element(selector).click(selector).perform()

		self.driver_func.stop(5)

		submit_btn_elem = self.driver_func.get_element_by_id( 'submit_approve_access' )
		self.driver_func.click_item( submit_btn_elem )

		#self.google_api_xpath






