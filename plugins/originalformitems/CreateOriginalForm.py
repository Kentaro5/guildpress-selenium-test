from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.support.ui import Select
from plugins.driver.DriverAction import Driver_Action
import time
import datetime



class Create_Original_Form:

    def __init__(self, driver):
        self.chrome = driver
        self.driver_func = Driver_Action( driver )

    def click_submit_btn( self ):
        submit_input = self.chrome.find_element_by_name('submit')
        submit_input.click()

    #普通に登録
    def add_original_form_inputs( self ):

        dt_now = datetime.datetime.now()

        target_element = {
                'short_text' : {
                    'add_label' : 'ショートテキスト'+str( dt_now.microsecond ), 
                    'add_option' : 'short_text'+str( dt_now.microsecond ),
                    'add_type' : 'テキスト',
                    'add_display' : '',
                    'add_required' : '',
                },
                'text_area' : {
                    'add_label' : 'テキストエリア'+str( dt_now.microsecond ),
                    'add_option' : 'text_area'+str( dt_now.microsecond ),
                    'add_type' : 'テキストエリア',
                    'add_display' : '',
                    'add_required' : '',
                },
                'check_box' : {
                    'add_label' : 'チェックボックス', 
                    'add_option' : 'check_box'+str( dt_now.microsecond ),
                    'add_type' : 'チェックボックス',
                    'add_display' : '',
                    'add_required' : '',
                    'add_checked_default' : '',
                    'add_checked_value' : '1',
                },
                'select_box' : {
                    'add_label' : 'セレクトボックス'+str( dt_now.microsecond ),
                    'add_option' : 'select_box'+str( dt_now.microsecond ),
                    'add_type' : 'セレクトボックス',
                    'add_display' : '',
                    'add_required' : '',
                    'add_dropdown_value' : ''
                }
            }
     

        check_element_lists = ['add_display', 'add_checked_default']
        skip_elements = ['add_dropdown_value', 'add_checked_value']

        for input_name,input_value in target_element.items():
            for name,set_value in input_value.items():

                try:
                    target_input_element = self.driver_func.get_element_by_name( name )
                except NoSuchElementException:
                    continue

                if( name == 'add_type' ) :
                    #セレクトボックスの処理
                    self.driver_func.set_select_item( target_input_element, set_value )

                elif( name in check_element_lists ) :
                    #チェックボックスの処理
                    self.driver_func.click_item( target_input_element )

                elif( name in skip_elements ) :
                    #スキップする処理
                    continue

                else :
                    #普通に値を入力。
                    self.driver_func.put_item_info( target_input_element, set_value )


            filed_btn = '//table/tfoot/tr/td[@class="pt20"]/input[@id="add_field"][@value="フィールド追加"]'
            submit_btn = self.driver_func.get_element_by_xpath( filed_btn )
            self.driver_func.click_item( submit_btn )












