from typing import Optional
from game_display import GameDisplay
import math
from classes.board import  Board
from classes.snake import Snake
from game_utils import get_random_apple_data
from classes.wall import Wall
from game_utils import get_random_wall_data
from helper.constants import COLORS




class SnakeGame:
    #TODO: Start board: need to think when to create board
    #TODO Function that adapt our board to the graphic one
    #TODO Add apple if wall destroys it

    #TODO Default to all parameters



    def __init__(self, args) -> None:
        WIDTH_SNAKE = args.width // 2
        HEIGHT_SNAKE = args.height //2
        self.__x = 5
        self.__y = 5
        self.__key_clicked = None
        self.__score = 0
        self.__snake:Snake = Snake([(HEIGHT_SNAKE - 2,WIDTH_SNAKE),(HEIGHT_SNAKE -1,WIDTH_SNAKE),\
                              (HEIGHT_SNAKE,WIDTH_SNAKE)])
        self.__board = Board(self.__snake.get_location(), args.width, args.height, args.apples, args.walls)
        self.__round = args.rounds
        self.__is_over = False



    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def update_objects(self,move)-> None:
        if not move: move = "UP"
        # Moves snake and check if he's dead
        snake_status:  dict = self.__snake.move_snake(move)
        if self.__board.place_snake([snake_status["old_loc"]], snake_status["new_loc"]) or snake_status["is_dead"]:
            self.__is_over = True
            return
        
        self.__board.move_walls_in_board() # advance wall
        self.__board.place_walls() #TODO if wall hit apple, add one miyad
        
        if  self.__board.snake_hits_wall(self.__snake):
            self.__is_over = True
            return
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
        if head[0] >= self.__board.__height or head[1] >= self.__board.__width or head[0] <= 0 or head[1] <= 0  :
            self.__is_over = True
        if self.__board[head[0]][head[1]] == "W":
            self.__is_over = True



    def draw_board(self, gd: GameDisplay) -> None:
        #print(self.__board.board)
        for height, _ in enumerate(self.__board.board):
            for width, _ in enumerate(self.__board.board[0]):
                color = self.__board.board[height][width]
                print(color)
                if color != "_":
                    gd.draw_cell(height, width, COLORS[color])

    def end_round(self) -> None:
        self.__round += 1

    def is_over(self) -> bool:
        return self.__is_over
