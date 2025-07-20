from typing import Literal

from game.config import BOARD_SIZE, GAME_FILE_PATH
from game.models.game_board import GameBoard
from game.models.user_stats import UserStats
from game.views.view import BoardRenderer

VALID_DIRECTIONS = ("up", "down", "left", "right")
Direction = Literal["up", "down", "left", "right"]


class GameController:
    def __init__(self, username: str = "joelbaldapan", move: str | None = None) -> None:
        self.username = username
        self.renderer = BoardRenderer()
        self.board = GameBoard.load(GAME_FILE_PATH)
        if move in VALID_DIRECTIONS:
            self.move: Direction = move

    def reset(self) -> None:
        """Reset the board: backs up the current file, creates a new board, and saves it."""
        board = GameBoard()
        board.add_random_tile()
        board.add_random_tile()
        board.save(GAME_FILE_PATH, username=self.username)
        self.renderer.render_to_svg(self.board.board, self.board.total_score)
        print(f"New board saved to {GAME_FILE_PATH} (size: {BOARD_SIZE}x{BOARD_SIZE})")

    def run(self) -> None:
        moved = self.board.move(self.move)

        if moved:
            self.board.add_random_tile()
            self.board.save(GAME_FILE_PATH, username=self.username)

            if self.username:
                UserStats.update(self.username, self.board.score)
        else:
            print(f"\nInvalid move ({self.move}). Board didn't change.")

        self.renderer.render(self.board.board, self.board.total_score)
        self.renderer.render_to_svg(self.board.board, self.board.total_score)

        if self.board.is_game_over():
            self.renderer.render(self.board.board, self.board.total_score)
            print("\nGame Over! Final score:", self.board.total_score)
