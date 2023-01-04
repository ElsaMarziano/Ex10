from helper.constants import *
from helper.helper import *

class Snake:
    def __init__(self, locations: list, color: str):
        self.size: int = SNAKE_SIZE
        self.location: list = locations # Head is always the last coordinate (index -1)
        self.__need_to_grow = 0
        
    def move_snake(self, direction: str):
        is_dead = False
        old_loc = None
        ''' This function makes the snake move in the desired direction, and handles its grow if needed '''
        if not check_direction(MOVES[direction], self.location[-1], self.location[-2]): return # Checks if the direction isn't opposite the snake
        current_head = self.location[-1]
        # Handle snake growth if needed
        if self.__need_to_grow == 0:
            old_loc = self.location[0]
            del self.location[0]
        else:
            self.size += 1
            self.__need_to_grow -= 1
        # Snake moves
        new_head = make_something_move(current_head, MOVES[direction])
        self.location.append(new_head)
        
        if new_head in self.location: # If the snake hurts himself, you lose
            is_dead = True
            
        return {"is_dead": is_dead, "old_loc": old_loc, "new_loc": new_head}
        
    def return_head_and_neck(self):
        ''' This function returns the coordinates of the head and "neck" of the snake - that is, all of the coordinates
        who will kill the snake if a wall touches them '''
        return self.location[-1:-3:-1]


    def get_size(self):
        return self.__size
    
    def growing(self):
        self.__need_to_grow += 3