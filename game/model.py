import json
import random
from pathlib import Path
from typing import Literal

from game.config import BOARD_SIZE

Direction = Literal["up", "down", "left", "right"]


class GameBoard:
    def __init__(self, board: list[list[int]] | None = None, score: int = 0) -> None:
        self.size = BOARD_SIZE
        self.score = score
        self.board = board or [[0] * self.size for _ in range(self.size)]

    def move(self, direction: Direction) -> bool:
        original = [row[:] for row in self.board]

        if direction in {"up", "down"}:
            self._move_vertical(direction)
        elif direction in {"left", "right"}:
            self._move_horizontal(direction)

        return self.board != original

    def add_random_tile(self) -> None:
        empty = [(r, c) for r in range(self.size) for c in range(self.size) if self.board[r][c] == 0]
        if not empty:
            return
        r, c = random.choice(empty)
        self.board[r][c] = 2 if random.random() < 0.9 else 4

    def is_game_over(self) -> bool:
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return False
                if c < self.size - 1 and self.board[r][c] == self.board[r][c + 1]:
                    return False
                if r < self.size - 1 and self.board[r][c] == self.board[r + 1][c]:
                    return False
        return True

    def save(self, filepath: str) -> None:
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w") as f:
            json.dump({"board": self.board, "score": self.score}, f)

    @classmethod
    def load(cls, filepath: str) -> "GameBoard":
        path = Path(filepath)
        if not path.exists():
            board = cls()
            board.add_random_tile()
            board.add_random_tile()
            return board

        with path.open() as f:
            data = json.load(f)
        return cls(board=data["board"], score=data["score"])

    # Private move helpers below

    def _move_horizontal(self, direction: Direction) -> None:
        reverse = direction == "right"
        for r in range(self.size):
            row = self.board[r][::-1] if reverse else self.board[r]
            merged, new_score = self._merge_row(row)
            self.score += new_score
            self.board[r] = merged[::-1] if reverse else merged

    def _move_vertical(self, direction: Direction) -> None:
        reverse = direction == "up"
        for c in range(self.size):
            col = [self.board[r][c] for r in range(self.size)]
            col = col[::-1] if reverse else col
            merged, new_score = self._merge_row(col)
            self.score += new_score
            merged = merged[::-1] if reverse else merged
            for r in range(self.size):
                self.board[r][c] = merged[r]

    def _merge_row(self, row: list[int]) -> tuple[list[int], int]:
        new_row = [val for val in row if val != 0]
        merged_row = []
        score = 0
        skip = False
        for i in range(len(new_row)):
            if skip:
                skip = False
                continue
            if i + 1 < len(new_row) and new_row[i] == new_row[i + 1]:
                merged_row.append(new_row[i] * 2)
                score += new_row[i] * 2
                skip = True
            else:
                merged_row.append(new_row[i])
        merged_row.extend([0] * (self.size - len(merged_row)))
        return merged_row, score
