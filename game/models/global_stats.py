import json
from pathlib import Path
from typing import List

from game.config import GLOBAL_STATS_FILE_PATH, BOARD_SIZE


class GlobalStats:
    @staticmethod
    def update(score: int, board: List[List[int]]) -> None:
        """
        Update global game statistics including high score, games finished, and largest tile.
        Create the stats file with default values if it doesn't exist.
        """
        stats_path = Path(GLOBAL_STATS_FILE_PATH)
        stats = {
            "high_score": 0,
            "games_finished": 0,
            "largest_tile": 0,
        }

        stats_path.parent.mkdir(parents=True, exist_ok=True)

        if stats_path.exists():
            with stats_path.open("r") as file:
                try:
                    loaded_stats = json.load(file)
                    stats.update(loaded_stats) # Update with existing data
                except json.JSONDecodeError:
                    # Handle empty or corrupted JSON file
                    print(f"Warning: {GLOBAL_STATS_FILE_PATH} is empty or corrupted. Initializing with default stats.")
                    pass # stats already has default values

        # Update games_finished
        stats["games_finished"] += 1

        # Update high_score
        if score > stats["high_score"]:
            stats["high_score"] = score

        # Calculate and update largest_tile
        current_largest_tile = 0
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                if board[r][c] > current_largest_tile:
                    current_largest_tile = board[r][c]

        if current_largest_tile > stats["largest_tile"]:
            stats["largest_tile"] = current_largest_tile

        with stats_path.open("w") as file:
            json.dump(stats, file, indent=2)

