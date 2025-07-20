import sys

from game.controllers.controller import GameController

VALID_DIRECTION_MAP = {
    "u": "up",
    "d": "down",
    "l": "left",
    "r": "right",
}


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage:")
        print("  python main.py <username> <command>")
        print("  python main.py reset")
        return

    raw_username = sys.argv[1]
    arg = sys.argv[2].lower()

    if arg == "reset":
        GameController().reset()
        return

    username = f"@{raw_username}"
    direction = VALID_DIRECTION_MAP.get(arg)
    if not direction:
        print(f"Invalid command: '{arg}'. Must be one of: u, d, l, r, or 'reset'")
        return

    controller = GameController(username=username, move=arg)
    controller.run()


if __name__ == "__main__":
    main()
