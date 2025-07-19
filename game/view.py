from pathlib import Path

from game.config import (
    BOARD_FILE_PATH,
    BOARD_SIZE,
    SVG_BACKGROUND_COLOR,
    SVG_BORDER_RADIUS,
    SVG_FONT_SIZE,
    SVG_GAP,
    SVG_SCORE_HEIGHT,
    SVG_TEXT_COLOR,
    SVG_TILE_COLORS,
    SVG_TILE_SIZE,
)


class BoardRenderer:
    def render(self, board: list[list[int]], score: int) -> None:
        """Render the game board to the console."""
        border = BOARD_SIZE * 7
        print("\n" + "=" * border)
        print(f" SCORE: {score}")
        print("=" * border)

        for row in board:
            rendered_row = " | ".join(f"{num or '':^4}" for num in row)
            print(f"| {rendered_row} |")
            print("-" * border)

    def render_to_svg(self, board: list[list[int]], score: int) -> None:
        """Render the game board as an SVG file."""
        width = BOARD_SIZE * SVG_TILE_SIZE + (BOARD_SIZE + 1) * SVG_GAP
        height = BOARD_SIZE * SVG_TILE_SIZE + (BOARD_SIZE + 1) * SVG_GAP + SVG_SCORE_HEIGHT

        svg_elements = []

        # SVG header and background
        svg_elements.extend([
            f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
            f'xmlns="http://www.w3.org/2000/svg">',
            f'<rect x="0" y="0" width="{width}" height="{height}" fill="{SVG_BACKGROUND_COLOR}"/>',
            # Score display
            f'<text x="{width / 2}" y="{SVG_SCORE_HEIGHT / 2 + SVG_FONT_SIZE / 3}" '
            f'font-family="Arial, sans-serif" font-size="{SVG_FONT_SIZE * 0.7}" fill="#fff" '
            f'text-anchor="middle">Score: {score}</text>',
        ])

        # Draw tiles
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                x = c * SVG_TILE_SIZE + (c + 1) * SVG_GAP
                y = r * SVG_TILE_SIZE + (r + 1) * SVG_GAP + SVG_SCORE_HEIGHT
                tile_value = board[r][c]
                tile_color = SVG_TILE_COLORS.get(tile_value, "#3c3a32")  # Default for values > 2048
                text_color = (
                    SVG_TEXT_COLOR if tile_value not in {8, 16, 32, 64, 128, 256, 512, 1024, 2048} else "#f9f6f2"
                )  # Adjust text color for darker tiles

                # Rectangle for the tile
                svg_elements.append(
                    f'<rect x="{x}" y="{y}" width="{SVG_TILE_SIZE}" height="{SVG_TILE_SIZE}" '
                    f'rx="{SVG_BORDER_RADIUS}" ry="{SVG_BORDER_RADIUS}" fill="{tile_color}"/>',
                )

                # Text for the tile value
                if tile_value != 0:
                    # Adjust font size for larger numbers
                    current_font_size = SVG_FONT_SIZE
                    if tile_value >= 1000:
                        current_font_size *= 0.7
                    elif tile_value >= 100:
                        current_font_size *= 0.8

                    svg_elements.append(
                        f'<text x="{x + SVG_TILE_SIZE / 2}" '
                        f'y="{y + SVG_TILE_SIZE / 2 + current_font_size / 3}" '
                        f'font-family="Arial, sans-serif" font-size="{current_font_size}" '
                        f'fill="{text_color}" text-anchor="middle">{tile_value}</text>',
                    )

        svg_elements.append("</svg>")

        Path(BOARD_FILE_PATH).write_text("\n".join(svg_elements))
        print(f"Board view exported to {BOARD_FILE_PATH}")
