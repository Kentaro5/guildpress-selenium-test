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

class Admin_Member_Rank:

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


    def check_lesson_detail_block_page(self):
        all_lesson_list = self.public_parts_xpath['all_lesson_list_xpath']
        all_lesson_list_link = self.public_parts_xpath['all_lesson_list_link_xpath']

        self.driver_func.stop(2)
        all_lesson_lists_elem = self.driver_func.get_elements_by_xpath( all_lesson_list )
        all_lesson_lists_link_elem = self.driver_func.get_elements_by_xpath( all_lesson_list_link )
        #概要ページから該当する名前順にリンクの要素を取得
        link_elem = self.basic_func.get_target_link_element( all_lesson_lists_elem, all_lesson_lists_link_elem, '英語上級講座' )

        #リンクを取得
        lesson_detail_link = self.driver_func.get_link( link_elem )

        #リンクに飛ぶ
        self.driver_func.move_to_page_by_link( self.chrome, lesson_detail_link )

    def go_to_lesson_list_page( self ):
        self.driver_func.go_to_public_nav_menu( '動画一覧ページ' )



    def add_admin_rank( self ):

        add_member_items = [
            'ゴールド会員',
            'シルバー会員',
            'ブロンズ会員',
            '無料会員'
        ]

        parent_add_member_items = [
            'ゴールド会員',
            'シルバー会員',
            'ブロンズ会員',
            '無料会員'
        ]

        member_rank_lists = self.admin_list_parts_xpath['add_member_ranks_xpath']
        member_ranks = self.driver_func.get_elements_by_xpath( member_rank_lists )

        print( len( member_ranks ) )

        if( len( member_ranks )  == 0 ) :
            for add_member_text in add_member_items:
                self.add_member_rank_info( add_member_text )

        else :

            for i, add_member_item in enumerate( add_member_items ) :

                try:
                    add_member_text = member_ranks[i].text
                except Exception as e:
                    pass
                else:
                    if( member_ranks[i].text in add_member_items ):
                        parent_add_member_items.remove( member_ranks[i].text )

            for add_member_text in parent_add_member_items:
                self.add_member_rank_info( add_member_text )


    def add_member_rank_info( self, add_member_text ):
        #新規登録ページに移動する。
        self.go_to_add_new_member_rank_page()

        member_rank_name_elem = self.driver_func.get_element_by_name( 'member_rank_name' )
        self.driver_func.put_item_info( member_rank_name_elem, add_member_text )

        submit_btn_elem = self.driver_func.get_element_by_name( 'submit' )
        self.driver_func.click_item( submit_btn_elem )


    def go_to_add_new_member_rank_page( self ):
        #固定ページの中から、新規登録ページに移動する。
        self.driver_func.single_move_admin_page( self.admin_list_parts_xpath['add_new_rank_page'] )


    def go_to_current_admin_menu_page( self ):
        #固定ページの中から、新規登録ページに移動する。
        self.driver_func.single_move_admin_page( self.admin_parts_xpath['guild_press_current_menu_xpath'] )


    def add_block_setting_overview_page( self ):

        page_list_xpath = self.admin_parts_xpath['page_list_xpath']
        page_lists_elem = self.driver_func.get_elements_by_xpath( page_list_xpath )
        check_box_xpath = self.admin_parts_xpath['guild_press_page_block_check_box_xpath']
        radio_btn_xpath = self.admin_parts_xpath['guild_press_page_block_radio_btn_xpath']
        label_xpath = self.admin_parts_xpath['guild_press_page_block_label_xpath']
        update_post_btn_xpath = self.admin_parts_xpath['update_post_btn']

        advance_overview_elem = self.basic_func.get_target_element( page_lists_elem, '英語上級講座' )
        self.driver_func.click_item( advance_overview_elem )

        guild_press_page_block_elem = self.driver_func.get_element_by_xpath( radio_btn_xpath )
        self.driver_func.scroll_down( self.chrome )
        self.driver_func.click_item( guild_press_page_block_elem )

        block_check_elem = self.driver_func.get_elements_by_xpath( check_box_xpath )
        label_elem = self.driver_func.get_elements_by_xpath( label_xpath )

        link_elem = self.basic_func.get_target_link_element( label_elem, block_check_elem, 'ゴールド会員' )
        self.driver_func.click_item( link_elem )

        update_post_btn_elem = self.driver_func.get_element_by_xpath( update_post_btn_xpath )
        self.driver_func.submit( update_post_btn_elem )


    def reset_block_setting_overview_page( self ):
        page_list_xpath = self.admin_parts_xpath['page_list_xpath']
        page_lists_elem = self.driver_func.get_elements_by_xpath( page_list_xpath )
        radio_btn_xpath = self.admin_parts_xpath['guild_press_page_non_block_radio_btn_xpath']
        update_post_btn_xpath = self.admin_parts_xpath['update_post_btn']

        advance_overview_elem = self.basic_func.get_target_element( page_lists_elem, '英語上級講座' )
        self.driver_func.click_item( advance_overview_elem )

        self.driver_func.scroll_down(self.chrome)

        guild_press_page_block_elem = self.driver_func.get_element_by_xpath( radio_btn_xpath )
        self.driver_func.click_item( guild_press_page_block_elem )

        update_post_btn_elem = self.driver_func.get_element_by_xpath( update_post_btn_xpath )
        self.driver_func.submit( update_post_btn_elem )


    #詳細ページに会員ランクを設定する
    def add_block_setting_detail_page( self ):

        page_list_xpath = self.admin_parts_xpath['page_list_xpath']
        check_box_xpath = self.admin_parts_xpath['guild_press_page_block_check_box_xpath']
        radio_btn_xpath = self.admin_parts_xpath['guild_press_page_block_radio_btn_xpath']
        label_xpath = self.admin_parts_xpath['guild_press_page_block_label_xpath']
        update_post_btn_xpath = self.admin_parts_xpath['update_post_btn']

        block_page_list = [
            '英語リスニング(初級講座)',
            '英語スピーキング(初級講座)',
            '英語スピーキング(上級講座)',
            '英語リスニング(上級講座)',
            ]
        for block_page_text in block_page_list:

            #一覧ページから、指定したレッスン詳細のリンクを取得。
            page_lists_elem = self.driver_func.get_elements_by_xpath( page_list_xpath )
            advance_detail_elem = self.basic_func.get_target_element( page_lists_elem, block_page_text )
            self.driver_func.click_item( advance_detail_elem )

            self.driver_func.scroll_down( self.chrome )

            #ラジオボタンでページブロックを選択
            guild_press_page_block_elem = self.driver_func.get_element_by_xpath( radio_btn_xpath )
            self.driver_func.click_item( guild_press_page_block_elem )

            #ラベル一覧を取得して、ゴールド会員にチェックを入れる。
            block_check_elem = self.driver_func.get_elements_by_xpath( check_box_xpath )
            label_elem = self.driver_func.get_elements_by_xpath( label_xpath )

            link_elem = self.basic_func.get_target_link_element( label_elem, block_check_elem, 'ゴールド会員' )
            self.driver_func.click_item( link_elem )
            update_post_btn_elem = self.driver_func.get_element_by_xpath( update_post_btn_xpath )
            self.driver_func.submit( update_post_btn_elem )

            self.driver_func.stop(3)

            #レッスン詳細一覧ページへ戻る。
            self.go_to_current_admin_menu_page()


    def reset_block_setting_detail_page( self ):
        page_list_xpath = self.admin_parts_xpath['page_list_xpath']

        radio_btn_xpath = self.admin_parts_xpath['guild_press_page_non_block_radio_btn_xpath']
        update_post_btn_xpath = self.admin_parts_xpath['update_post_btn']

        block_page_list = [
            '英語リスニング(初級講座)',
            '英語スピーキング(初級講座)',
            '英語スピーキング(上級講座)',
            '英語リスニング(上級講座)',
            ]
        for block_page_text in block_page_list:

            page_lists_elem = self.driver_func.get_elements_by_xpath( page_list_xpath )

            advance_detail_elem = self.basic_func.get_target_element( page_lists_elem, block_page_text )
            self.driver_func.click_item( advance_detail_elem )

            self.driver_func.scroll_half_down(self.chrome)

            guild_press_page_block_elem = self.driver_func.get_element_by_xpath( radio_btn_xpath )
            self.driver_func.click_item( guild_press_page_block_elem )

            update_post_btn_elem = self.driver_func.get_element_by_xpath( update_post_btn_xpath )
            self.driver_func.submit( update_post_btn_elem )

            self.driver_func.stop(3)

            #レッスン詳細一覧ページへ戻る。
            self.go_to_current_admin_menu_page()






