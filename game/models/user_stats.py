import json
from pathlib import Path

from game.config import USER_STATS_PATH


class UserStats:
    @staticmethod
    def update(username: str, score: int) -> None:
        stats = {}

        path = Path(USER_STATS_PATH)
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            with open(USER_STATS_PATH) as file:
                stats = json.load(file)

        user_data = stats.get(username, {"moves": 0, "total_score": 0})
        user_data["moves"] += 1
        user_data["total_score"] += score

        stats[username] = user_data

        with open(USER_STATS_PATH, "w") as file:
            json.dump(stats, file, indent=2)
