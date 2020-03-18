from plugins.basic.basic import Basic

class Lesson_Posts_Path:

    def __init__(self):

        self.basic_func = Basic()
        self.base_dir = self.basic_func.get_base_dir_path()

        self.many_lesson_posts_path = {}

        self.normal_lesson_posts_path = {
            'beginner_lesson_details' : {
                'first_lesson_details' : {
                    'post_title' : '英語文法(初級講座)',
                    'category_name' : '英語初級講座',
                    'text_dir' : self.base_dir+'/assets/texts/beginner/english-beginner-grammer.txt',
                    'img_dir' : self.base_dir+'/assets/img/beginner/english-beginner-grammer.png'
                },
                'second_lesson_details' : {
                    'post_title' : '英語リスニング(初級講座)',
                    'category_name' : '英語初級講座',
                    'text_dir' : self.base_dir+'/assets/texts/beginner/english-beginner-listening.txt',
                    'img_dir' : self.base_dir+'/assets/img/beginner/english-beginner-listening.png'
                },
                'third_lesson_details' : {
                    'post_title' : '英語リーディング(初級講座)',
                    'category_name' : '英語初級講座',
                    'text_dir' : self.base_dir+'/assets/texts/beginner/english-beginner-reading.txt',
                    'img_dir' : self.base_dir+'/assets/img/beginner/english-beginner-reading.png'
                },
                'fourth_lesson_details' : {
                    'post_title' : '英語スピーキング(初級講座)',
                    'category_name' : '英語初級講座',
                    'text_dir' : self.base_dir+'/assets/texts/beginner/english-beginner-speaking.txt',
                    'img_dir' : self.base_dir+'/assets/img/beginner/english-beginner-speaking.png'
                },
                'fifth_lesson_details' : {
                    'post_title' : '英語単語(初級講座)',
                    'category_name' : '英語初級講座',
                    'text_dir' : self.base_dir+'/assets/texts/beginner/english-beginner-words.txt',
                    'img_dir' : self.base_dir+'/assets/img/beginner/english-beginner-words.png'
                }
            },
            'normal_lesson_details' : {
                'first_lesson_details' : {
                    'post_title' : '英語文法(中級講座)',
                    'category_name' : '英語中級講座',
                    'text_dir' : self.base_dir+'/assets/texts/normal/english-normal-grammer.txt',
                    'img_dir' : self.base_dir+'/assets/img/normal/english-normal-grammer.png'
                },
                'second_lesson_details' : {
                    'post_title' : '英語リスニング(中級講座)',
                    'category_name' : '英語中級講座',
                    'text_dir' : self.base_dir+'/assets/texts/normal/english-normal-listening.txt',
                    'img_dir' : self.base_dir+'/assets/img/normal/english-normal-listening.png'
                },
                'third_lesson_details' : {
                    'post_title' : '英語リーディング(中級講座)',
                    'category_name' : '英語中級講座',
                    'text_dir' : self.base_dir+'/assets/texts/normal/english-normal-reading.txt',
                    'img_dir' : self.base_dir+'/assets/img/normal/english-normal-reading.png'
                },
                'fourth_lesson_details' : {
                    'post_title' : '英語スピーキング(中級講座)',
                    'category_name' : '英語中級講座',
                    'text_dir' : self.base_dir+'/assets/texts/normal/english-normal-speaking.txt',
                    'img_dir' : self.base_dir+'/assets/img/normal/english-normal-speaking.png'
                },
                'fifth_lesson_details' : {
                    'post_title' : '英語単語(中級講座)',
                    'category_name' : '英語中級講座',
                    'text_dir' : self.base_dir+'/assets/texts/normal/english-normal-words.txt',
                    'img_dir' : self.base_dir+'/assets/img/normal/english-normal-words.png'
                }
            },
            'advanced_lesson_details' : {
                'first_lesson_details' : {
                    'post_title' : '英語文法(上級講座)',
                    'category_name' : '英語上級講座',
                    'text_dir' : self.base_dir+'/assets/texts/advanced/english-advanced-grammer.txt',
                    'img_dir' : self.base_dir+'/assets/img/advanced/english-advanced-grammer.png'
                },
                'second_lesson_details' : {
                    'post_title' : '英語リスニング(上級講座)',
                    'category_name' : '英語上級講座',
                    'text_dir' : self.base_dir+'/assets/texts/advanced/english-advanced-listening.txt',
                    'img_dir' : self.base_dir+'/assets/img/advanced/english-advanced-listening.png'
                },
                'third_lesson_details' : {
                    'post_title' : '英語リーディング(上級講座)',
                    'category_name' : '英語上級講座',
                    'text_dir' : self.base_dir+'/assets/texts/advanced/english-advanced-reading.txt',
                    'img_dir' : self.base_dir+'/assets/img/advanced/english-advanced-reading.png'
                },
                'fourth_lesson_details' : {
                    'post_title' : '英語スピーキング(上級講座)',
                    'category_name' : '英語上級講座',
                    'text_dir' : self.base_dir+'/assets/texts/advanced/english-advanced-speaking.txt',
                    'img_dir' : self.base_dir+'/assets/img/advanced/english-advanced-speaking.png'
                },
                'fifth_lesson_details' : {
                    'post_title' : '英語単語(上級講座)',
                    'category_name' : '英語上級講座',
                    'text_dir' : self.base_dir+'/assets/texts/advanced/english-advanced-words.txt',
                    'img_dir' : self.base_dir+'/assets/img/advanced/english-advanced-words.png'
                }
            }
        }


    def get_normal_lesson_posts_path(self):
        return self.normal_lesson_posts_path


    def get_many_lesson_posts_path(self):
        return self.many_lesson_posts_path

    def create_many_lesson_posts(self):

        for z in range( 60, 61 ):
            loop_str_z = str(z)
            cat_name = '英語初級講座'+loop_str_z
            for x in range( 0, 200 ):
                loop_str_x = str(x)
                new_val = self.set_dic_val(loop_str_x, cat_name)
                new_dic = self.create_new_dic( loop_str_x, loop_str_z, new_val )
                self.many_lesson_posts_path.update(new_dic)

    def create_new_dic( self, loop_str_x, loop_str_z, new_list_val ):
        new_dic = {}
        key_name = 'lesson_details'+loop_str_z+loop_str_x
        new_dic.setdefault( key_name, new_list_val )

        return new_dic

    def set_dic_val( self, loop_str,cat_name ):
        new_list_val = {}
        new_list_val.setdefault( 'post_title', '英語文法(初級講座)'+loop_str )
        new_list_val.setdefault( 'category_name', cat_name )
        new_list_val.setdefault( 'text_dir', self.base_dir+'/assets/texts/beginner/english-beginner-grammer.txt' )
        new_list_val.setdefault( 'img_dir', self.base_dir+'/assets/img/beginner/english-beginner-grammer.png' )


        return new_list_val





