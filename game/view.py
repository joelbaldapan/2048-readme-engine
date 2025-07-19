from game.config import BOARD_SIZE


class BoardRenderer:
    def render(self, board: list[list[int]], score: int) -> None:
        border = BOARD_SIZE * 7
        print("\n" + "=" * border)
        print(f" SCORE: {score}")
        print("=" * border)

        for row in board:
            rendered_row = " | ".join(f"{num or '':^4}" for num in row)
            print(f"| {rendered_row} |")
            print("-" * border)
