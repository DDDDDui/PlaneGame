import pygame
from plane_sprites import *


class PlaneGame(object):

    def __init__(self):
        print("游戏初始化")

        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT)
        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法，精灵和精灵组的创建
        self._create_sprites()

    def _create_sprites(self):

        # 创建背景精灵和精灵组
        pass

    def start_game(self):
        print("游戏开始")

    @staticmethod
    def _game_over():
        print("游戏结束")


if __name__ == "__main__":

    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()
