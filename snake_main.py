import argparse
import game_utils
from snake_game import SnakeGame
from game_display import GameDisplay

def main_loop(gd: GameDisplay, args: argparse.Namespace) -> None:
    # INIT OBJECTS
    game = SnakeGame(args)
    gd.show_score(game.score)
    # DRAW BOARD
    game.draw_board(gd)
    # END OF ROUND 0
    prev_move = "Up"
    while not game.is_over():
        gd.show_score(game.score)
        # CHECK KEY CLICKS
        key_clicked = gd.get_key_clicked()
        game.read_key(key_clicked)
        # UPDATE OBJECTS
        if not key_clicked:
            key_clicked = prev_move
        game.update_objects(key_clicked, prev_move)
        prev_move = key_clicked if key_clicked else prev_move
        # DRAW BOARD
        game.draw_board(gd)
        # WAIT FOR NEXT ROUND:
        game.end_round()
        gd.end_round()
    print("done", game.is_over())

if __name__ == "__main__":
    print("You should run:\n"
          "> python game_display.py")
    main_loop(GameDisplay(10, 10, 10, 10, ""), {})
    
# TODO When creating snake, directly give the list of coordinates he's in