import classes.wall as Wall
from helper.helper import *


class Board:
    # need to add debug and round?
    def __init__(self, width: int = 40, height: int = 30, apples: int = 3, walls: int = 2):
        self.board: list = [["_" for _ in range(width)] for _ in range(height)]
        self.wall_list = list()  # current walls on the board
        self.apples_on_board: int = 0  # current apples on the board
        self.max_walls: int = walls  # num of walls that can exist on board
        # how we transfer the apples on board from board to board? we need another func
        self.max_apples: int = apples  # num of apple that can exist on board
        self.width: int = width 
        self.height: int = height



    def add_wall(self, wall: Wall):  # only add wall,not place them
        """ This function adds a new wall to the wall_list """
        # TODO check if round is even
        if len(self.wall_list) < self.max_walls:
            middle_location = wall.location
            # TODO Check if Wall appears on the snake, and if so return
            # check if wall in limit
            if check_location(self.height, self.width, middle_location):
                self.wall_list.append(wall)  # do you append a wall if middle c


    def add_apple(self, location: tuple):
        """ This function tries to add an apple """
        if self.apples_on_board < self.max_apples:
            if check_location(self.height, self.width, location):  # check if apple in limit of the board
                if self.board[location[0]][location[1]] == "_":  # fall on empty place
                    self.apples_on_board += 1
                    self.board[location[0]][location[1]] = "A"


    def move_walls_in_board(self):
        """ Change coordinates of every wall on the list """
        for wall in self.wall_list:
            wall.move_wall()


    def place_walls(self):  # !Remember to move walls in board before the apples
        """ This function handles the movement of all walls on the board """
        for wall in self.wall_list:
            locations_not_in_board = 0
            wall_list_locations = wall.get_wall_locations()
            for location in wall_list_locations:
                # TODO Try to do this without locations_not_in_board
                if check_location(self.height, self.width):
                    self.board[location[0]][location[1]] = "W"
                else:
                    locations_not_in_board += 1
            if locations_not_in_board == wall.length:
                # remove the wall that all locations not in board
                self.wall_list.remove(wall)
                
    # For place_walls: maybe go over the locations of each wall, if one of them is in the board get out of the for loop,
    # else continue until we get to the last location and then remove wall

