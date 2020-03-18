from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
import os

class Basic:

    def get_file_text(self, file_dir):
        f = open( file_dir )
        text_data = f.read()
        f.close()
        return text_data

    def get_base_dir_path( self ):
        return os.getcwd()

    def check_page_is_created( self, target_text, page_lists ):

        for element in page_lists:

            if( target_text == element.text ):
                return True

        return False

    #複数のリストから指定したものを返す処理
    def get_target_element( self, tareget_lists_item, target_text ):

        for target_list_elem in tareget_lists_item:
            if( target_list_elem.text == target_text ):
                return target_list_elem


    def get_target_link_element( self, first_tareget_lists_item, second_tareget_lists_item, target_text ):

        for first_tareget_list_item, second_tareget_list_item in zip( first_tareget_lists_item, second_tareget_lists_item ):
            if( first_tareget_list_item.text == target_text ):
                return second_tareget_list_item

    def get_calendar_page_url( self ):
        return 'https://vbjapan.xsrv.jp/wp_test/%E3%82%AB%E3%83%AC%E3%83%B3%E3%83%80%E3%83%BC%E3%83%9A%E3%83%BC%E3%82%B8/'
        #return 'https://product.guildpress.net/%E3%82%AB%E3%83%AC%E3%83%B3%E3%83%80%E3%83%BC%E3%83%9A%E3%83%BC%E3%82%B8/'

    def get_my_page_url( self ):
        return 'https://vbjapan.xsrv.jp/wp_test/%E3%83%9E%E3%82%A4%E3%81%BA%E3%83%BC%E3%82%B7%E3%82%99/'
        #return 'https://product.guildpress.net/%E3%83%9E%E3%82%A4%E3%81%BA%E3%83%BC%E3%82%B7%E3%82%99/'

    def get_lesson_list_page(self):
        return 'https://vbjapan.xsrv.jp/wp_test/%E5%8B%95%E7%94%BB%E4%B8%80%E8%A6%A7%E3%83%9A%E3%83%BC%E3%82%B8/'
        #return 'https://product.guildpress.net/%E5%8B%95%E7%94%BB%E4%B8%80%E8%A6%A7%E3%83%9A%E3%83%BC%E3%82%B8/'
