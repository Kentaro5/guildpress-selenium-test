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

class Admin_Add_Quiz:

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


    def set_quiz_to_page( self ):

        lesson_details = {
            'beginner_lesson_details' : {
                'first_lesson_details' : {
                    'post_title' : '英語文法(初級講座)',
                    'page_lock' : '1',
                    'quiz_num' : 6,
                    'quiz_correct_num' : 5,
                    'quiz_text' : self.base_dir+'/assets/texts/quiz/quiz.txt',
                    'first_quiz_answer': 'answer_1',
                    'quiz_answer' : {
                        'answer_2',
                        'answer_3',
                        'answer_4',
                        'answer_5',
                        'answer_6',
                    }
                },
                'second_lesson_details' : {
                    'post_title' : '英語リスニング(初級講座)',
                    'page_lock' : '2',
                    'quiz_num' : 2,
                    'quiz_correct_num' : 2,
                    'quiz_text' : self.base_dir+'/assets/texts/quiz/quiz.txt',
                    'first_quiz_answer': 'answer_1',
                    'quiz_answer' : {
                        'answer_2',
                    }
                },
                'third_lesson_details' : {
                    'post_title' : '英語リーディング(初級講座)',
                    'page_lock' : '2',
                    'quiz_num' : 1,
                    'quiz_correct_num' : 1,
                    'quiz_text' : self.base_dir+'/assets/texts/quiz/quiz.txt',
                    'first_quiz_answer': 'answer_1',
                    'quiz_answer' : {
                    }
                },
                'fourth_lesson_details' : {
                    'post_title' : '英語スピーキング(初級講座)',
                    'page_lock' : '2',
                    'quiz_num' : 4,
                    'quiz_correct_num' : 2,
                    'quiz_text' : self.base_dir+'/assets/texts/quiz/quiz.txt',
                    'first_quiz_answer': 'answer_1',
                    'quiz_answer' : {
                        'answer_2',
                        'answer_3',
                        'answer_4',
                    }
                },
                'fifth_lesson_details' : {
                    'post_title' : '英語単語(初級講座)',
                    'page_lock' : '2',
                    'quiz_num' : 4,
                    'quiz_correct_num' : 3,
                    'quiz_text' : self.base_dir+'/assets/texts/quiz/quiz.txt',
                    'first_quiz_answer': 'answer_1',
                    'quiz_answer' : {
                        'answer_2',
                        'answer_3',
                        'answer_4',
                    }
                }
            },
            'normal_lesson_details' : {
                'first_lesson_details' : {
                    'post_title' : '英語文法(中級講座)',
                    'page_lock' : '1',
                    'quiz_num' : 2,
                    'quiz_correct_num' : 1,
                    'quiz_text' : self.base_dir+'/assets/texts/quiz/quiz.txt',
                    'first_quiz_answer': 'answer_1',
                    'quiz_answer' : {
                        'answer_2',
                    }
                },
                'second_lesson_details' : {
                    'post_title' : '英語リスニング(中級講座)',
                    'page_lock' : '2',
                    'quiz_num' : 1,
                    'quiz_correct_num' : 1,
                    'quiz_text' : self.base_dir+'/assets/texts/quiz/quiz.txt',
                    'first_quiz_answer': 'answer_1',
                    'quiz_answer' : {
                    }
                },
                'third_lesson_details' : {
                    'post_title' : '英語リーディング(中級講座)',
                    'page_lock' : '2',
                    'quiz_num' : 7,
                    'quiz_correct_num' : 5,
                    'quiz_text' : self.base_dir+'/assets/texts/quiz/quiz.txt',
                    'first_quiz_answer': 'answer_1',
                    'quiz_answer' : {
                        'answer_2',
                        'answer_3',
                        'answer_4',
                        'answer_5',
                        'answer_6',
                        'answer_7',
                    }
                },
                'fourth_lesson_details' : {
                    'post_title' : '英語スピーキング(中級講座)',
                    'page_lock' : '2',
                    'quiz_num' : 6,
                    'quiz_correct_num' : 5,
                    'quiz_text' : self.base_dir+'/assets/texts/quiz/quiz.txt',
                    'first_quiz_answer': 'answer_1',
                    'quiz_answer' : {
                        'answer_2',
                        'answer_3',
                        'answer_4',
                        'answer_5',
                        'answer_6',
                    }
                },
                'fifth_lesson_details' : {
                    'post_title' : '英語単語(中級講座)',
                    'page_lock' : '2',
                    'quiz_num' : 9,
                    'quiz_correct_num' : 8,
                    'quiz_text' : self.base_dir+'/assets/texts/quiz/quiz.txt',
                    'first_quiz_answer': 'answer_1',
                    'quiz_answer' : {
                        'answer_2',
                        'answer_3',
                        'answer_4',
                        'answer_5',
                        'answer_6',
                        'answer_7',
                        'answer_8',
                        'answer_9',
                    }
                }
            },
            'advanced_lesson_details' : {
                'first_lesson_details' : {
                    'post_title' : '英語文法(上級講座)',
                    'page_lock' : '1',
                    'quiz_num' : 4,
                    'quiz_correct_num' : 3,
                    'quiz_text' : self.base_dir+'/assets/texts/quiz/quiz.txt',
                    'first_quiz_answer': 'answer_1',
                    'quiz_answer' : {
                        'answer_2',
                        'answer_3',
                        'answer_4',
                    }
                },
                'second_lesson_details' : {
                    'post_title' : '英語リスニング(上級講座)',
                    'page_lock' : '2',
                    'quiz_num' : 5,
                    'quiz_correct_num' : 1,
                    'quiz_text' : self.base_dir+'/assets/texts/quiz/quiz.txt',
                    'first_quiz_answer': 'answer_1',
                    'quiz_answer' : {
                        'answer_2',
                        'answer_3',
                        'answer_4',
                        'answer_5',
                    }
                },
                'third_lesson_details' : {
                    'post_title' : '英語リーディング(上級講座)',
                    'page_lock' : '2',
                    'quiz_num' : 1,
                    'quiz_correct_num' : 1,
                    'quiz_text' : self.base_dir+'/assets/texts/quiz/quiz.txt',
                    'first_quiz_answer': 'answer_1',
                    'quiz_answer' : {
                    }
                },
                'fourth_lesson_details' : {
                    'post_title' : '英語スピーキング(上級講座)',
                    'page_lock' : '2',
                    'quiz_num' : 5,
                    'quiz_correct_num' : 3,
                    'quiz_text' : self.base_dir+'/assets/texts/quiz/quiz.txt',
                    'first_quiz_answer': 'answer_1',
                    'quiz_answer' : {
                        'answer_2',
                        'answer_3',
                        'answer_4',
                        'answer_5',
                    }
                },
                'fifth_lesson_details' : {
                    'post_title' : '英語単語(上級講座)',
                    'page_lock' : '2',
                    'quiz_num' : 5,
                    'quiz_correct_num' : 4,
                    'quiz_text' : self.base_dir+'/assets/texts/quiz/quiz.txt',
                    'first_quiz_answer': 'answer_1',
                    'quiz_answer' : {
                        'answer_2',
                        'answer_3',
                        'answer_4',
                        'answer_5',
                    }
                }
            }
        }

        lesson_details_test = {
            'beginner_lesson_details' : {
                'second_lesson_details' : {
                    'post_title' : '英語単語(上級講座)',
                    'page_lock' : '2',
                    'quiz_num' : 5,
                    'quiz_correct_num' : 4,
                    'quiz_text' : self.base_dir+'/assets/texts/quiz/quiz.txt',
                    'first_quiz_answer': 'answer_1',
                    'quiz_answer' : {
                        'answer_2',
                        'answer_3',
                        'answer_4',
                        'answer_5',
                    }
                }
            }
        }

        page_list_xpath = self.admin_parts_xpath['page_list_xpath']
        page_list_elem = self.driver_func.get_elements_by_xpath( page_list_xpath )

        for details_item_name, details_item_value in lesson_details.items():
            for list_name,lesson_details_lists in details_item_value.items():
                self.add_info( lesson_details_lists )

    def reset_info( self, lesson_details_lists ):
        page_list_xpath = self.admin_parts_xpath['page_list_xpath']
        page_list_elem = self.driver_func.get_elements_by_xpath( page_list_xpath )
        no_quiz_btn_xpath = self.admin_parts_xpath['no_quiz_btn_xpath']
        quiz_textarea_xpath = self.admin_parts_xpath['quiz_textarea_xpath']
        quiz_input_xpath = self.admin_parts_xpath['quiz_input_xpath']
        add_quiz_btn_xpath = self.admin_parts_xpath['add_quiz_btn_xpath']
        quiz_first_input_xpath = self.admin_parts_xpath['quiz_first_input_xpath']
        answer_radio_xpath = self.admin_parts_xpath['answer_radio_xpath']
        first_answer_radio_xpath = self.admin_parts_xpath['first_answer_radio_xpath']
        current_page_btn_xpath = self.admin_parts_xpath['current_page_btn_xpath']
        update_post_btn_xpath = self.admin_parts_xpath['update_post_btn']

        target_text = lesson_details_lists['post_title']

        target_elem = self.basic_func.get_target_element( page_list_elem, target_text )
        self.driver_func.click_item( target_elem )

        if( lesson_details_lists['page_lock'] == '2' ):
            self.driver_func.stop( 1 )
            guild_press_quiz_btn_elem = self.driver_func.get_element_by_xpath( no_quiz_btn_xpath )
            self.driver_func.click_item( guild_press_quiz_btn_elem )


        self.driver_func.scroll_top( self.chrome )

        update_post_btn_elem = self.driver_func.get_element_by_xpath( update_post_btn_xpath )
        self.driver_func.click_item( update_post_btn_elem )

        self.driver_func.stop( 1 )

        #投稿リストを表示する
        current_page_btn_elem = self.driver_func.get_element_by_xpath( current_page_btn_xpath )
        self.driver_func.click_item( current_page_btn_elem )


    def add_info( self, lesson_details_lists ):

        page_list_xpath = self.admin_parts_xpath['page_list_xpath']
        page_list_elem = self.driver_func.get_elements_by_xpath( page_list_xpath )
        quiz_btn_xpath = self.admin_parts_xpath['quiz_btn_xpath']
        quiz_textarea_xpath = self.admin_parts_xpath['quiz_textarea_xpath']
        quiz_input_xpath = self.admin_parts_xpath['quiz_input_xpath']
        add_quiz_btn_xpath = self.admin_parts_xpath['add_quiz_btn_xpath']
        quiz_first_input_xpath = self.admin_parts_xpath['quiz_first_input_xpath']
        answer_radio_xpath = self.admin_parts_xpath['answer_radio_xpath']
        first_answer_radio_xpath = self.admin_parts_xpath['first_answer_radio_xpath']
        current_page_btn_xpath = self.admin_parts_xpath['current_page_btn_xpath']
        update_post_btn_xpath = self.admin_parts_xpath['update_post_btn']

        target_text = lesson_details_lists['post_title']

        target_elem = self.basic_func.get_target_element( page_list_elem, target_text )
        self.driver_func.click_item( target_elem )

        if( lesson_details_lists['page_lock'] == '2' ):
            self.driver_func.scroll_down( self.chrome )
            guild_press_quiz_btn_elem = self.driver_func.get_element_by_xpath( quiz_btn_xpath )
            self.driver_func.click_item( guild_press_quiz_btn_elem )

            for x in range( len( lesson_details_lists['quiz_answer'] ) ):
                add_quiz_btn_elem = self.driver_func.get_element_by_xpath( add_quiz_btn_xpath )
                self.driver_func.click_item( add_quiz_btn_elem )

            guild_press_quiz_textarea_elem = self.driver_func.get_element_by_xpath( quiz_textarea_xpath )
            content_text = self.basic_func.get_file_text( lesson_details_lists['quiz_text'] )

            self.driver_func.put_item_info( guild_press_quiz_textarea_elem, content_text  )

            quiz_input_elem = self.driver_func.get_elements_by_xpath( quiz_input_xpath )

            quiz_first_input_elem = self.driver_func.get_element_by_xpath( quiz_first_input_xpath )
            self.driver_func.put_item_info( quiz_first_input_elem, lesson_details_lists['first_quiz_answer'] )

            first_answer_radio_elem = self.driver_func.get_element_by_xpath( first_answer_radio_xpath )

            answer_radio_elem = self.driver_func.get_elements_by_xpath( answer_radio_xpath )

            self.driver_func.click_item( first_answer_radio_elem )

            for i, (quiz_inputs_elem, quiz_answer) in enumerate( zip( quiz_input_elem, lesson_details_lists['quiz_answer'] ) ):
                if( (i + 1) == lesson_details_lists['quiz_correct_num'] ):
                    self.driver_func.click_item( answer_radio_elem[i] )
                self.driver_func.put_item_info( quiz_inputs_elem, quiz_answer )


        self.driver_func.scroll_top( self.chrome )

        update_post_btn_elem = self.driver_func.get_element_by_xpath( update_post_btn_xpath )
        self.driver_func.click_item( update_post_btn_elem )

        self.driver_func.stop( 1 )

        #投稿リストを表示する
        current_page_btn_elem = self.driver_func.get_element_by_xpath( current_page_btn_xpath )
        self.driver_func.click_item( current_page_btn_elem )













