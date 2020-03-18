from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from plugins.xpath.AdminMenuPath import Admin_Menu_Path


import time

class Init_Settings:

    def __init__(self, driver):
        
        self.chrome = driver
        self.admin_xpath_list_func = Admin_Menu_Path()

    def move_create_new_page(self):

        page_wp_menu = '//div[@class="wp-menu-name"][text()="固定ページ"]'

        new_page_wp_menu = '//div[@id="adminmenuwrap"]/ul[@id="adminmenu"]/li[@id="menu-pages"]/ul[@class="wp-submenu wp-submenu-wrap"]/li[3]/a[text()="新規追加"]'

        driver_action = ActionChains(self.chrome)
        main_menu_box = self.chrome.find_element_by_xpath(page_wp_menu)
        
        driver_action.move_to_element(main_menu_box).perform()

        sub_menu_box = self.chrome.find_element_by_xpath(new_page_wp_menu).get_attribute('href')
        self.chrome.get(sub_menu_box)


    def create_new_guild_press_shortcode_page(self, page_title, shortcode):

        title_box = self.chrome.find_element_by_name('post_title')
        title_box.send_keys( page_title )

        self.chrome.find_element_by_id('content-html').click()

        content_box = self.chrome.find_element_by_name('content')
        content_box.send_keys( shortcode )


    def move_to_guild_press_setting_page(self):

        page_wp_menu = '//div[@class="wp-menu-name"][text()="GuildPress"]'

        new_page_wp_menu = '//ul[@class="wp-submenu wp-submenu-wrap"]/li[@class="wp-first-item"]/a[@class="wp-first-item"][text()="GuildPress"]'

        driver_action = ActionChains(self.chrome)
        main_menu_box = self.chrome.find_element_by_xpath(page_wp_menu)

        driver_action.move_to_element(main_menu_box).perform()

        sub_menu_box = self.chrome.find_element_by_xpath(new_page_wp_menu).get_attribute('href')
        self.chrome.get(sub_menu_box)

    def set_up_guild_press_settings(self):

        publish_btn = self.chrome.find_element_by_name('submit')

        target_element = ['guild_press_register', 'guild_press_mypage', 'guild_press_edit_user_info', 'guild_press_login']
        strings = ['新規登録ページ', 'マイぺージ', 'ユーザー情報編集ページ', 'ログインページ']

        for select_element, taget_string in zip( target_element, strings ) :

            setting_element = self.chrome.find_element_by_name( select_element )

            # 取得したエレメントをSelectタグに対応したエレメントに変化させる
            setting_select_element = Select(setting_element)

            # 選択したいvalueを指定する
            setting_select_element.select_by_visible_text(taget_string)

        publish_btn.click()

        time.sleep(3)


                















