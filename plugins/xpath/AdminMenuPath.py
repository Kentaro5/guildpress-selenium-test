class Admin_Menu_Path:

    def __init__(self):

        self.admin_menu_xpaths = {
            'admin_main_setting_path' : '//div[@class="wp-menu-image dashicons-before dashicons-admin-settings"]',

            'admin_sub_setting_path' : '//div[@id="adminmenuwrap"]/ul[@id="adminmenu"]/li[@id="menu-settings"]/ul[@class="wp-submenu wp-submenu-wrap"]/li[@class="wp-first-item"]/a[@class="wp-first-item"][text()="一般"]',

            'admin_page_path' : '//div[@class="wp-menu-name"][text()="固定ページ"]',

            'admin_list_page_path' : '//ul[@id="adminmenu"]/li[@id="menu-pages"]/ul[@class="wp-submenu wp-submenu-wrap"]/li[@class="wp-first-item"]/a[@class="wp-first-item"][text()="固定ページ一覧"]',

            'admin_new_regsiter_page_path' : '//td[@class="title column-title has-row-actions column-primary page-title"]/strong/a[@class="row-title"][text()="新規登録ページ"]',

            'admin_go_to_mypage_path' : '//td[@class="title column-title has-row-actions column-primary page-title"]/strong/a[text()="マイぺージ"]',

            'admin_user_list_page_path' : '//div[@class="wp-menu-name"][text()="ユーザー"]',

            'admin_user_list_sub_page_path' : '//ul[@class="wp-submenu wp-submenu-wrap"]/li[@class="wp-first-item"]/a[@class="wp-first-item"][text()="ユーザー一覧"]',

            'admin_guild_press_page_path' : '//div[@class="wp-menu-name"][text()="GuildPress"]',

            'admin_guild_press_settings_page_path' : '//ul[@class="wp-submenu wp-submenu-wrap"]/li[@class="wp-first-item"]/a[@class="wp-first-item"][text()="GuildPress"]',

            'admin_guild_press_texts_docs_page_path' : '//ul[@class="wp-submenu wp-submenu-wrap"]/li[8]/a[text()="教材・資料一覧"]',


            'admin_guild_press_paypal_page_path' : '//ul[@class="wp-submenu wp-submenu-wrap"]/li[5]/a[text()="PayPal設定"]',

            'admin_guild_press_original_form_page_path' : '//ul[@class="wp-submenu wp-submenu-wrap"]/li[6]/a[text()="ユーザー登録フォーム項目"]',

            'admin_guild_press_member_rank_page_path' : '//ul[@id="adminmenu"]/li[@id="toplevel_page_guild_press_basic_setting"]/ul[@class="wp-submenu wp-submenu-wrap"]/li[7]/a[text()="会員ランク一覧"]',

            'admin_guild_press_lesson_over_view_page_path' : '//div[@class="wp-menu-name"][text()="レッスン一覧"]',

            'admin_guild_press_lesson_over_view_list_page_path' : '//ul[@class="wp-submenu wp-submenu-wrap"]/li[@class="wp-first-item"]/a[@class="wp-first-item"][text()="レッスン一覧"]',

            'admin_guild_press_lesson_detail_page_path' : '//div[@class="wp-menu-name"][text()="各レッスン登録"]',

            'admin_guild_press_lesson_detail_list_page_path' : '//ul[@class="wp-submenu wp-submenu-wrap"]/li[@class="wp-first-item"]/a[@class="wp-first-item"][text()="各レッスン登録"]',

            'admin_guild_press_lesson_calendar_page_path' : '//ul[@id="adminmenu"]/li[@id="toplevel_page_guild_press_basic_setting"]/ul[@class="wp-submenu wp-submenu-wrap"]/li[3]/a[text()="予約一覧"]',

            'admin_guild_press_lesson_calendar_page_path' : '//ul[@id="adminmenu"]/li[@id="toplevel_page_guild_press_basic_setting"]/ul[@class="wp-submenu wp-submenu-wrap"]/li[3]/a[text()="予約一覧"]',

        }

        self.admin_menu_list_parts_xpath = {

            'add_new_page' : '//div[@id="wpbody-content"]/div[@class="wrap"]/a[@class="page-title-action"][text()="新規追加"]',

            'add_new_rank_page' : '//div[@id="wpbody"]/div[@id="wpbody-content"]/div[@class="wrap"]/a[@class="add-new-h2"][text()="新規追加"]',

            'add_new_texts_page' : '//div[@id="wpbody-content"]/div[@class="wrap"]/a[@class="add-new-h2"][text()="新規追加"]',

            'add_member_ranks_xpath' : '//table[@class="wp-list-table widefat fixed striped posts"]/tbody[@id="the-list"]/tr/td[@class="member_rank column-member_rank"]',

        }


        self.admin_parts_xpath = {

            'img_upload_btn' : '//div[@class="upload-ui"]/button[@id="insert-media-button"][text()="メディアを追加"]',

            'media_input_file' : '//input[starts-with(@id,"html5_")]',

            'media_submit_btn' : '//div[@class="media-toolbar-primary search-form"]/button[@class="button media-button button-primary button-large media-button-insert"][text()="投稿に挿入"]',

            'texts_docs_submit_btn' : '//div[@class="media-toolbar-primary search-form"]/button[@class="button media-button button-primary button-large media-button-select"]',

            'media_add_eye_catch_btn' : '//div[@id="postimagediv"]/div[@class="inside"]/p[@class="hide-if-no-js"]/a[@id="set-post-thumbnail"][text()="アイキャッチ画像を設定"]',

            'media_eye_catch_submit_btn' : '//div[@class="media-toolbar-primary search-form"]/button[@class="button media-button button-primary button-large media-button-select"][text()="アイキャッチ画像を設定"]',

            'publish_post_btn' : '//div[@id="submitpost"]/div[@id="major-publishing-actions"]/div[@id="publishing-action"]/input[@id="publish"][@value="公開"]',

            'update_post_btn' : '//div[@id="publishing-action"]/input[@id="publish"]',

            'page_list_xpath' : '//tbody[@id="the-list"]/tr/td[@class="title column-title has-row-actions column-primary page-title"]/strong/a',

            'guild_press_tab_xpath' : '//div[@id="wpwrap"]/div[@id="wpcontent"]/div[@id="wpbody"]/div[@id="wpbody-content"]/div[@class="wrap"]/div[@id="guild_press_tabs"]/a',

            'guild_press_regsiter_link_xpath' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[5]/td[@class="calendar-box calender_cell tue"]/div[@class="reservation-view"]/a',

            'guild_press_setting_tab_xpath' : '//div[@class="wrap"]/div[@id="guild_press_tabs"]/a[@class="nav-tab "]',

            'guild_press_page_block_check_box_xpath' : '//div[@id="guild_press_member_list_box"]/p/input',

            'guild_press_page_block_label_xpath' : '//div[@id="guild_press_member_list_box"]/p/label',

            'guild_press_page_block_radio_btn_xpath' : '//div[@id="gp_page_block_box"]/div[@class="inside"]/p/input[@id="guild_press_page_block"]',

            'guild_press_page_non_block_radio_btn_xpath' : '//div[@id="gp_page_block_box"]/div[@class="inside"]/p/input[@id="guild_press_page_non_block"]',

            'guild_press_current_menu_xpath' : '//li[@class="wp-first-item current"]/a[@class="wp-first-item current"]',

            'guild_press_text_docs_rank_block_xpath' : '//div[@id="guild_press_add_new_member_rank_box"]/div[@class="inside"]/p/input[@id="guild_press_rank_check"]',

            'guild_press_text_docs_rank_check_box_xpath' : '//div[@class="inside"]/div[@id="guild_press_member_list_box"]/p/input[@id="guild_press_block_texts_docs_rank"]',

            'guild_press_text_docs_rank_label_xpath' : '//div[@class="inside"]/div[@id="guild_press_member_list_box"]/p/label',

            'guild_press_text_docs_submit_xpath' : '//div[@class="wrap"]/form/p[@class="submit"]/input[@id="submit"]',

            'guild_press_text_docs_show_shortcode_xpath' : '//table[@class="wp-list-table widefat fixed striped posts"]/tbody[@id="the-list"]/tr[1]/td[@class="show_short_code column-show_short_code"]',

            'guild_press_text_docs_dwd_shortcode_xpath' : '//table[@class="wp-list-table widefat fixed striped posts"]/tbody[@id="the-list"]/tr[1]/td[@class="dwd_short_code column-dwd_short_code"]',

            'guild_press_first_lesson_detail' : '//table[@class="wp-list-table widefat fixed striped posts"]/tbody[@id="the-list"]/tr/td[@class="title column-title has-row-actions column-primary page-title"]/strong/a[@class="row-title"]',

            'post_permalink' : '//div[@id="titlediv"]/div[@class="inside"]/div[@id="edit-slug-box"]/span[@id="sample-permalink"]/a',

            'page_lock_radio_xpath' : '//div[@id="gp_page_lock_box"]/div[@class="inside"]/p/input[@id="guild_press_page_lock"]',

            'current_page_btn_xpath' : '//ul[@class="wp-submenu wp-submenu-wrap"]/li[@class="wp-first-item current"]/a[@class="wp-first-item current"]',

            'current_page_btn_xpath' : '//ul[@class="wp-submenu wp-submenu-wrap"]/li[@class="wp-first-item current"]/a[@class="wp-first-item current"]',

            'quiz_btn_xpath' : '//div[@class="inside"]/p/input[@id="guild_press_page_quiz"]',

            'no_quiz_btn_xpath' : '//div[@class="inside"]/p/input[@id="guild_press_page_non_quiz"]',

            'quiz_textarea_xpath' : '//div[@id="gp_page_quiz_box"]/div[@class="inside"]/div[@id="guild_press_quiz_box"]/textarea',

            'quiz_first_input_xpath' : '//div[@id="guild_press_quiz_answer_texts"][1]/label[1]/input[@id="guild_press_quiz_answer_text"]',

            'quiz_input_xpath' : '//div[@id="guild_press_quiz_answer_texts"]/input[@id="guild_press_quiz_answer_text"]',

            'add_quiz_btn_xpath' : '//div[@id="guild_press_quiz_box"]/button[@id="guild_press_add_quiz_answer"]',

            'answer_radio_xpath' : '//div[@id="guild_press_quiz_answer_texts"]/input[@id="guild_press_quiz_correct_answer"]',

            'first_answer_radio_xpath' : '//div[@id="guild_press_quiz_answer_texts"]/label/input[@id="guild_press_quiz_correct_answer"]'


        }

        self.public_parts_xpath = {

            'menu_list_xpath' : '//ul[@id="menu-test"]/li/a',

            'nav_list_xpath' : '//ul[@class="nav navbar-nav"]/li/a',

            'all_lesson_list_xpath' : '//div[@class="col-xs-12 col-md-4 post-lists"]/a[@class="posts-lists-link"]/div[@class="single-post-box"]/div[@class="single-post-content"]/h2[@class="single-post-title"]',

            'all_lesson_list_link_xpath' : '//div[@class="col-xs-12 col-md-4 post-lists"]/a[@class="posts-lists-link"]',

            'first_lesson_link_xpath' : '//div[@id="lesson-list-box"]/a[@class="lesson_link"]',

            'lesson_detail_lists' : '//div[@id="lesson-list-box"]/a[@class="lesson_link"]',

            'lesson_comp_btn_xpath' : '//button[@id="lesson_comp"]',

            'lesson_next_btn_xpath' : '//button[@class="btn_design ml30"][text()="次のページへ"]',

            'calendar_cell_list_xpath' : '//div[@class="calendar-schedule-box"]/a[@id="pop_box"]',

            'calendar_cell_register_xpath' : '//div[@id="DOMWindow"]/div[@class="calendar-detail-box"]/div[@class="row calendar-edit-box"]/div[@class="col-md-12"]/p[@class="calendar-register-text"]/a',

            'calendar_cell_edit_xpath' : '//div[@id="DOMWindow"]/div[@class="calendar-detail-box"]/div[@class="row calendar-edit-box"]/div[@class="col-md-6"]/p[@class="calendar-edit-text"]/a',

            'all_lesson_title_list_xpath' : '//div[@class="lesson-list-detail-box"]/div[@class="row"]/div[@class="col-md-9 lesson-list-detail-desc-box"]/h2',

            'lesson_quiz_lists_xpath' : '//div[@class="row"]/section[@class="col-lg-12"]/div/label[@class="flexed"]/input[@id="gp_user_answer_text"]',

            'send_answer_xpath' : '//div[@id="respond"]/p[@class="form-submit"]/button[@id="send_quiz_answer_btn"]',

            'next_btn_xpath' : '//div[@id="lesson-list-box"]/div[@class="page-lesson-detail-box"]/div[@id="respond"][2]/p[@class="form-submit"]/button[@id="next_link_btn"]',

            'edit_btn_xpath' : '//div[@class="my-page-top"]/div[@class="center"]/a/button[@class="btn_design"][text()="情報を更新する"]',

            'dwd_btn_xpath' : '//div[@class="page-lesson-detail-box"]/a/div[@class="dwd_background"]'



        }

        self.get_google_calendar_api_xpath = {


        }


        self.get_many_calendar_parts_xpath = {

            'sun_day_first' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[2]/td[@class="calendar-box calender_cell sun"]/div[@class="reservation-view"]/a',

            'sun_day_second' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[3]/td[@class="calendar-box calender_cell sun"]/div[@class="reservation-view"]/a',

            'sun_day_third' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[4]/td[@class="calendar-box calender_cell sun"]/div[@class="reservation-view"]/a',

            'sun_day_fourth' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[5]/td[@class="calendar-box calender_cell sun"]/div[@class="reservation-view"]/a',

            'sun_day_last' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[6]/td[@class="calendar-box calender_cell sun"]/div[@class="reservation-view"]/a',

            'mon_day_first' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[2]/td[@class="calendar-box calender_cell mon"]/div[@class="reservation-view"]/a',

            'mon_day_second' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[3]/td[@class="calendar-box calender_cell mon"]/div[@class="reservation-view"]/a',

            'mon_day_third' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[4]/td[@class="calendar-box calender_cell mon"]/div[@class="reservation-view"]/a',

            'mon_day_fourth' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[5]/td[@class="calendar-box calender_cell mon"]/div[@class="reservation-view"]/a',

            'mon_day_last' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[6]/td[@class="calendar-box calender_cell mon"]/div[@class="reservation-view"]/a',

            'tues_day_first' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[2]/td[@class="calendar-box calender_cell tue"]/div[@class="reservation-view"]/a',

            'tues_day_second' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[3]/td[@class="calendar-box calender_cell tue"]/div[@class="reservation-view"]/a',

            'tues_day_third' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[4]/td[@class="calendar-box calender_cell tue"]/div[@class="reservation-view"]/a',

            'tues_day_fourth' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[5]/td[@class="calendar-box calender_cell tue"]/div[@class="reservation-view"]/a',

            'tues_day_last' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[6]/td[@class="calendar-box calender_cell tue"]/div[@class="reservation-view"]/a',

            'wednes_day_first' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[2]/td[@class="calendar-box calender_cell wed"]/div[@class="reservation-view"]/a',

            'wednes_day_second' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[3]/td[@class="calendar-box calender_cell wed"]/div[@class="reservation-view"]/a',

            'wednes_day_third' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[4]/td[@class="calendar-box calender_cell wed"]/div[@class="reservation-view"]/a',

            'wednes_day_fourth' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[5]/td[@class="calendar-box calender_cell wed"]/div[@class="reservation-view"]/a',

            'wednes_day_last' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[6]/td[@class="calendar-box calender_cell wed"]/div[@class="reservation-view"]/a',

            'thurs_day_first' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[2]/td[@class="calendar-box calender_cell thu"]/div[@class="reservation-view"]/a',

            'thurs_day_second' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[3]/td[@class="calendar-box calender_cell thu"]/div[@class="reservation-view"]/a',

            'thurs_day_third' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[4]/td[@class="calendar-box calender_cell thu"]/div[@class="reservation-view"]/a',

            'thurs_day_fourth' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[5]/td[@class="calendar-box calender_cell thu"]/div[@class="reservation-view"]/a',

            'thurs_day_last' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[6]/td[@class="calendar-box calender_cell thu"]/div[@class="reservation-view"]/a',

            'fly_day_first' : '//div[@class="inside"]/div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[2]/td[@class="calendar-box calender_cell fri"]/div[@class="reservation-view"]/a',

            'fly_day_second' : '//div[@class="inside"]/div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[3]/td[@class="calendar-box calender_cell fri"]/div[@class="reservation-view"]/a',

            'fly_day_third' : '//div[@class="inside"]/div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[4]/td[@class="calendar-box calender_cell fri"]/div[@class="reservation-view"]/a',

            'fly_day_fourth' : '//div[@class="inside"]/div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[5]/td[@class="calendar-box calender_cell fri"]/div[@class="reservation-view"]/a',

            'fly_day_last' : '//div[@class="inside"]/div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[6]/td[@class="calendar-box calender_cell fri"]/div[@class="reservation-view"]/a',

            'saturday_day_first' : '//div[@class="inside"]/div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[2]/td[@class="calendar-box calender_cell sat"]/div[@class="reservation-view"]/a',

            'saturday_day_second' : '//div[@class="inside"]/div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[3]/td[@class="calendar-box calender_cell sat"]/div[@class="reservation-view"]/a',

            'saturday_day_third' : '//div[@class="inside"]/div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[4]/td[@class="calendar-box calender_cell sat"]/div[@class="reservation-view"]/a',

            'saturday_day_fourth' : '//div[@class="inside"]/div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[5]/td[@class="calendar-box calender_cell sat"]/div[@class="reservation-view"]/a',

            'saturday_day_last' : '//div[@class="inside"]/div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[6]/td[@class="calendar-box calender_cell sat"]/div[@class="reservation-view"]/a',
        }
        """

        self.get_many_calendar_parts_xpath = {

            'sun_day_second' : '//div[@class="reservation-table"]/table[@class="calender_table"]/tbody/tr[3]/td[@class="calendar-box calender_cell sun"]/div[@class="reservation-view"]/a',
        }
        """


    # 管理画面のメニューのパスを返す
    def get_admin_menu_xpath(self):
        return self.admin_menu_xpaths


    # 管理画面メニュー内の新規追加や編集などのパーツのパスを返す。
    def get_admin_menu_list_parts_xpath(self):
        return self.admin_menu_list_parts_xpath


    # 管理画面内の項目に関するパス(作成した固定ページリストとか)
    def get_admin_parts(self):
        return self.admin_parts_xpath


    # GoogleカレンダーAPIの設定をする時に使用するパス(作成した固定ページリストとか)
    def get_google_calendar_api_parts(self):
        return self.get_google_calendar_api_xpath


    # GoogleカレンダーAPIの設定をする時に使用するパス(作成した固定ページリストとか)
    def get_public_parts(self):
        return self.public_parts_xpath


    # カレンダーページ(管理画面側)のパスを返す
    def get_many_calendar_parts(self):
        return self.get_many_calendar_parts_xpath









