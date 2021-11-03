# import time
# from game import Gomoku
# import sys
# import time
# import pygame
# from pygame.locals import *
# from random import *
# import math
# import traceback
#
#
# def main():
#     pygame.init()
#     clock = pygame.time.Clock()
#     g = Gomoku()
#     # g.play()
#     # 绘制棋盘
#     space = 60  # 四周留下的边距
#     cell_size = 40  # 每个格子大小
#     cell_num = 15
#     grid_size = cell_size * (cell_num - 1) + space * 2  # 棋盘的大小
#     screencaption = pygame.display.set_caption('五子棋')
#     screen = pygame.display.set_mode((grid_size, grid_size))  # 设置窗口长宽
#     font1 = pygame.font.Font("font/font.ttf", 48)
#     font2 = pygame.font.Font("font/font.ttf", 24)
#     white = (255, 255, 255)
#     black = (30, 30, 30)
#     running = True
#     an = 0
#     while running:
#         ch = 0
#         screen.fill((0, 0, 150))  # 将界面设置为蓝色
#         for x in range(0, cell_size * cell_num, cell_size):
#             pygame.draw.line(screen, (200, 200, 200), (x + space, 0 + space),
#                              (x + space, cell_size * (cell_num - 1) + space), 1)
#         for y in range(0, cell_size * cell_num, cell_size):
#             pygame.draw.line(screen, (200, 200, 200), (0 + space, y + space),
#                              (cell_size * (cell_num - 1) + space, y + space), 1)
#
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == MOUSEBUTTONUP:
#                 if an:
#                     x, y = pygame.mouse.get_pos()
#                     if 450 <= x <= 600 and 20 <= y <= 60:
#                         an = 0
#                         g = Gomoku()
#                 else:
#                     x, y = pygame.mouse.get_pos()  # 获取鼠标位置
#                     xi = int(round((x - space) * 1.0 / cell_size))  # 获取到x方向上取整的序号
#                     yi = int(round((y - space) * 1.0 / cell_size))  # 获取到y方向上取整的序号
#                     ch = g.move(xi, yi)
#         an = g.game_result()
#         if an == 1:
#             text = font1.render("VICTORY", True, white)
#             text2 = font2.render("RESTART", True, white)
#             screen.blit(text, (250, 0))
#             screen.blit(text2, (450, 25))
#             ch = 0
#         if ch:
#             xa, ya = g.ai_move()
#         for x, y, player in g.chess:
#             if player == 1:
#                 pygame.draw.circle(screen, (205, 205, 205), [x * cell_size + space, y * cell_size + space], 16, 16)
#             else:
#                 pygame.draw.circle(screen, black, [x * cell_size + space, y * cell_size + space], 16, 16)
#         # 判断结果
#         an = g.game_result()
#         if an == 2:
#             text1 = font1.render("GAME OVER!", True, white)
#             text2 = font2.render("RETRY", True, white)
#             screen.blit(text1, (200, 0))
#             screen.blit(text2, (480, 25))
#
#         pygame.display.flip()
#         clock.tick(30)
#
#
# if __name__ == "__main__":
#     main()
