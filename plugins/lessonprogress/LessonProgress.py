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


class Lesson_Progress:

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

		#ユーザー側の画面のメニューとか、動画一覧などのパーツ
		self.public_parts_xpath = self.admin_xpath_list_func.get_public_parts()

		self.base_dir = self.basic_func.get_base_dir_path()

		self.lesson_list_page_url = self.basic_func.get_lesson_list_page()

	def go_to_lesson_list_page( self ):
		print( 'go_to_lesson_list_page' )
		self.driver_func.move_to_page_by_link( self.chrome, self.lesson_list_page_url )

	def progress_each_lesson( self ):

		all_lesson_list = self.public_parts_xpath['all_lesson_list_xpath']
		all_lesson_list_link = self.public_parts_xpath['all_lesson_list_link_xpath']

		first_lesson_link = self.public_parts_xpath['first_lesson_link_xpath']

		lesson_comp_btn = self.public_parts_xpath['lesson_comp_btn_xpath']
		lesson_next_btn = self.public_parts_xpath['lesson_next_btn_xpath']

		target_lesson_lists = {
			'英語初級講座',
			'英語中級講座',
			'英語上級講座'
		}

		for target_lesson_text in target_lesson_lists:

			self.driver_func.stop(2)
			all_lesson_lists_elem = self.driver_func.get_elements_by_xpath( all_lesson_list )
			all_lesson_lists_link_elem = self.driver_func.get_elements_by_xpath( all_lesson_list_link )
			#概要ページから該当する名前順にリンクの要素を取得
			link_elem = self.basic_func.get_target_link_element( all_lesson_lists_elem, all_lesson_lists_link_elem, target_lesson_text )

			#リンクを取得
			lesson_detail_link = self.driver_func.get_link( link_elem )

			#リンクに飛ぶ
			self.driver_func.move_to_page_by_link( self.chrome, lesson_detail_link )

			#概要ページのすべてのレッスンを取得する
			first_lesson_elem = self.driver_func.get_elements_by_xpath( first_lesson_link )

			#最初のレッスンをクリックする。
			self.driver_func.click_item( first_lesson_elem[0] )

			self.driver_func.stop(1)

			#レッスンの総数分だけ、レッスン完了をクリックして、レッスンを完了していく。
			for i in range( len( first_lesson_elem ) ):
				lesson_comp_btn_elem = self.driver_func.get_element_by_xpath( lesson_comp_btn )
				self.driver_func.click_item( lesson_comp_btn_elem )

				#次のページへ進むが最後のページにはないので、それをチェックする。
				try:
					lesson_next_btn_elem = self.driver_func.get_element_by_xpath( lesson_next_btn )
					self.driver_func.click_item( lesson_next_btn_elem )
				except NoSuchElementException:
					print('none')


			self.driver_func.move_to_page_by_link( self.chrome, self.lesson_list_page_url )




