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

    def utility(self, state, player):
        """+1 if MAX wins, -1 if MIN wins, else 0."""
        return state.utility if player == 'MAX' else -state.utility

    def terminal_test(self, state):
        """Terminal when no objects remain."""
        return self._is_terminal_board(state.board)

    def display(self, state):
        """shows the board."""
        print("board: ", state.board)

    def play_game(self, *players):
        """Play a game while echoing each move"""
        state = self.initial
        # Print the initial board once, like the sample
        self.display(state)
        while True:
            for player in players:
                # Get a move from this player (AI or human).
                move = player(self, state)
                # Print the chosen move on its own line, e.g. "(0, 1)"
                print(move)
                # Apply it and show the new board.
                state = self.result(state, move)
                self.display(state)

                if self.terminal_test(state):
                    # Final display already printed; return winner utility for MAX.
                    return self.utility(state, self.to_move(self.initial))

    # -- Helpers --

    def _compute_moves(self, board):
        """Generate all legal (row, n) moves given the board."""
        moves = []
        for r, count in enumerate(board):
            for n in range(1, count + 1):
                moves.append((r, n))
        return moves

    def _is_terminal_board(self, board):
        """True iff all rows are empty."""
        return all(x == 0 for x in board)


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1])  # Creating the game instance
    # nim = GameOfNim(board=[7, 5, 3, 1])  # a larger tree to search

    # Sanity checks against the spec:
    print(nim.initial.board)   # must be [0, 5, 3, 1]
    print(nim.initial.moves)   # must be [(1,1)..(1,5), (2,1)..(2,3), (3,1)]
    print(nim.result(nim.initial, (1, 3)))

    # Computer moves first (alpha-beta) vs human (query_player).
    utility = nim.play_game(alpha_beta_player, query_player)
    if utility < 0:
        print("MIN won the game")
    else:
        print("MAX won the game")
