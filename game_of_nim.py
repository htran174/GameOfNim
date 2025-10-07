# game_of_nim.py
from games import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
        A state has the player to move, a cached utility, a list of moves in
        the form of a list of (x, y) positions, and a board, in the form of
        a list with number of objects in each row."""

    def __init__(self, board=[3, 1]):
        board = list(board)
        self.initial = GameState(
            to_move='MAX',
            utility=0,
            board=board,
            moves=self._compute_moves(board)
        )

    # -- Core Game interface --

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""

        return state.moves

    def result(self, state, move):
        """Apply move (row, n) and return the resulting GameState. Assumes move is valid."""

        r, n = move
        new_board = list(state.board)
        new_board[r] -= n

        mover = state.to_move
        to_move = 'MIN' if mover == 'MAX' else 'MAX'

        if self._is_terminal_board(new_board):
            winner = to_move
            utility = 1 if winner == 'MAX' else -1
            moves = []

        else:
            utility = 0
            moves = self._compute_moves(new_board)

        return GameState(
            to_move=to_move,
            utility=utility,
            board=new_board,
            moves=moves
        )

    