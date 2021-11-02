class Gomoku:

    def __init__(self):
        self.g_map = [[0 for y in range(15)] for x in range(15)]
        self.cur_step = 0  # 步数
        self.chess = []

    def move(self, pos_x, pos_y):
        if 0 <= pos_x <= 14 and 0 <= pos_y <= 14:  # 判断能否落子
            if self.g_map[pos_x][pos_y] == 0:
                self.g_map[pos_x][pos_y] = 1
                self.cur_step += 1
                self.chess.append((pos_x, pos_y, 1))
                return 1
        else:
            return 0

    # 判断游戏结局。0进行中，1玩家胜，2电脑胜利，3平局
    def game_result(self):
        # 判断是否横向五子
        for y in range(15):
            for x in range(11):
                p = 1
                c = 2
                for a in range(5):
                    if self.g_map[x+a][y] != 1:
                        p = 0
                    if self.g_map[x + a][y] != 2:
                        c = 0
                    if p == 0 and c == 0:
                        break
                if p:
                    return 1
                if c:
                    return 2
        # 判断是否纵向五子
        for x in range(15):
            for y in range(11):
                p = 1
                c = 2
                for a in range(5):
                    if self.g_map[x][y+a] != 1:
                        p = 0
                    if self.g_map[x][y+a] != 2:
                        c = 0
                    if p == 0 and c == 0:
                        break
                if p:
                    return 1
                if c:
                    return 2
        # 判断是否左上-右下五子
        for x in range(11):
            for y in range(11):
                p = 1
                c = 2
                for a in range(5):
                    if self.g_map[x+4-a][y+4-a] != 1:
                        p = 0
                    if self.g_map[x+4-a][x+4-a] != 2:
                        c = 0
                    if p == 0 and c == 0:
                        break
                if p:
                    return 1
                if c:
                    return 2
        # 判断是否右上-左下五子
        for x in range(11):
            for y in range(11):
                p = 1
                c = 2
                for a in range(5):
                    if self.g_map[x+a][y+a] != 1:
                        p = 0
                    if self.g_map[x+a][y+a] != 2:
                        c = 0
                    if p == 0 and c == 0:
                        break
                if p:
                    return 1
                if c:
                    return 2
        # 判和
        for x in range(15):
            for y in range(15):
                if self.g_map[x][y] == 0:
                    return 0
        return 3

    def ai_move(self):
        for x in range(15):
            for y in range(15):
                if self.g_map[x][y] == 0:
                    self.g_map[x][y] = 2
                    self.cur_step += 1
                    self.chess.append((x, y, 2))
                    return x, y


