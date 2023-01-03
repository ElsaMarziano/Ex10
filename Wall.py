class Wall:
    """ class of wall diff"""

    def __init__(self, name, location, movement,length=3,):
        self.name = name # to know the walls apart
        self.length = length #diff is 3
        self.location = location #middle location, (x,y)
        self.movement = movement #"Up","Down","Left","Right"

    def get_wall_locations(self):
        list_of_locations = [] #  list with 3 tuples (row,col)
        middle_row = self.location[0] # x
        middle_col = self.location[1] #y
        if self.movement == "Up" or self.movement == "Down":
            list_of_locations = [(middle_row - 1,middle_col),(middle_row,middle_col),(middle_row + 1,middle_col)]
        elif self.movement == "Right" or self.movement == "Left":
            list_of_locations = [(middle_row,middle_col-1), (middle_row, middle_col), (middle_row , middle_col + 1)]
        return list_of_locations



    def move_wall(self):
        if self.movement == "Right":
            self.location = (self.location[0], self.location[1] + 1)
        elif self.movement == "Left":
            self.location = (self.location[0], self.location[1] - 1)
        elif self.movement == "Up":
            self.location = (self.location[0]+1, self.location[1])
        elif self.movement == "Down":
            self.location = (self.location[0] - 1, self.location[1])



