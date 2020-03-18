from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import datetime

class Pay_Pal_Add_New_One:

    def __init__(self, driver):
        self.chrome = driver

    def go_to_pay_pal_register_page( self ):
        add_new_one_xpath = '//div[@id="wpbody"]/div[@id="wpbody-content"]/div[@class="wrap"]/a[@class="add-new-h2"][text()="新規追加"]'

        registeadd_new_btn = self.chrome.find_element_by_xpath( add_new_one_xpath )
        registeadd_new_btn.click()

    #普通に登録
    def add_normal_subscription_payment( self ):

        dt_now = datetime.datetime.now()

        target_element = {
            'post_title' : 'PayPal_Test'+str( dt_now.microsecond ),
            'paypal_address' : 'メールアドレス記載',
            'submit_btn_text' : 'paypalnormalボタン',
            'amount' : '333',
            'currency' : '日本円',
            'currency_symbol' : '円',
            'sandbox' : '',
            'paypal_lang' : '日本語',
            'item_name' : 'paypalテスト商品',
            'payment' : '継続課金',
            'member_rank' : '会員ランクを選択してください。',
            'payment_period' : '終了しない',
            'payment_cycle_number' : '1',
            'payment_cycle' : '日間',
            }

        select_element_lists = ['currency', 'paypal_lang', 'payment', 'member_rank']
        check_element_lists = ['sandbox']

        for key,value in target_element.items():

            try:
                paypal_input = self.chrome.find_element_by_name(key)
            except NoSuchElementException:
                continue

            if( key in select_element_lists ) :

                # 取得したエレメントをSelectタグに対応したエレメントに変化させる
                setting_select_element = Select( paypal_input )

                # 選択したいvalueを指定する
                setting_select_element.select_by_visible_text( value )

            elif( key in check_element_lists ) :

                if( paypal_input.is_selected() ) :

                    return
                else :
                    #要素をチェックする。
                    paypal_input.click()

            else :
                paypal_input.send_keys( value )

        submit_input = self.chrome.find_element_by_name('submit')
        submit_input.click()

    #　会員ランクを追加するバージョン
    def add_member_subscription_payment( self ):

        dt_now = datetime.datetime.now()

        target_element = {
                'post_title' : 'PayPal_Test_ゴールド会員'+str( dt_now.microsecond ),
                'paypal_address' : 'メールアドレス記載',
                'submit_btn_text' : 'paypalmemberボタン',
                'amount' : '333',
                'currency' : '日本円',
                'currency_symbol' : '円',
                'sandbox' : '',
                'paypal_lang' : '日本語',
                'item_name' : 'paypalテスト商品',
                'payment' : '継続課金',
                'member_rank' : 'ゴールド会員',
                'payment_period' : '終了しない',
                'payment_cycle_number' : '1',
                'payment_cycle' : '日間',
        }

        select_element_lists = ['currency', 'paypal_lang', 'payment', 'member_rank']
        check_element_lists = ['sandbox']

        for key,value in target_element.items():

            try:
                paypal_input = self.chrome.find_element_by_name(key)
            except NoSuchElementException:
                continue

            if( key in select_element_lists ) :

                # 取得したエレメントをSelectタグに対応したエレメントに変化させる
                setting_select_element = Select( paypal_input )

                # 選択したいvalueを指定する
                setting_select_element.select_by_visible_text( value )

            elif( key in check_element_lists ) :

                if( paypal_input.is_selected() ) :

                    return
                else :
                    #要素をチェックする。
                    paypal_input.click()

            else :
                paypal_input.send_keys( value )

        submit_input = self.chrome.find_element_by_name('submit')
        submit_input.click()

        return target_element['post_title']
















