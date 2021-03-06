# 项目说明
# load：         加载数据集并进行预处理
# function:      训练和推荐需要用到的函数
# train:         训练网络
# recommender:   电影推荐
# show：         pyqt做的UI界面
# main：         主函数

# 如果需要训练新的模型，则运行train文件。训练完成后运行main文件可进行调用。
# 如果根据已有模型进行电影推荐，则运行main文件。

import sys
from show import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = show_window()
    sys.exit(app.exec_())