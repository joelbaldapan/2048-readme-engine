import sys

from game.controller import GameController

VALID_DIRECTIONS = {"up", "down", "left", "right"}


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage:")
        print("  python main.py <direction>     # up/down/left/right")
        print("  python main.py reset           # start new game")
        return

    arg = sys.argv[1].lower()

    if arg == "reset":
        GameController().reset()
        return

    if arg not in VALID_DIRECTIONS:
        print(f"Invalid direction: '{arg}'. Must be one of: up, down, left, right")
        return

    controller = GameController(move=arg)
    controller.run()


if __name__ == "__main__":
    main()
