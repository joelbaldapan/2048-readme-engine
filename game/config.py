BOARD_SIZE: int = 5
GAME_FILE_PATH: str = "data/current_game.json"
BOARD_FILE_PATH: str = "board/current_board.svg"

# SVG Rendering Constants
SVG_TILE_SIZE = 100
SVG_BORDER_RADIUS = 8
SVG_GAP = 10
SVG_FONT_SIZE = 48
SVG_SCORE_HEIGHT = 60

# VANILLA COLORS
SVG_BACKGROUND_COLOR = "#a6a6a6"
SVG_EMPTY_TILE_COLOR = "#c9c9c9"
SVG_TEXT_COLOR_WHITE = "#f9f6f2"
SVG_TEXT_COLOR_BLACK = "#121211"
_SVG_TILE_COLORS = {
    0: SVG_EMPTY_TILE_COLOR,
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf73",
    256: "#edcc62",
    512: "#edc850",
    1024: "#eec745",
    2048: "#eec434",
}
_SVG_FALLBACK_TILE_COLORS = "#3c3a32"


# BLUE COLORS
SVG_BACKGROUND_COLOR = "#113c7e"
SVG_EMPTY_TILE_COLOR = "#275a6f"
SVG_TEXT_COLOR_WHITE = "#f9f6f2"
SVG_TEXT_COLOR_BLACK = "#121211"
SVG_TILE_COLORS = {
    0: SVG_EMPTY_TILE_COLOR,
    2: "#b2dbdd",
    4: "#afdcde",
    8: "#5ac4c2",
    16: "#00adb1",
    32: "#008a96",
    64: "#00747e",
    128: "#0073a1",
    256: "#0072bc",
    512: "#0083cd",
    1024: "#2d5e9f",
    2048: "#2c5597",
    4096: "#264678",
    8192: "#1C3762",
    16384: "#1C2F4F",
    32768: "#10203A",
}
SVG_FALLBACK_TILE_COLORS = "#08101D"
