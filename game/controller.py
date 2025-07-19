from typing import Literal

from game.config import BOARD_SIZE, FILE_PATH
from game.model import GameBoard
from game.view import BoardRenderer

VALID_DIRECTIONS = ("up", "down", "left", "right")
Direction = Literal["up", "down", "left", "right"]


class GameController:
    def __init__(self, move: str | None = None) -> None:
        if move not in VALID_DIRECTIONS:
            return
        self.move: Direction = move
        self.board = GameBoard.load(FILE_PATH)
        self.renderer = BoardRenderer()

    def reset(self) -> None:
        """Reset the board: backs up the current file, creates a new board, and saves it."""
        board = GameBoard()
        board.add_random_tile()
        board.add_random_tile()
        board.save(FILE_PATH)
        print(f"New board saved to {FILE_PATH} (size: {BOARD_SIZE}x{BOARD_SIZE})")

    def run(self) -> None:
        if self.board.is_game_over():
            self.renderer.render(self.board.board, self.board.score)
            print("\nGame Over! Final score:", self.board.score)
            return

        moved = self.board.move(self.move)

        if moved:
            self.board.add_random_tile()
            self.board.save(FILE_PATH)
        else:
            print(f"\nInvalid move ({self.move}). Board didn't change.")

        self.renderer.render(self.board.board, self.board.score)

        if self.board.is_game_over():
            print("\nGame Over! Final score:", self.board.score)
