'''
Name:    Hien Tran
CWID:    830889556
Class:   CPSC 481-02 17420
'''

# game_of_nim.py
from games import *
class GameOfNim(Game):
    """Game of Nim with first player 'MAX'.
    State is a GameState(to_move, utility, board, moves) where:
      - board: list[int] with the count of objects in each row
      - moves: list[(row, n)] of legal removals (n >= 1) from a single row
    Rules (misère Nim for this assignment):
      - Two players alternate removing >=1 objects from exactly one row.
      - The player who removes the last object LOSES.
    """

    def __init__(self, board=[3, 1]):
        # Ensure we store a copy and precompute legal moves for the initial state
        board = list(board)
        self.initial = GameState(
            to_move='MAX',
            utility=0,
            board=board,
            moves=self._compute_moves(board)
        )

   


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1])  # Creating the game instance
    # nim = GameOfNim(board=[7, 5, 3, 1])  # a much larger tree to search
    print(nim.initial.board)   # must be [0, 5, 3, 1]
    print(nim.initial.moves)   # must be [(1,1)..(1,5), (2,1)..(2,3), (3,1)]
    print(nim.result(nim.initial, (1, 3)))
    utility = nim.play_game(alpha_beta_player, query_player)  # computer moves first
    if utility < 0:
        print("MIN won the game")
    else:
        print("MAX won the game")
