from plugins.basic.basic import Basic

class Lesson_Progress_Path:

    def __init__(self):

        self.basic_func = Basic()
        self.base_dir = self.basic_func.get_base_dir_path()

        self.many_target_lesson_lists_path = []

        self.normal_target_lesson_lists_path = {
            '英語初級講座',
            '英語中級講座',
            '英語上級講座'
        }


    def get_normal_target_lesson_lists_path(self):
        return self.normal_target_lesson_lists_path


    def get_many_target_lesson_lists_path(self):
        return self.many_target_lesson_lists_path


    def create_many_lesson_posts(self):

        for z in range( 0, 200 ):
            loop_str_z = str(z)
            new_lesson_name = '英語初級講座'+loop_str_z
            self.many_target_lesson_lists_path.append( new_lesson_name )






