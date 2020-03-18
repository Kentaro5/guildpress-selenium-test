from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from plugins.xpath.AdminMenuPath import Admin_Menu_Path
from plugins.driver.DriverAction import Driver_Action
from plugins.login.Admin_Login import *

from controllers.InitSetController import Init_Set_Controller
from controllers.NormalUserRegisterController import Normal_User_Register_Controller
from controllers.PayPalUserRegisterController import PayPal_User_Register_Controller
from controllers.OriginalFormController import Original_Form_Controller
from controllers.LessonOverViewController import Lesson_Over_View_Controller
from controllers.LessonDetailPostsController import Lesson_Detail_Posts_Controller
from controllers.LessonProgressController import Lesson_Progress_Controller
from controllers.GoogleCalendarSettingController import Google_Calendar_Setting_Controller
from controllers.AdminCalendarController import Admin_Calendar_Controller
from controllers.PublicCalendarController import Public_Calendar_Controller
from controllers.AdminManyCalendarsController import Admin_Many_Calendars_Controller
from controllers.MemberRankOverViewController import Member_Rank_OverView_Controller
from controllers.MemberRankDetailPostsController import Member_Rank_Detail_Posts_Controller
from controllers.TextDocsController import Text_Docs_Controller
from controllers.AdminRockController import Admin_Rock_Controller
from controllers.AddQuizController import Add_Quiz_Controller
from controllers.NewsController import News_Controller
from controllers.EditUserController import Edit_User_Controller
from controllers.many.lesson.ManyLessonOverViewController import Many_Lesson_Over_View_Controller
from controllers.many.lesson.ManyLessonDetailPostsController import Many_Lesson_Detail_Posts_Controller
from controllers.many.lesson_progress.ManyLessonProgressController import Many_Lesson_Progress_Controller





#xpathで使うものを設定。
admin_xpath = Admin_Menu_Path()
admin_xpath_list = admin_xpath.get_admin_menu_xpath()
admin_parts_xpath_list = admin_xpath.get_admin_parts()
admin_menu_list_parts_xpath = admin_xpath.get_admin_menu_list_parts_xpath()


# 使うドライバーを定義する
chrome = webdriver.Chrome(ChromeDriverManager().install())

#テストする先のURLを設定する
target_url = 'http://localhost:8888/wordpress/wp-selenium/'


# インスタンス作成
driver_action_func = Driver_Action( chrome )

# インスタンス作成
admin_login = Admin_Login(chrome, target_url)

# 管理画面にログイン
admin_login.login_to_admin()




############################################################



#初期設定ができるかチェックする。
init_set_test = Init_Set_Controller( chrome, target_url )
init_set_test.start()

print('init_set_test')






############################################################


#普通の登録ができるかチェックする。
normal_user_register_test = Normal_User_Register_Controller( chrome, target_url )
normal_user_register_test.start()

print('normal_user_register_test')




############################################################


#ペイパル決済を用いた登録ができるかチェックする。
paypal_user_register_test = PayPal_User_Register_Controller( chrome, target_url )
paypal_user_register_test.start()


print('paypal_user_register_test')


############################################################


#ユーザーのオリジナル投稿フォーム部分の作成
original_form_test = Original_Form_Controller( chrome, target_url )
original_form_test.start()
print('original_form_test')


############################################################


#レッスンの概要ページを詰める
lesson_over_view_test = Lesson_Over_View_Controller( chrome, target_url )
lesson_over_view_test.start()
print('lesson_over_view_test')

############################################################


#レッスン詳細ページを詰める。
lesson_detail_posts_test = Lesson_Detail_Posts_Controller( chrome, target_url )
lesson_detail_posts_test.start()
print('lesson_detail_posts_test')


############################################################

#各レッスンの進捗を進めてチェックする。
lesson_progress_test = Lesson_Progress_Controller( chrome, target_url )
lesson_progress_test.start()
print('lesson_progress_test')



############################################################


#管理画面でカレンダーが動作するかチェックする。
admin_calendar_controller_test = Admin_Calendar_Controller( chrome, target_url )
admin_calendar_controller_test.start()

calendar_title = admin_calendar_controller_test.get_calendar_title()
print('admin_calendar_controller_test')


############################################################



#ユーザー側のカレンダーページが動作するかチェックする
admin_calendar_controller_test = Public_Calendar_Controller( chrome, target_url, calendar_title )
admin_calendar_controller_test.start()
print('admin_calendar_controller_test')




############################################################



##各会員ランクを登録する
admin_member_rank_test = Member_Rank_OverView_Controller( chrome, target_url )
admin_member_rank_test.start()
print('admin_member_rank_test')





############################################################


##今度は詳細ページでの表示を確認する
member_rank_detail_posts_test = Member_Rank_Detail_Posts_Controller( chrome, target_url )
member_rank_detail_posts_test.start()

print('member_rank_detail_posts_test')




############################################################


##教材のアップロードのテスト
text_docs_test = Text_Docs_Controller( chrome, target_url )
text_docs_test.start()
print('text_docs_test')



############################################################


##ページにロックを掛けるテスト
admin_rock_test = Admin_Rock_Controller( chrome, target_url )
admin_rock_test.start()
print('admin_rock_test')



############################################################


##ページにクイズを設定するテスト
add_quiz_test = Add_Quiz_Controller( chrome, target_url )
add_quiz_test.start()
print('add_quiz_test')


############################################################


news_test = News_Controller( chrome, target_url )
news_test.start()
print('news_test')


############################################################


edit_user_test = Edit_User_Controller( chrome, target_url )
edit_user_test.start()
print('edit_user_test')




############################################################


#管理画面でカレンダーが動作するかチェックする。
admin_many_calendar_controller_test = Admin_Many_Calendars_Controller( chrome, target_url )
admin_many_calendar_controller_test.start()

calendar_titles = admin_many_calendar_controller_test.get_calendar_titles()

print('admin_many_calendar_controller_test')


############################################################


#ユーザー側のカレンダーページが動作するかチェックする
for x in range( 4 ):
    admin_calendar_controller_test = Public_Calendar_Controller( chrome, target_url, calendar_titles )
    admin_calendar_controller_test.start_many()
    print('admin_calendar_controller_test')



############################################################




#レッスンの概要ページをたくさん作る。
many_lesson_over_view_test = Many_Lesson_Over_View_Controller( chrome, target_url )
many_lesson_over_view_test.start()
print('Many_Lesson_Over_View_Controller_test')




############################################################




#レッスンの詳細ページをたくさん作る。
many_lesson_detail_posts_test = Many_Lesson_Detail_Posts_Controller( chrome, target_url )
many_lesson_detail_posts_test.start()

print('Many_Lesson_Detail_Posts_Controller_test')



############################################################



many_lesson_progress_test = Many_Lesson_Progress_Controller( chrome, target_url )
many_lesson_progress_test.start()
print('Many_Lesson_Progress_Controller_test')




############################################################


