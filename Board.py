class Board:
    def __init__(self,width= 40,height = 30 ,apples = 3, walls = 2 ):# need to add debug and round?
        self.board = [["_" for column in range(width)] for row in range(height)]
        self.wall_list = list() #current walls that in board
        self.apples_on_board = 0  #current apples that in board
        self.walls = walls #num of walls that can exist on board
        self.apples = apples #num of apple that can exist on board
        self.width = width
        self.height = height

    def add_wall(self,Wall): #only add wall,not place them
        if len(self.wall_list) < self.walls: # when adding rounds put another if here to check if round is even
            middle_location = Wall.location
            if middle_location[0] < self.height and middle_location[1] < self.height: #check if wall in limit
                self.wall_list.append(Wall) # do you append a wall if middle c

    def add_apple(self,location):
        if self.apples_on_board < self.apples:
            if location[0] < self.height and location[1] < self.height:  # check if apple in limit
                if self.board[location[0]][location[1]] == "_": # fall on empty place
                    self.apples_on_board += 1
                    self.board[location[0]][location[1]] = "A"





    def move_walls_in_board(self): # move the wall in list so when placeing them they will be in the right place
        for wall in self.wall_list:
            wall.move_wall()


    def place_walls(self): #remember to move walls in board first
        for wall in self.wall_list:
            locations_not_in_board = 0
            wall_list_locations = wall.get_wall_locations()
            for location in wall_list_locations:
                if location[0] < self.height and location[1] < self.height:
                    self.board[location[0]][location[1]] = "W"
                else:
                    locations_not_in_board += 1
            if locations_not_in_board == wall.length:
                self.wall_list.remove(wall) # remove the wall that all locations not in board
                # To do check if remove can know the different between walls!






