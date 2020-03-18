from plugins.basic.basic import Basic

class Lesson_Over_View_Path:

    def __init__(self):

        self.basic_func = Basic()
        self.base_dir = self.basic_func.get_base_dir_path()

        self.many_lesson_overview = {}

        self.normal_lesson_overview = {
            'first_lesson_over_view' : {
                'post_title' : '英語初級講座',
                'category_name' : '英語初級講座',
                'text_dir' : self.base_dir+'/assets/texts/beginner/english-beginner.txt',
                'img_dir' : self.base_dir+'/assets/img/beginner/english-beginner-overview.png'
            },
            'second_lesson_over_view' : {
                'post_title' : '英語中級講座',
                'category_name' : '英語中級講座',
                'text_dir' : self.base_dir+'/assets/texts/normal/english-normal.txt',
                'img_dir' : self.base_dir+'/assets/img/normal/english-normal-overview.png'
            },
            'third_lesson_over_view' : {
                'post_title' : '英語上級講座',
                'category_name' : '英語上級講座',
                'text_dir' : self.base_dir+'/assets/texts/advanced/english-advanced.txt',
                'img_dir' : self.base_dir+'/assets/img/advanced/english-advanced-overview.png'
            }
        }


    def get_normal_lesson_overview(self):
        return self.normal_lesson_overview


    def get_many_lesson_overview(self):
        return self.many_lesson_overview

    def create_many_lesson_overview(self):
        for x in range( 0, 20 ):
            loop_str = str(x)
            new_val = self.set_dic_val(loop_str)
            new_dic = self.create_new_dic( loop_str, new_val )
            self.many_lesson_overview.update(new_dic)

    def create_new_dic( self, loop_str, new_list_val ):
        new_dic = {}
        key_name = 'lesson_over_view'+loop_str
        new_dic.setdefault( key_name, new_list_val )

        return new_dic

    def set_dic_val( self, loop_str ):
        new_list_val = {}
        new_list_val.setdefault( 'post_title', '英語初級講座'+loop_str )
        new_list_val.setdefault( 'category_name', '英語初級講座'+loop_str )
        new_list_val.setdefault( 'text_dir', self.base_dir+'/assets/texts/beginner/english-beginner.txt' )
        new_list_val.setdefault( 'img_dir', self.base_dir+'/assets/img/beginner/english-beginner-overview.png' )

        return new_list_val






