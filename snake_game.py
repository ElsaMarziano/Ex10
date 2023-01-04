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
#

    def __init__(self,width = 4,height = 4,apples = 4,round = -1,debug = None) -> None:
        self.__x = 0
        self.__y = 1
        self.__key_clicked = None


    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def update_objects(self)-> None:
        # advance snake
        # advance wall
        # check what happen if snake eat apple and wall hit snake
        # check eat apple
        # update score
        # add apple
        # add wall
        a =1


    def draw_board(self, gd: GameDisplay) -> None: 
        gd.draw_cell(self.__x, self.__y, "blue")


    def end_round(self) -> None:
        # Prepare new board
        pass

    def is_over(self) -> bool:
        return self.__is_over

