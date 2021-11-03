cell_num = 15
# g_map = [[1, 2, 3, 4],
#          [5, 6, 7, 8],
#          [9, 10, 11, 12],
#          [13, 14, 15, 16]
#          ]
mm = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
score = {
    "11111": 100000, "011110": 10000, "01111": 1000, "11110": 1000, "01110": 1000,
    "1110": 100, "0111": 100, "0110": 100, "011": 10, "110": 10, "010": 10
}


def test(g_map):
    # 横项遍历
    for col in g_map:
        print(col)
        # ai_value += self.each_value([-1 * i for i in col])
    # 纵项遍历，需要转置
    for row in list(map(list, zip(*g_map))):
        print(row)
    # 右上
    for col in range(cell_num):
        line = []
        offset = 0
        while col + offset < cell_num:
            line.append(g_map[offset][col + offset])
            offset += 1
        print(line)

    # 左上
    for row in range(1, cell_num):
        line = []
        offset = 0
        while row + offset < cell_num:
            line.append(g_map[row + offset][offset])
            offset += 1
        print(line)

    # 左上
    for row in range(cell_num):
        line = []
        offset = 0
        while row - offset >= 0:
            line.append(g_map[row - offset][offset])
            offset += 1
        print(line)

    # 右下
    for col in range(1, cell_num):
        line = []
        offset = 0
        while col + offset < cell_num:
            line.append(g_map[cell_num - offset - 1][col + offset])
            offset += 1
        print(line)


def each_value(line):
    global score
    value = 0
    count = 0  # 比较的起始位置
    # 棋形转换成字符串
    # line = ''.join(str(i) for i in line)
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
            return value
    return value


if __name__ == "__main__":
    # for each in mm:
    #     print(each)
    # test(mm)
    value = each_value('000-111100000000')
    print(value)
