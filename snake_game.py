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
# TODO put defult to all para
# TODO to add an apple if a wall destroy it
# TODO check if wall cut snake or kill it
# TODO check if snake hit limit
# TODO think how the game start
# TODO make str to board
# TODO eat apple
# TODO cut to half, update snake, update board


    def __init__(self, args) -> None:
        self.__x = 5
        self.__y = 5
        self.__key_clicked = None
        self.__score = 0
        self.__board = Board(args.width, args.height, args.apples, args.walls)
        self.__snake:Snake = Snake([(self.__board.height -2 ,self.__board.width),(self.__board.height-1,self.__board.width),\
                              (self.__board.height,self.__board.width)])
        self.__round = 0
        self.__is_over = False



    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def update_objects(self,move)-> None:
        # Moves snake and check if he's dead
        snake_status:  dict = self.__snake.move_snake(move)
        if self.__board.place_snake([snake_status.old_loc], snake_status.new_loc) or snake_status.is_dead:
            self.__is_over = True
            return

        self.__board.move_walls_in_board() # advance wall
        self.__board.place_walls() #TODO if wall hit apple, add one miyad

        if  self.__board.snake_hits_wall(self.__snake):
            self.__is_over = True
            return
        self.__board.place_walls()
        self.check_collusion(self.__snake.get_head())
        # check if dead
        # if snake eat apple
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

    def check_collusion(self, head: tuple):
        if head[0] >= self.__board.height or head[1] >= self.__board.width or head[0] <= 0 or head[1] <= 0  :
            self.__is_over = True
        if self.__board[head[0]][head[1]] == "W":
            self.__is_over = True



    def draw_board(self, gd: GameDisplay) -> None: 
        gd.draw_cell(self.__x, self.__y, "blue")

    def end_round(self) -> None:
        self.__round += 1

    def is_over(self) -> bool:
        return self.__is_over

