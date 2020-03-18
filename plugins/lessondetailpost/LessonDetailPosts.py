from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from plugins.driver.DriverAction import Driver_Action
from plugins.xpath.AdminMenuPath import Admin_Menu_Path
from plugins.basic.basic import Basic
import time
import datetime

class Lesson_Detail_Posts:

    def __init__(self, driver):
        self.chrome = driver
        self.driver_func = Driver_Action( driver )
        self.admin_xpath_list_func = Admin_Menu_Path()
        self.basic_func = Basic()
        self.admin_xpath_lists_xpath = self.admin_xpath_list_func.get_admin_menu_xpath()
        self.admin_list_parts_xpath = self.admin_xpath_list_func.get_admin_menu_list_parts_xpath()
        self.admin_parts_xpath = self.admin_xpath_list_func.get_admin_parts()

    def add_lesson_detail_page(self):
        #ポストのタイトル、テキストのディレクトリ、カテゴリー名、アイキャッチ画像
        base_dir = self.basic_func.get_base_dir_path()
        lesson_details = {
            'beginner_lesson_details' : {
                'first_lesson_details' : {
                    'post_title' : '英語文法(初級講座)',
                    'category_name' : '英語初級講座',
                    'text_dir' : base_dir+'/assets/texts/beginner/english-beginner-grammer.txt',
                    'img_dir' : base_dir+'/assets/img/beginner/english-beginner-grammer.png'
                },
                'second_lesson_details' : {
                    'post_title' : '英語リスニング(初級講座)',
                    'category_name' : '英語初級講座',
                    'text_dir' : base_dir+'/assets/texts/beginner/english-beginner-listening.txt',
                    'img_dir' : base_dir+'/assets/img/beginner/english-beginner-listening.png'
                },
                'third_lesson_details' : {
                    'post_title' : '英語リーディング(初級講座)',
                    'category_name' : '英語初級講座',
                    'text_dir' : base_dir+'/assets/texts/beginner/english-beginner-reading.txt',
                    'img_dir' : base_dir+'/assets/img/beginner/english-beginner-reading.png'
                },
                'fourth_lesson_details' : {
                    'post_title' : '英語スピーキング(初級講座)',
                    'category_name' : '英語初級講座',
                    'text_dir' : base_dir+'/assets/texts/beginner/english-beginner-speaking.txt',
                    'img_dir' : base_dir+'/assets/img/beginner/english-beginner-speaking.png'
                },
                'fifth_lesson_details' : {
                    'post_title' : '英語単語(初級講座)',
                    'category_name' : '英語初級講座',
                    'text_dir' : base_dir+'/assets/texts/beginner/english-beginner-words.txt',
                    'img_dir' : base_dir+'/assets/img/beginner/english-beginner-words.png'
                }
            },
            'normal_lesson_details' : {
                'first_lesson_details' : {
                    'post_title' : '英語文法(中級講座)',
                    'category_name' : '英語中級講座',
                    'text_dir' : base_dir+'/assets/texts/normal/english-normal-grammer.txt',
                    'img_dir' : base_dir+'/assets/img/normal/english-normal-grammer.png'
                },
                'second_lesson_details' : {
                    'post_title' : '英語リスニング(中級講座)',
                    'category_name' : '英語中級講座',
                    'text_dir' : base_dir+'/assets/texts/normal/english-normal-listening.txt',
                    'img_dir' : base_dir+'/assets/img/normal/english-normal-listening.png'
                },
                'third_lesson_details' : {
                    'post_title' : '英語リーディング(中級講座)',
                    'category_name' : '英語中級講座',
                    'text_dir' : base_dir+'/assets/texts/normal/english-normal-reading.txt',
                    'img_dir' : base_dir+'/assets/img/normal/english-normal-reading.png'
                },
                'fourth_lesson_details' : {
                    'post_title' : '英語スピーキング(中級講座)',
                    'category_name' : '英語中級講座',
                    'text_dir' : base_dir+'/assets/texts/normal/english-normal-speaking.txt',
                    'img_dir' : base_dir+'/assets/img/normal/english-normal-speaking.png'
                },
                'fifth_lesson_details' : {
                    'post_title' : '英語単語(中級講座)',
                    'category_name' : '英語中級講座',
                    'text_dir' : base_dir+'/assets/texts/normal/english-normal-words.txt',
                    'img_dir' : base_dir+'/assets/img/normal/english-normal-words.png'
                }
            },
            'advanced_lesson_details' : {
                'first_lesson_details' : {
                    'post_title' : '英語文法(上級講座)',
                    'category_name' : '英語上級講座',
                    'text_dir' : base_dir+'/assets/texts/advanced/english-advanced-grammer.txt',
                    'img_dir' : base_dir+'/assets/img/advanced/english-advanced-grammer.png'
                },
                'second_lesson_details' : {
                    'post_title' : '英語リスニング(上級講座)',
                    'category_name' : '英語上級講座',
                    'text_dir' : base_dir+'/assets/texts/advanced/english-advanced-listening.txt',
                    'img_dir' : base_dir+'/assets/img/advanced/english-advanced-listening.png'
                },
                'third_lesson_details' : {
                    'post_title' : '英語リーディング(上級講座)',
                    'category_name' : '英語上級講座',
                    'text_dir' : base_dir+'/assets/texts/advanced/english-advanced-reading.txt',
                    'img_dir' : base_dir+'/assets/img/advanced/english-advanced-reading.png'
                },
                'fourth_lesson_details' : {
                    'post_title' : '英語スピーキング(上級講座)',
                    'category_name' : '英語上級講座',
                    'text_dir' : base_dir+'/assets/texts/advanced/english-advanced-speaking.txt',
                    'img_dir' : base_dir+'/assets/img/advanced/english-advanced-speaking.png'
                },
                'fifth_lesson_details' : {
                    'post_title' : '英語単語(上級講座)',
                    'category_name' : '英語上級講座',
                    'text_dir' : base_dir+'/assets/texts/advanced/english-advanced-words.txt',
                    'img_dir' : base_dir+'/assets/img/advanced/english-advanced-words.png'
                }
            }
        }

        #for list_loop_name,lesson_details_lists in lesson_overview.items():

        for details_item_name, details_item_value in lesson_details.items():
            for list_name,lesson_details_lists in details_item_value.items():
                self.create_new_lesson_detail_page( lesson_details_lists )

    def create_new_lesson_detail_page( self, lesson_details_lists ):

        #要素を取得するためのXpathのリストを準備
        lesson_list_path = self.admin_xpath_lists_xpath['admin_guild_press_lesson_detail_list_page_path']
        add_new_lesson_list_path = self.admin_list_parts_xpath['add_new_page']

        #Xpathで、各要素を取得
        publish_post_btn = self.admin_parts_xpath['publish_post_btn']

        add_new_element = self.driver_func.get_element_by_xpath( add_new_lesson_list_path )

        #新規追加をクリックして、移動。
        self.driver_func.click_item(add_new_element)

        self.put_contents( lesson_details_lists )

        self.upload_img( lesson_details_lists )

        self.upload_thumbnail( lesson_details_lists )


        #公開ボタンを押す。
        self.driver_func.click_publish_btn()

        self.driver_func.stop(3)

        #一度他のページへ移動
        self.driver_func.move_admin_page( self.admin_xpath_lists_xpath['admin_main_setting_path'], self.admin_xpath_lists_xpath['admin_sub_setting_path'] )

        self.driver_func.move_admin_page( self.admin_xpath_lists_xpath['admin_guild_press_lesson_detail_page_path'], self.admin_xpath_lists_xpath['admin_guild_press_lesson_detail_list_page_path'] )

    def put_contents( self, lesson_details_lists ):
        #各要素を取得して、入力していく。
        post_title_element = self.driver_func.get_element_by_name( 'post_title' )
        self.driver_func.put_item_info( post_title_element, lesson_details_lists['post_title'] )

        #コンテンツを詰める
        content_html = self.driver_func.get_element_by_id('content-html')

        if( not content_html.is_selected() ) :
            self.driver_func.click_item( content_html )

        content_box_element = self.driver_func.get_element_by_name( 'content' )
        content_text = self.basic_func.get_file_text( lesson_details_lists['text_dir'] )
        self.driver_func.put_item_info( content_box_element, content_text )

        self.check_category_box( lesson_details_lists['category_name'] )


    def upload_img( self, lesson_details_lists ):
        media_input_file = self.admin_parts_xpath['media_input_file']

         #メディアを入れるためにボタンをクリックする。
        media_btn_html = self.driver_func.get_element_by_id('insert-media-button')
        self.driver_func.click_item( media_btn_html )

        #画像をアップロード
        img_btn_element = self.driver_func.get_element_by_xpath( media_input_file )
        self.driver_func.put_item_info( img_btn_element, lesson_details_lists['img_dir'] )


        #アップロードした後しばらく待つ。
        self.is_click_media_submit_btn()


    def is_click_media_submit_btn( self ):
        media_submit_btn = self.admin_parts_xpath['media_submit_btn']

        self.driver_func.stop(0.5)
        img_submit_element = self.driver_func.get_element_by_xpath( media_submit_btn )

        if( img_submit_element.is_enabled() ):
            self.driver_func.click_item( img_submit_element )

        else :
            self.is_click_media_submit_btn()


    def upload_thumbnail( self, lesson_details_lists ):
        media_input_file = self.admin_parts_xpath['media_input_file']
        media_add_eye_catch_btn = self.admin_parts_xpath['media_add_eye_catch_btn']
        #サムネイルを入れるためにボタンをクリックする。
        media_btn_html = self.driver_func.get_element_by_xpath( media_add_eye_catch_btn )
        self.driver_func.click_item( media_btn_html )

        #画像をアップロード
        img_btn_element = self.driver_func.get_element_by_xpath( media_input_file )
        self.driver_func.put_item_info( img_btn_element, lesson_details_lists['img_dir'] )

        #アップロードした後しばらく待つ。
        self.is_click_thumbnail_submit_btn()



    def is_click_thumbnail_submit_btn( self ):
        media_eye_catch_submit_btn = self.admin_parts_xpath['media_eye_catch_submit_btn']

        self.driver_func.stop(0.5)
        eye_chactch_submit_element = self.driver_func.get_element_by_xpath( media_eye_catch_submit_btn )

        if( eye_chactch_submit_element.is_enabled() ):
            print('is_click_thumbnail_submit_btn')
            self.driver_func.click_item( eye_chactch_submit_element )

        else :
            print('no is_click_thumbnail_submit_btn')
            self.is_click_thumbnail_submit_btn()





    def check_category_box( self, tareget_text ):

        cat_lists = '//ul[@id="guild_lesson_categorychecklist"]/li'
        cat_lists_check_box = '//ul[@id="guild_lesson_categorychecklist"]/li/label/input'

        category_list_element = self.driver_func.get_elements_by_xpath( cat_lists )
        category_box_element = self.driver_func.get_elements_by_xpath( cat_lists_check_box )

        for element, checkbox in zip( category_list_element, category_box_element ) :
            text = element.text

            if( text == tareget_text and not checkbox.is_selected() ):
                checkbox.click()











