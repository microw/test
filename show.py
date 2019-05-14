# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from recommender import rating_movie, recommend_same_type_movie, recommend_user_favorite_movie, \
    recommend_other_favorite_movie
from function import movies_orig


class show_window(QWidget):
    def __init__(self):
        super(show_window, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(1050,690)
        self.setWindowTitle('电影推荐')
        title_Label = QLabel('机器学习——电影推荐', self)
        title_Label.move(400, 30)
        author_Label = QLabel('作者：张冰源 / zby', self)
        author_Label.move(900, 80)
        validator_user = QIntValidator(1, 6040, self)
        # validator_movie = QIntValidator(1, 3592, self)

        fun1_Label = QLabel('打分情况：', self)
        fun1_Label.move(50, 400)
        user1_Label = QLabel('用户：', self)
        user1_Label.move(150, 400)
        self.user1_Line = QLineEdit('1', self)
        #颜色
        self.user1_Line.setStyleSheet("QWidget { background-color: #FFEFD5 }")
        self.user1_Line.move(220, 400)
        self.user1_Line.setFixedWidth(80)
        # self.user1_Line.setValidator(validator_user)
        mov1_Label = QLabel('电影:', self)
        mov1_Label.move(150, 450)
        self.mov1_Line = QLineEdit('1', self)
        #颜色
        self.mov1_Line.setStyleSheet("QWidget { background-color: #FFEFD5 }")
        self.mov1_Line.move(220, 450)
        self.mov1_Line.setFixedWidth(80)
        # self.mov1_Line.setValidator(validator_movie)
        fun1_Btn = QPushButton('确定', self)
        #颜色
        fun1_Btn.setStyleSheet("QWidget { background-color: #FFEFD5 }")
        fun1_Btn.move(350, 450)
        fun1_Btn.clicked.connect(self.rate_movie)
        rate_Label = QLabel('打分：', self)
        rate_Label.move(150, 500)
        self.rate_Label = QLabel('——', self)
        self.rate_Label.move(220, 500)
        self.rate_Label.setFixedWidth(100)

        fun2_Label = QLabel('相似推荐：', self)
        fun2_Label.move(50, 150)
        mov2_Label = QLabel('电影：', self)
        mov2_Label.move(150, 150)
        self.mov2_Line = QLineEdit('1', self)
        #颜色控制
        self.mov2_Line.setStyleSheet("QWidget { background-color: #FFEFD5 }")

        self.mov2_Line.move(220, 150)

        self.mov2_Line.setFixedWidth(80)
        # self.mov2_Line.setValidator(validator_movie)
        fun2_Btn = QPushButton('确定', self)
        #控件颜色设置

        fun2_Btn.setStyleSheet("QWidget { background-color: #FFEFD5 }")
        fun2_Btn.move(350, 150)
        fun2_Btn.clicked.connect(self.recommend_same_type)

        fun3_Label = QLabel('猜你喜欢：', self)
        fun3_Label.move(50, 220)
        user3_Label = QLabel('用户：', self)
        user3_Label.move(150, 220)
        self.user3_Line = QLineEdit('1', self)
        #颜色
        self.user3_Line.setStyleSheet("QWidget { background-color: #FFEFD5 }")
        self.user3_Line.move(220, 220)
        self.user3_Line.setFixedWidth(80)
        self.user3_Line.setValidator(validator_user)
        fun3_Btn = QPushButton('确定', self)
        #颜色设置

        fun3_Btn.setStyleSheet("QWidget { background-color: #FFEFD5 }")
        fun3_Btn.move(350, 220)
        fun3_Btn.clicked.connect(self.recommend_user_favourite)

        fun4_Label = QLabel('志同道合：', self)
        fun4_Label.move(50, 290)
        mov4_Label = QLabel('电影:', self)
        mov4_Label.move(150, 290)
        self.mov4_Line = QLineEdit('1', self)
        #颜色
        self.mov4_Line.setStyleSheet("QWidget { background-color: #FFEFD5 }")
        self.mov4_Line.move(220, 290)
        self.mov4_Line.setFixedWidth(80)
        # self.mov4_Line.setValidator(validator_movie)
        fun4_Btn = QPushButton('确定', self)
        #颜色
        fun4_Btn.setStyleSheet("QWidget { background-color: #FFEFD5 }")
        fun4_Btn.move(350, 290)
        fun4_Btn.clicked.connect(self.recommend_other_favourite)

        fun5_Label = QLabel('功能设置：', self)
        fun5_Label.move(50, 570)
        max_mov_Label = QLabel('推荐电影上限：', self)
        max_mov_Label.move(150, 570)
        self.max_mov_Line = QLineEdit('4', self)
        #颜色
        self.max_mov_Line.setStyleSheet("QWidget { background-color: #FFEFD5 }")
        self.max_mov_Line.move(300, 570)
        self.max_mov_Line.setFixedWidth(145)
        max_user_Label = QLabel('推荐好友上限：', self)
        max_user_Label.move(150, 620)
        self.max_user_Line = QLineEdit('5', self)
        self.max_user_Line.setStyleSheet("QWidget { background-color: #FFEFD5 }")
        self.max_user_Line.move(300, 620)
        self.max_user_Line.setFixedWidth(145)

        result_Label = QLabel('推荐结果：', self)
        result_Label.move(500, 100)
        self.result_Edit = QTextEdit(self)
        #颜色
        self.result_Edit.setStyleSheet("QWidget { background-color: #FFEFD5 }")
        self.result_Edit.setFixedSize(500, 520)
        self.result_Edit.move(500, 150)
        # self.setStyleSheet("#MainWindow{border-image:url(./images/python.jpg);}")
        self.setObjectName("QWidget")
        # todo 2 设置窗口背景色
        col = QColor(96, 96, 96)
        print(col.name())

        self.setStyleSheet("#QWidget { background-color: %s }" % col.name())

        self.show()

    def rate_movie(self):
        user = int(self.user1_Line.text())
        mov = self.mov1_Line.text()
        # 电影名转化为电影ID
        mov = self.code_to_movie_name(mov)
        result = rating_movie(user, mov)
        self.rate_Label.setText(str(result))

    def recommend_same_type(self):
        mov = self.mov2_Line.text()
        # 电影名转化为电影ID
        mov = self.code_to_movie_name(mov)
        result = recommend_same_type_movie(mov, int(self.max_mov_Line.text()))
        for i in result:
            self.result_Edit.append(i)
            self.result_Edit.append('')

    def recommend_user_favourite(self):
        user = int(self.user3_Line.text())
        result = recommend_user_favorite_movie(user, int(self.max_mov_Line.text()))
        for i in result:
            self.result_Edit.append(i)
            self.result_Edit.append('')

    def recommend_other_favourite(self):
        mov = self.mov4_Line.text()
        # 电影名转化为电影ID
        mov = self.code_to_movie_name(mov)
        result = recommend_other_favorite_movie(mov, int(self.max_user_Line.text()), int(self.max_mov_Line.text()))
        for i in result:
            self.result_Edit.append(i)
            self.result_Edit.append('')

    # 电影名转化为电影ID
    def code_to_movie_name(self, movie_name):
        movie_code = None
        for val in movies_orig:
            if movie_name == val[1]:
                movie_code = val[0]

        movie_code = 1 if not movie_code else movie_code
        return movie_code
