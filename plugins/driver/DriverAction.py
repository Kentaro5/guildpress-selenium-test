from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from plugins.xpath.AdminMenuPath import Admin_Menu_Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from plugins.basic.basic import Basic
import time
import datetime


class Driver_Action:

    def __init__(self, driver):
        self.chrome = driver
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

    def go_to_public_nav_menu( self, target_menu_name ):
        nav_menu_list = self.public_parts_xpath['nav_list_xpath']

        nav_menu_lists_elem = self.get_elements_by_xpath( nav_menu_list )

        lesson_list_elem = self.basic_func.get_target_element( nav_menu_lists_elem, target_menu_name )

        self.click_item( lesson_list_elem )


    def go_to_public_menu( self, target_menu_name ):

        menu_list = self.public_parts_xpath['menu_list_xpath']

        menu_lists_elem = self.get_elements_by_xpath( menu_list )

        lesson_list_elem = self.basic_func.get_target_element( menu_lists_elem, target_menu_name )

        self.click_item( lesson_list_elem )

    def get_element_by_xpath( self, element_xpath ):
        return self.chrome.find_element_by_xpath(element_xpath)

    #要素を複数見つけて返す
    def get_elements_by_xpath( self, element_xpath ):
        return self.chrome.find_elements_by_xpath(element_xpath)

    def click_item( self, element_name ):
        element_name.click()

    def get_element_by_id( self, element_name ):
        return self.chrome.find_element_by_id( element_name )

    def get_element_by_name( self, element_name ):
        return self.chrome.find_element_by_name( element_name )

    def get_element_by_tag_name( self, element_name ):
        return self.chrome.find_element_by_tag_name( element_name )

    def get_element_by_css_selector( self, selector_name ):
        return self.chrome.find_element_by_css_selector( selector_name )


    def get_link( self, element_name ):
        return element_name.get_attribute('href')


    def set_select_item( self, element, set_value ):
        #選択したいvalueを指定する
        Select( element ).select_by_visible_text( set_value )

    def submit( self, element ):
        element.submit()


    def put_item_info( self, target_element, set_value ):
        target_element.send_keys( set_value )

    def move_create_add_new_page( self, page_wp_menu, new_page_wp_menu ):

        driver_action = ActionChains(self.chrome)
        main_menu_box = self.chrome.find_element_by_xpath(page_wp_menu)

        driver_action.move_to_element(main_menu_box).perform()

        sub_menu_box = self.chrome.find_element_by_xpath(new_page_wp_menu).get_attribute('href')
        self.chrome.get(sub_menu_box)

    def clear_item_info(  self, target_element  ):
        target_element.clear()

    def stop( self, stop_num ):
        time.sleep( stop_num )

    #管理画面のメニューを移動する。
    def move_admin_page( self, main_menu_path, sub_menu_path ):

        driver_action = ActionChains(self.chrome)
        main_menu_box = self.chrome.find_element_by_xpath(main_menu_path)

        driver_action.move_to_element(main_menu_box).perform()

        sub_menu_box = self.chrome.find_element_by_xpath(sub_menu_path).get_attribute('href')
        self.chrome.get(sub_menu_box)

    #一覧から選んで移動する
    def single_move_admin_page( self, main_menu_path ):
        main_menu_box = self.chrome.find_element_by_xpath(main_menu_path).get_attribute('href')
        self.chrome.get(main_menu_box)

    #一覧から選んで移動する
    def go_to_add_new_page( self ):
        add_new_btn_xpath = '//div[@id="wpbody-content"]/div[@class="wrap"]/a[@class="page-title-action"][text()="新規追加"]'
        add_new_btn = self.chrome.find_element_by_xpath(add_new_btn_xpath)
        add_new_btn.click()

    #固定ページや登録ページにあるリンクを取得する。
    def edit_page_link( self ):
        link_xpath = '//div[@id="titlediv"]/div[@class="inside"]/div[@id="edit-slug-box"]/span[@id="sample-permalink"]/a'
        page_link = self.chrome.find_element_by_xpath( link_xpath ).get_attribute('href')

        return page_link

    #固定ページの公開ボタンをクリックする。
    def click_publish_btn(self):
        publish_btn_path = '//div[@id="publishing-action"]/input[@id="publish"]'
        publish_btn = self.chrome.find_element_by_xpath(publish_btn_path)

        try:
            WebDriverWait(self.chrome, 3).until( EC.alert_is_present() )

            alert = self.chrome.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass

        publish_btn.click()

    def click_update_btn(self):

        update_post_btn_xpath = self.admin_parts_xpath['update_post_btn']
        update_post_btn_elem = self.get_element_by_xpath( update_post_btn_xpath )

        try:
            WebDriverWait(self.chrome, 2).until(EC.alert_is_present(),
            'Timed out waiting for PA creation ' +
            'confirmation popup to appear.')

            alert = self.chrome.switch_to.alert
            alert.accept()
            print("alert accepted")
        except TimeoutException:
            print("no alert")

        self.click_item( update_post_btn_elem )


    def move_to_page_by_link(self, driver, pag_link):
        driver.get(pag_link)

    def quit(self, driver):
        driver.quit()

    def scroll_half_down( self, driver ):
        height = driver.execute_script("return document.body.scrollHeight")
        height = height // 4

        for x in range(1,height):
            driver.execute_script("window.scrollTo(0, "+str(x)+");")

    # 下にゆっくりスクール
    def scroll_down( self, driver ):
        height = driver.execute_script("return document.body.scrollHeight")
        height = height // 2

        for x in range(1,height):
            driver.execute_script("window.scrollTo(0, "+str(x)+");")

    #TOPに一瞬で戻る
    def scroll_top( self, driver ):
        driver.execute_script("window.scrollTo(0, 0);")

    def click_permalink( self ):
        post_permalink_xpath = self.admin_parts_xpath['post_permalink']
        post_permalink_elem = self.get_element_by_xpath( post_permalink_xpath )
        self.click_item( post_permalink_elem )

    def select_item_by_text( self, tareget_element, target_text ):
        Select(tareget_element).select_by_visible_text(target_text)
