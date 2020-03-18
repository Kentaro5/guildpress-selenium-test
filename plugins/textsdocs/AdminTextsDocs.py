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

class Admin_Texts_Docs:

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

        #ユーザー画面内の項目に関するパス
        self.public_parts_xpath = self.admin_xpath_list_func.get_public_parts()

        self.base_dir = self.basic_func.get_base_dir_path()


    def add_texts_docs_info( self ):

        texts_docs_lists = {
            'beginner_texts_docs' : {
                'first_texts_docs' : {
                    'text_title' : '英語文法(初級講座)教材',
                    'category_name' : '英語初級講座',
                    'img_dir' : self.base_dir+'/assets/texts_docs/english-grammer.pdf',
                    'page_block' : '2'
                },
                'second_texts_docs' : {
                    'text_title' : '英語リスニング(初級講座)教材',
                    'category_name' : '英語初級講座',
                    'img_dir' : self.base_dir+'/assets/texts_docs/english-listening.pdf',
                    'page_block' : '1'
                },
                'third_texts_docs' : {
                    'text_title' : '英語リーディング(初級講座)教材',
                    'category_name' : '英語初級講座',
                    'img_dir' : self.base_dir+'/assets/texts_docs/english-reading.pdf',
                    'page_block' : '2'
                },
                'fourth_texts_docs' : {
                    'text_title' : '英語スピーキング(初級講座)教材',
                    'category_name' : '英語初級講座',
                    'img_dir' : self.base_dir+'/assets/texts_docs/english-speaking.pdf',
                    'page_block' : '2'
                },
                'fifth_texts_docs' : {
                    'text_title' : '英語単語(初級講座)教材',
                    'category_name' : '英語初級講座',
                    'img_dir' : self.base_dir+'/assets/texts_docs/english-words.pdf',
                    'page_block' : '1'
                }
            },
            'normal_texts_docs' : {
                'first_texts_docs' : {
                    'text_title' : '英語文法(中級講座)教材',
                    'category_name' : '英語中級講座',
                    'img_dir' : self.base_dir+'/assets/texts_docs/english-grammer.pdf',
                    'page_block' : '2'
                },
                'second_texts_docs' : {
                    'text_title' : '英語リスニング(中級講座)教材',
                    'category_name' : '英語中級講座',
                    'img_dir' : self.base_dir+'/assets/texts_docs/english-listening.pdf',
                    'page_block' : '1'
                },
                'third_texts_docs' : {
                    'text_title' : '英語リーディング(中級講座)教材',
                    'category_name' : '英語中級講座',
                    'img_dir' : self.base_dir+'/assets/texts_docs/english-reading.pdf',
                    'page_block' : '2'
                },
                'fourth_texts_docs' : {
                    'text_title' : '英語スピーキング(中級講座)教材',
                    'category_name' : '英語中級講座',
                    'img_dir' : self.base_dir+'/assets/texts_docs/english-speaking.pdf',
                    'page_block' : '2'
                },
                'fifth_texts_docs' : {
                    'text_title' : '英語単語(中級講座)教材',
                    'category_name' : '英語中級講座',
                    'img_dir' : self.base_dir+'/assets/texts_docs/english-words.pdf',
                    'page_block' : '1'
                }
            },
            'advanced_texts_docs' : {
                'first_texts_docs' : {
                    'text_title' : '英語文法(上級講座)教材',
                    'category_name' : '英語上級講座',
                    'img_dir' : self.base_dir+'/assets/texts_docs/english-grammer.pdf',
                    'page_block' : '2'
                },
                'second_texts_docs' : {
                    'text_title' : '英語リスニング(上級講座)教材',
                    'category_name' : '英語上級講座',
                    'img_dir' : self.base_dir+'/assets/texts_docs/english-listening.pdf',
                    'page_block' : '1'
                },
                'third_texts_docs' : {
                    'text_title' : '英語リーディング(上級講座)教材',
                    'category_name' : '英語上級講座',
                    'img_dir' : self.base_dir+'/assets/texts_docs/english-reading.pdf',
                    'page_block' : '2'
                },
                'fourth_texts_docs' : {
                    'text_title' : '英語スピーキング(上級講座)教材',
                    'category_name' : '英語上級講座',
                    'img_dir' : self.base_dir+'/assets/texts_docs/english-speaking.pdf',
                    'page_block' : '2'
                },
                'fifth_texts_docs' : {
                    'text_title' : '英語単語(上級講座)教材',
                    'category_name' : '英語上級講座',
                    'img_dir' : self.base_dir+'/assets/texts_docs/english-words.pdf',
                    'page_block' : '1'
                }
            }
        }

        texts_docs_lists_test = {
            'beginner_texts_docs' : {
                'first_texts_docs' : {
                    'text_title' : '英語文法(初級講座)教材',
                    'category_name' : '英語初級講座',
                    'img_dir' : self.base_dir+'/assets/texts_docs/english-grammer.pdf',
                    'page_block' : '2'
                },
            }
        }

        for texts_docs_lists_name, texts_docs_lists_value in texts_docs_lists.items():
            for list_name,text_docs_lists in texts_docs_lists_value.items():
                self.add_info( text_docs_lists )


    def add_info( self, text_docs_lists ) :

        new_btn_xpath = self.admin_list_parts_xpath['add_new_texts_page']
        submit_btn_xpath = self.admin_parts_xpath['guild_press_text_docs_submit_xpath']

        new_btn_elem = self.driver_func.get_element_by_xpath( new_btn_xpath )
        self.driver_func.click_item( new_btn_elem )

        post_title_elem = self.driver_func.get_element_by_name( 'gp_post_title' )
        self.driver_func.put_item_info( post_title_elem, text_docs_lists['text_title'] )

        self.upload_texts_docs( text_docs_lists )

        self.add_category( text_docs_lists )

        submit_btn_element = self.driver_func.get_element_by_xpath( submit_btn_xpath )
        self.driver_func.click_item( submit_btn_element )

    def add_category( self, text_docs_lists ):
        radio_btn_xpath = self.admin_parts_xpath['guild_press_text_docs_rank_block_xpath']
        check_box_xpath = self.admin_parts_xpath['guild_press_text_docs_rank_check_box_xpath']
        label_xpath = self.admin_parts_xpath['guild_press_text_docs_rank_label_xpath']

        texts_docs_btn_elem = self.driver_func.get_element_by_name( 'gp_lesson_category' )
        self.driver_func.set_select_item( texts_docs_btn_elem, text_docs_lists['category_name'] )

        if( text_docs_lists['page_block'] == '2' ):
            guild_press_page_block_elem = self.driver_func.get_element_by_xpath( radio_btn_xpath )
            self.driver_func.click_item( guild_press_page_block_elem )

            block_check_elem = self.driver_func.get_elements_by_xpath( check_box_xpath )
            label_elem = self.driver_func.get_elements_by_xpath( label_xpath )

            link_elem = self.basic_func.get_target_link_element( label_elem, block_check_elem, 'ゴールド会員' )
            self.driver_func.click_item( link_elem )


        elif( text_docs_lists['page_block'] == '1' ):
            pass

    def upload_texts_docs( self, text_docs_lists ):

        texts_docs_btn_elem = self.driver_func.get_element_by_name( 'csv' )
        self.driver_func.click_item( texts_docs_btn_elem )

        media_input_file = self.admin_parts_xpath['media_input_file']
        #画像をアップロード
        img_btn_element = self.driver_func.get_element_by_xpath( media_input_file )
        self.driver_func.put_item_info( img_btn_element, text_docs_lists['img_dir'] )

        #教材のアップロードが完了できているかチェックする、
        self.is_click_media_submit_btn()
        

    def is_click_media_submit_btn( self ):
        texts_docs_submit_btn = self.admin_parts_xpath['texts_docs_submit_btn']

        self.driver_func.stop(2)
        img_submit_element = self.driver_func.get_element_by_xpath( texts_docs_submit_btn )

        if( img_submit_element.is_enabled() ):
            self.driver_func.click_item( img_submit_element )

        else :
            self.is_click_media_submit_btn()



    def get_dwd_show_shortcode( self ) :
        show_short_code_xpath = self.admin_parts_xpath['guild_press_text_docs_show_shortcode_xpath']
        dwd_short_code_xpath = self.admin_parts_xpath['guild_press_text_docs_dwd_shortcode_xpath']

        show_short_elem = self.driver_func.get_element_by_xpath( show_short_code_xpath )
        dwd_short_elem = self.driver_func.get_element_by_xpath( dwd_short_code_xpath )

        short_codes = {
            'show_shortcode' : show_short_elem.text,
            'dwd_shortcode' : dwd_short_elem.text,
        }

        return short_codes


    def put_short_codes_to_lesson_detail( self, texts_docs_shortcodes ):

        show_shortcode = texts_docs_shortcodes['show_shortcode']
        dwd_shortcode = texts_docs_shortcodes['dwd_shortcode']

        first_lesson_detail_xpath = self.admin_parts_xpath['guild_press_first_lesson_detail']
        first_lesson_detail_elem = self.driver_func.get_element_by_xpath( first_lesson_detail_xpath )

        self.driver_func.click_item( first_lesson_detail_elem )

        content_elem = self.driver_func.get_element_by_name( 'content' )

        #テキストエリアのテキストを改行でリスト方にする。
        content_texts = content_elem.text.splitlines()
        last_index = len(content_texts) - 1
        
        content_texts[last_index] = show_shortcode+'\n'+dwd_shortcode+'\n'+content_texts[last_index]
        
        self.driver_func.clear_item_info( content_elem )

        for content_text in content_texts:
            self.driver_func.put_item_info( content_elem, content_text+'\n' )

        # update_post_btn_xpath = self.admin_parts_xpath['update_post_btn']
        # update_post_btn_elem = self.driver_func.get_element_by_xpath( update_post_btn_xpath )
        # self.driver_func.click_item( update_post_btn_elem )

        self.driver_func.click_update_btn()

        #貼り付けたショートコードの確認
        self.go_to_short_codes_page()
        

    def go_to_short_codes_page( self ):
        
        post_permalink_xpath = self.admin_parts_xpath['post_permalink']
        post_permalink_elem = self.driver_func.get_element_by_xpath( post_permalink_xpath )
        self.driver_func.click_item( post_permalink_elem )

        # スクールダウンして表示を確認する。
        self.driver_func.scroll_down( self.chrome )

        dwd_btn_xpath = self.public_parts_xpath['dwd_btn_xpath']
        dwd_btn_elem = self.driver_func.get_element_by_xpath( dwd_btn_xpath )

        self.driver_func.click_item(dwd_btn_elem)
        

















