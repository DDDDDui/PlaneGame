import pygame


class PlaneGame(object):

    def __init__(self):
        print("游戏初始化")

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
