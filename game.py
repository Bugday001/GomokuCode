import numpy as np
import time
from functools import wraps

inf = 999999999
# 各种棋形的分数
man_score = {
    "11111": 100000, "011110": 10000, "01111": 1000, "11110": 1000, "01110": 1000,
    "1110": 100, "0111": 100, "0110": 100, "011": 10, "110": 10, "010": 10
}
ai_score = {
    "-2-2-2-2-2": -110000, "0-2-2-2-20": -11000, "0-2-2-2-2": -1100, "-2-2-2-20": -1100,
    "0-2-2-20": -1100, "-2-2-20": -110, "0-2-2-2": -110, "0-2-20": -110, "0-2-2": -11,
    "-2-20": -11, "0-20": -11
}
# 搜索深度
search_depth = 4


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print("Total time running %s: %s seconds" %
              (function.__name__, str(t1 - t0))
              )
        return result

    return function_timer


class Gomoku:
    def __init__(self):
        self.g_map = [[0 for y in range(15)] for x in range(15)]
        self.cur_step = 0  # 步数
        self.chess = []
        self.player = 1  # -1是电脑，1是人类
        self.best_loc = [0, 0]  # 电脑下棋的最佳位置
        self.cell_num = 15

    def move(self, pos_x, pos_y):
        self.player = -1  # 下次电脑下棋
        if 0 <= pos_x <= 14 and 0 <= pos_y <= 14:  # 判断能否落子
            if self.g_map[pos_x][pos_y] == 0:
                self.g_map[pos_x][pos_y] = 1
                self.cur_step += 1
                self.chess.append((pos_x, pos_y, 1))
                return 1
        else:
            return 0

    # 判断游戏结局。0进行中，1玩家胜，-1电脑胜利，2平局
    def game_result(self):
        # 横项遍历
        for line in self.g_map:
            line = ''.join(str(i) for i in line)
            if "11111" in line:
                return 1
            elif "-2-2-2-2-2" in line:
                return -1
        # 纵项遍历，需要转置
        for line in list(map(list, zip(*self.g_map))):
            line = ''.join(str(i) for i in line)
            if "11111" in line:
                return 1
            elif "-2-2-2-2-2" in line:
                return -1
        # 斜的,对角线遍历
        # 右上
        for col in range(self.cell_num):
            line = []
            offset = 0
            while col + offset < self.cell_num:
                line.append(self.g_map[offset][col + offset])
                offset += 1
            line = ''.join(str(i) for i in line)
            if "11111" in line:
                return 1
            elif "-2-2-2-2-2" in line:
                return -1
        # 左上
        for row in range(1, self.cell_num):
            line = []
            offset = 0
            while row + offset < self.cell_num:
                line.append(self.g_map[row + offset][offset])
                offset += 1
            line = ''.join(str(i) for i in line)
            if "11111" in line:
                return 1
            elif "-2-2-2-2-2" in line:
                return -1
        # 左上
        for row in range(self.cell_num):
            line = []
            offset = 0
            while row - offset >= 0:
                line.append(self.g_map[row - offset][offset])
                offset += 1
            line = ''.join(str(i) for i in line)
            if "11111" in line:
                return 1
            elif "-2-2-2-2-2" in line:
                return -1
        # 右下
        for col in range(1, self.cell_num):
            line = []
            offset = 0
            while col + offset < self.cell_num:
                line.append(self.g_map[self.cell_num - offset - 1][col + offset])
                offset += 1
            line = ''.join(str(i) for i in line)
            if "11111" in line:
                return 1
            elif "-2-2-2-2-2" in line:
                return -1
        return 0

    @fn_timer
    def ai_move(self):
        print("ai_move!")
        self.maxmin_search(search_depth)
        print(self.best_loc)
        self.player = 1  # 下次人类下棋
        self.g_map[self.best_loc[0]][self.best_loc[1]] = -2
        self.cur_step += 1
        self.chess.append((self.best_loc[0], self.best_loc[1], 2))
        return self.best_loc[0], self.best_loc[1]

    # 判断周围是否有棋，是否有必要预测，写法很蠢，待改进
    def is_around_empty(self, loc):
        area = 1
        index = [0, 0, 0, 0]
        index[0] = loc[0] - area if loc[0] - area > 0 else 0
        index[1] = loc[0] + area if loc[0] + area < self.cell_num - 1 else self.cell_num - 1
        index[2] = loc[1] - area if loc[1] - area > 0 else 0
        index[3] = loc[1] + area if loc[1] + area < self.cell_num - 1 else self.cell_num - 1
        loc_map = np.array(self.g_map)
        return (loc_map[index[0]:index[1], index[2]:index[3]] == 0).all()

    # 合法的落棋位置集合
    def legal_loc(self):
        left_loc = []
        for i in range(self.cell_num):
            for j in range(self.cell_num):
                if self.g_map[i][j] == 0 and not self.is_around_empty((i, j)):
                    left_loc.append((i, j))
        return left_loc

    # 落棋
    def move_piece(self, loc):
        if self.player == -1:
            self.g_map[loc[0]][loc[1]] = -2
        else:
            self.g_map[loc[0]][loc[1]] = 1
        self.player *= -1  # 切换下次的player

    # 悔棋
    def remove_piece(self, loc):
        self.g_map[loc[0]][loc[1]] = 0
        self.player *= -1  # 切换上次的player

    # 每一个队列的返回值
    def each_value(self, line, score):
        value = 0
        count = 0  # 比较的起始位置
        # 棋形转换成字符串
        line = ''.join(str(i) for i in line)
        while count < 16:
            for k in score.keys():
                if line[count:].find(k) >= 0:
                    value += score[k]
                    count += len(k) + line[count:].find(k)
                    if k[-1] == '0':
                        count -= 1
                    break
            else:
                # 一个也没找到
                # if value==1000:
                #     print(line, value)
                return value
        # print(line, value)
        return value

    # 总评分函数
    def Evaluate(self):
        global man_score, ai_score
        # print("evaluate!")
        if self.game_result() == -1:
            return inf
        elif self.game_result() == 1:
            return -inf
        man_value = 0
        ai_value = 0
        # 横项遍历
        for col in self.g_map:
            man_value += self.each_value(col, man_score)
            ai_value += self.each_value(col, ai_score)
        # 纵项遍历，需要转置
        for row in list(map(list, zip(*self.g_map))):
            man_value += self.each_value(row, man_score)
            ai_value += self.each_value(row, ai_score)
        # 斜的,对角线遍历
        # 右上
        for col in range(self.cell_num):
            line = []
            offset = 0
            while col + offset < self.cell_num:
                line.append(self.g_map[offset][col + offset])
                offset += 1
            man_value += self.each_value(line, man_score)
            ai_value += self.each_value(line, ai_score)
        # 左上
        for row in range(1, self.cell_num):
            line = []
            offset = 0
            while row + offset < self.cell_num:
                line.append(self.g_map[row + offset][offset])
                offset += 1
            man_value += self.each_value(line, man_score)
            ai_value += self.each_value(line, ai_score)
        # 左上
        for row in range(self.cell_num):
            line = []
            offset = 0
            while row - offset >= 0:
                line.append(self.g_map[row - offset][offset])
                offset += 1
            man_value += self.each_value(line, man_score)
            ai_value += self.each_value(line, ai_score)
        # 右下
        for col in range(1, self.cell_num):
            line = []
            offset = 0
            while col + offset < self.cell_num:
                line.append(self.g_map[self.cell_num - offset - 1][col + offset])
                offset += 1
            man_value += self.each_value(line, man_score)
            ai_value += self.each_value(line, ai_score)
        return -man_value - ai_value

    # 最大最小
    def maxmin_search(self, depth, bro_best_value=inf):
        # print("maxmin:", depth)
        if -1 == self.game_result() or 1 == self.game_result():
            return self.Evaluate()
        if depth == 0:
            return self.Evaluate()
        if self.player == -1:
            best_value = -inf
        elif self.player == 1:
            best_value = inf
        # 得到空的位置
        left_loc = self.legal_loc()
        for loc in left_loc:
            self.move_piece(loc)
            value = self.maxmin_search(depth - 1, best_value)
            self.remove_piece(loc)
            if self.player == 1:
                # 剪枝
                if value < bro_best_value and 1:
                    return value
                if value <= best_value:
                    best_value = value
                    if depth == search_depth:
                        self.best_loc = loc
            elif self.player == -1:
                if value > bro_best_value and 1:
                    return value
                if value >= best_value:
                    best_value = value
                    if depth == search_depth:
                        self.best_loc = loc
        return best_value
