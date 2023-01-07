import wall as Wall
from helper import *
from snake import Snake
import copy
from game_utils import get_random_apple_data


class Board:
    # need to add debug and round?
    def __init__(self, snake_locations: list, width: int = 30, height: int = 30, apples: int = 3, walls: int = 2):
        #TODO do every variable private
        self.board: list = self.create_board(width, height, snake_locations)
        self.__wall_list = list()  # current walls on the board
        self.apples_on_board: int = 0  # current apples on the board
        self.__max_walls: int = walls  # num of walls that can exist on board
        # how we transfer the apples on board from board to board? we need another func
        self.__max_apples: int = apples  # num of apple that can exist on board
        self.width: int = width 
        self.height: int = height
        
        
    def create_board(self, width, height, snake_locations):
        """ This function creates the board on the very first time """
        my_board = [[("_" if (col, line) not in snake_locations else "S") for col in range(width)] for line in range(height)]
        return my_board
        
        
    def add_wall(self, wall: Wall):  # only add wall,not place them
        """ This function adds a new wall to the wall_list """
        if len(self.__wall_list) < self.__max_walls:
            middle_location = wall.location
            # Check if the coordinate received is inside the limits of the board
            if check_location(self.height, self.width, middle_location):
                for location in wall.get_wall_locations():
                    # If wall appears on snake, return
                    if check_location(self.height, self.width, location) :
                        if self.board[location[1]][location[0]] == "S":
                            return
                self.__wall_list.append(wall)  # do you append a wall if middle c


    def add_apple(self, location: tuple):
        """ This function tries to add an apple """
        if self.apples_on_board < self.__max_apples:
            if check_location(self.height, self.width, location):  # check if apple in limit of the board
                if self.board[location[1]][location[0]] == "_":  # fall on empty place
                    self.apples_on_board += 1
                    self.board[location[1]][location[0]] = "A"



    def move_walls_in_board(self):
        """ Change coordinates of every wall on the list """
        for wall in self.__wall_list:
            old_location = wall.get_wall_locations()
            for loc in old_location:
                if check_location(self.height, self.width, loc):
                    self.board[loc[1]][loc[0]] = "_"
            wall.move_wall()



    def place_walls(self):
        """ This function handles the movement of all walls on the board """
        wall_to_add = 0
        for wall in self.__wall_list:
            locations_not_in_board = 0
            wall_list_locations = wall.get_wall_locations()
            for location in wall_list_locations:
                # TODO Try to do this without locations_not_in_board and check for old loc
                if check_location(self.height, self.width,location):
                    if self.board[location[1]][location[0]] == "A":
                        #! @Amitai Is this okay?
                        self.apples_on_board -= 1
                        self.add_apple(get_random_apple_data())
                    self.board[location[1]][location[0]] = "W"
                else:
                    locations_not_in_board += 1
            if locations_not_in_board == wall.length:
                # remove the wall that all locations not in board
                self.__wall_list.remove(wall)
                wall_to_add += 1
        return wall_to_add
                
    # For place_walls: maybe go over the locations of each wall, if one of them is in the board get out of the for loop,
    # else continue until we get to the last location and then remove wall


    def place_snake(self, old_locations: list, new_loc: tuple = None):
        """ This function updates the snake's location """
        # Erase the places the snake isn't in anymore
        if old_locations != [[]]: #? Weird that we can't check with length. Check this during code review
            for old_loc in old_locations:
                self.board[old_loc[1]][old_loc[0]] = "_"
        # Check if snake is still in the board
        if new_loc and check_location(self.height, self.width, new_loc):
            self.board[new_loc[1]][new_loc[0]] = "S"
        else:
            return "DEAD"


    def snake_hits_wall(self, snake: Snake):
        """ This function checks if the snake hits a wall, and if so if he's dead or just injured """
        for wall in self.__wall_list:
            coordinates = snake.get_location()
            wall_locations = wall.get_wall_locations()
            # Check if snake is dead
            if wall_locations[0] in snake.return_head_and_neck() or wall_locations[-1] in snake.return_head_and_neck():
                return True
            # Check if snake is injured and if so, update size
            #? Maybe put this in a function to avoid duplicate - code review
            elif wall_locations[0] in coordinates:
                locations = snake.update_size(wall_locations[0])
                self.place_snake(locations)
            elif wall_locations[-1] in coordinates:
                locations = snake.update_size(wall_locations[-1])
                self.place_snake(locations)


    #TODO Check if we need this
    def mirror_board_upside_down(self):
        # Create a reversed copy of the matrix using slicing
        reversed_board = copy.deepcopy(self.board)[::-1]
        return reversed_board


           
                



