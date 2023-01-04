from helper.constants import *
from helper.helper import *

class Snake:
    def __init__(self, locations: list, color: str):
        self.__size: int = SNAKE_SIZE
        # Not sure if we need a direction
        #self.direction: str = direction # ? Maybe pass the tuple matching the direction, and not the string
        self.__location: list = locations # Head is always the last coordinate (index -1)
        
    def move_snake(self, direction: str, is_growing: bool):
        ''' This function makes the snake move in the desired direction, and handles its grow if needed '''
        if not check_direction(MOVES[direction], self.location[-1], self.location[-2]): return # Checks if the direction isn't opposite the snake
        CURRENT_HEAD = self.location[-1]
        # Handle snake growth if needed
        if not is_growing:
            del self.location[0]
        else:
            self.size += 1
        # Snake moves
        NEW_HEAD = make_something_move(CURRENT_HEAD, MOVES[direction])
        self.location.append(NEW_HEAD)
        if NEW_HEAD in self.location: # If the snake hurts himself, you lose
            return "DEAD"
        
    def return_head_and_neck(self):
        ''' This function returns the coordinates of the head and "neck" of the snake - that is, all of the coordinates
        who will kill the snake if a wall touches them '''
        return self.location[-1:-3:-1]


    def get_size(self):
        return self.__size
    
snake = Snake([(3, 0), (3, 1), (3, 2)], COLORS[0])
snake.move_snake("RIGHT", False)
print(snake.location)
        
