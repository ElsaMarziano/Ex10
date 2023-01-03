from game_utils import get_random_wall_data
from helper.constants import MOVES
from helper.helper import make_something_move

class Wall:
    """ class of wall default"""

    def __init__(self, name: str, length: int = 3): # need to check how we get location and movement(i think its one tuple)
        WALL_DATA = get_random_wall_data()
        # TODO Check if we need to tell the walls apart
        self.name = name # to tell the walls apart
        self.length = length # default is 3
        self.location = (WALL_DATA[0], WALL_DATA[1]) # middle location, (row,col)
        self.movement = WALL_DATA[2] #"Up","Down","Left","Right"

    def get_wall_locations(self):
        """ Return list of locations the wall is in """
        list_of_locations = [] #  list with 3 tuples (row,col)
        middle_row = self.location[0] # x
        middle_col = self.location[1] #y
        # TODO Check if there's a way to do this more effectively with the make_something_move function
        if self.movement == "Up" or self.movement == "Down":
            list_of_locations = [(middle_row - 1,middle_col),(middle_row,middle_col),(middle_row + 1,middle_col)]
        elif self.movement == "Right" or self.movement == "Left":
            list_of_locations = [(middle_row,middle_col-1), (middle_row, middle_col), (middle_row , middle_col + 1)]
        return list_of_locations



    def move_wall(self):
        """ Moves the wall in the right direction """
        self.location = make_something_move(self.location, MOVES[self.movement])