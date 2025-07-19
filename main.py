import sys

from game.controllers.controller import GameController

VALID_DIRECTIONS = {"up", "down", "left", "right"}


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage:")
        print("  python main.py <username> <direction>")
        print("  python main.py reset")
        return

    username = sys.argv[1]
    arg = sys.argv[2].lower()

    if arg == "reset":
        GameController().reset()
        return

    if arg not in VALID_DIRECTIONS:
        print(f"Invalid direction: '{arg}'. Must be one of: up, down, left, right")
        return

    controller = GameController(username=username, move=arg)
    controller.run()


if __name__ == "__main__":
    main()
