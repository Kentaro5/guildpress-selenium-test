from selenium import webdriver
from plugins.basic.basic import Basic
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

class User_Register_Setting:

    def __init__(self, driver):

        self.chrome = driver

    def check_membership_setting(self):

        check_element = self.chrome.find_element_by_name( 'users_can_register' )

        if( check_element.is_selected() ) :

            return
        else :
            #要素をチェックする。
            check_element.click()

            save_btn_element = self.chrome.find_element_by_name( 'submit' )
            save_btn_element.click()

    def get_new_register_page_link(self):

        register_link_xpath = '//div[@id="titlediv"]/div[@class="inside"]/div[@id="edit-slug-box"]/span[@id="sample-permalink"]/a'

        register_link = self.chrome.find_element_by_xpath( register_link_xpath ).get_attribute('href')

        return register_link

    #毎回ユーザーのがだるいので、登録したら削除するようにする。
    def delete_registered_user(self):

        delete_link_xpath = '//td[@class="username column-username has-row-actions column-primary"]/div[@class="row-actions"]/span[@class="delete"]/a[@class="submitdelete"][text()="削除"]'

        delete_link = self.chrome.find_element_by_xpath( delete_link_xpath ).get_attribute('href')

        self.chrome.get(delete_link)

        delete_btn_element = self.chrome.find_element_by_name( 'submit' )
        delete_btn_element.click()






