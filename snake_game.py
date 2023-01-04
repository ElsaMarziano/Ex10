from typing import Optional
from game_display import GameDisplay
import math
from classes.board import  Board
from classes.snake import Snake


class SnakeGame:
# TODO check how draw cell works
# TODO check where to put score
# TODO put defult to all para
# TODO to add an apple if a wall destroy it
# TODO check if wall cut snake or kill it
# TODO check if snake hit limit
# TODO put wall only if round is even
# TODO think how the game start
# TODO update how much is left for the snake to grow
# TODO make str to board
#

    def __init__(self,width,height,apples,debug) -> None:
        self.__x = 5
        self.__y = 5
        self.__key_clicked = None
        self.__score = 0
        self.__board = Board()
        self.__snake:Snake = Snake([(self.__board.height -2 ,self.__board.width),(self.__board.height-1,self.__board.width),\
                              (self.__board.height,self.__board.width)])



    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def update_objects(self,move)-> None:
        self.__snake.move_snake(move,False)
        self.__board
        # advance snake
        # advance wall
        # check what happen if snake eat apple and wall hit snake
        # check eat apple
        # update score
        # add apple
        # add wall
    def add_score(self):
        self.__score += int(math.sqrt(self.__snake.get_size()))




    def draw_board(self, gd: GameDisplay) -> None:
        gd.draw_cell(self.__x, self.__y, "blue")

    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        return self.__is_over

