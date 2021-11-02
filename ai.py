
def ca(map):
    # 黑子评分
    win = 1000000
    lb4 = 50000
    db4 = 400
    lb3 = 400
    sb3 = 20
    lb2 = 20
    sb2 = 20
    lb1 = 1
    # 白子评分
    lose = -10000000
    lw5 = -100000
    dw4 = -100000
    lw3 = -80000
    sw3 = -50
    lw2 = -50
    sw2 = -3
    lw1 = -3

    # 创建棋盘排布
    m = [[0 for y in range(16)] for x in range(16)]
    for x in range(19):
        for y in range(19):
            if x <= 4 or y <= 4 or x >= 15 or y >= 15:
                m[x][y] = 3
            else:
                m[x][y] = map[x-1][y-1]
    n = map(str, m)  # 换字符串
    for x in range(4, 14):
        for y in range(1, 15):
            if m[x][y] == 0:
                m[x][y] = 2
                ch = ''
                for a in range(8):
                    ch += n[x-4][y]  # 形成横向字符串判断类型

