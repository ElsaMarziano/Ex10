from typing import Optional
from game_display import GameDisplay
import math
from classes.board import  Board
from classes.snake import Snake
from game_utils import get_random_apple_data
from classes.wall import Wall
from game_utils import get_random_wall_data




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
        self.__round = 0
        self.__is_over = False



    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def update_objects(self,move)-> None:
        # Moves snake and check if he's dead
        snake_status:  dict["is_dead": bool, "old_loc": tuple, "new_loc": tuple] = self.__snake.move_snake(move)
        self.__board.place_snake(snake_status.old_loc, snake_status.new_loc)
        if snake_status.is_dead:
            self.__is_over = True
            return
        self.__board.move_walls_in_board() # advance wall
        self.__board.place_walls()
        # check if dead
        # if snake eat apple
        # self.__snake.growing()
        # self.add_score()
        self.__board.add_apple(get_random_apple_data())
        if self.__round % 2 == 0:
            self.__board.add_wall(Wall())
        self.__board.place_walls()
        # add the apples
        # add apple
        # add wall
        
        
    def add_score(self):
        self.__score += int(math.sqrt(self.__snake.get_size()))



    def draw_board(self, gd: GameDisplay) -> None: 
        gd.draw_cell(self.__x, self.__y, "blue")

    def end_round(self) -> None:
        self.__round += 1

    def is_over(self) -> bool:
        return self.__is_over

