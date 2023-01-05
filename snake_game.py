from typing import Optional
from game_display import GameDisplay
import math
from classes.board import  Board
from classes.snake import Snake
from game_utils import get_random_apple_data
from classes.wall import Wall
from game_utils import get_random_wall_data
from helper.constants import COLORS, MOVES
from helper.helper import check_direction
from helper.helper import make_something_move
from helper.helper import check_location




class SnakeGame:
    #TODO Function that adapt our board to the graphic one ??
    #TODO Add apple if wall destroys it
    #TODO When adding wall, check if it's not on the snake
    #TODO Check why check_direction doesn't work (it lets the snake go in that direction and then kills it cause it ate itself)
    #TODO Code review!!!!!!! + add comments
    #TODO Check if we need to paint the elements one by one
    #TODO upload score when apple eaten
    #TODO dont commit suicide
    #TODO Default to all parameters



    def __init__(self, args) -> None:
        WIDTH_SNAKE = args.width // 2
        HEIGHT_SNAKE = args.height // 2
        self.__x = 5
        self.__y = 5
        self.__key_clicked = None
        self.score = 0
        self.__snake = Snake([(WIDTH_SNAKE,HEIGHT_SNAKE - 2),(WIDTH_SNAKE,HEIGHT_SNAKE - 1), (WIDTH_SNAKE,HEIGHT_SNAKE)])
        self.__board = Board(self.__snake.get_location(),args.width, args.height, args.apples, args.walls)
        self.__round = args.rounds
        self.__is_over = False



    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def update_objects(self, move)-> None:
        # Moves snake and check if he's dead
        # TODO NEED to check if after the head move if its out of limit
        snake_head_after_move = make_something_move(self.__snake.get_head(), MOVES[move]) # get head after move
        
        if check_location(self.__board.height, self.__board.width, snake_head_after_move): # check if next step is out of limit
            need_to_grow = self.__board.board[snake_head_after_move[1]][snake_head_after_move[0]] == "A" #check if head is on apple
        snake_status:  dict = self.__snake.move_snake(move) #move first before tell him to grow if needed
        if self.__board.place_snake([snake_status["old_loc"]], snake_status["new_loc"]) == "DEAD" or snake_status["is_dead"]:
            self.__is_over = True
            return
        if need_to_grow: # grow if need
            self.__snake.growing()
            self.__board.apples_on_board -= 1
            self.add_score()
        self.__board.move_walls_in_board() # advance wall
        self.__board.place_walls() #TODO if wall hit apple, add one miyad
        
        if self.__board.snake_hits_wall(self.__snake):
            self.__is_over = True
            return
        # check if dead
        # if snake eat apple
        # self.add_score()
        self.__board.add_apple((20,20))
        if self.__round % 2 == 0:
            self.__board.add_wall(Wall())
        self.__board.place_walls()
        # add the apples
        # add apple
        # add wall
        
        
    def add_score(self):
        self.score += int(math.sqrt(self.__snake.get_size()))

    def check_collision(self, head: tuple): #TODO Check if we need this function
        if head[0] >= self.__board.height or head[0] >= self.__board.width or head[1] <= 0 or head[1] <= 0  :
            self.__is_over = True
        if self.__board[head[1]][head[0]] == "W":
            self.__is_over = True



    def draw_board(self, gd: GameDisplay) -> None:
        for height, _ in enumerate(self.__board.board):
            for width, _ in enumerate(self.__board.board[0]):
                color = self.__board.board[height][width]
                if color != "_":
                    gd.draw_cell(width, height, COLORS[color])

    def end_round(self) -> None:
        self.__round += 1

    def is_over(self) -> bool:
        return self.__is_over
