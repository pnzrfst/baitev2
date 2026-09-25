import sys
import time
from pathlib import Path

TEAL = "\033[38;5;79m"
BLACK = "\033[38;5;232m"

_ENTER_ALT_SCREEN = "\033[?1049h"
_EXIT_ALT_SCREEN = "\033[?1049l"
_HOME_AND_CLEAR = "\033[H\033[2J"

_LINES = (Path(__file__).parent / "baite_art.txt").read_text().split("\n")

_WORD = _LINES[0:9]
_CAT = _LINES[11:21]
_CAPTION = _LINES[23:24]


def _frame(eyes_open: bool, airborne: bool) -> list[str]:
    before_gap, after_gap = (2, 2) if not airborne else (1, 3)
    cat = _CAT if eyes_open else [line.replace(BLACK, TEAL) for line in _CAT]

    return _WORD + [""] * before_gap + cat + [""] * after_gap + _CAPTION


def _draw(lines: list[str]) -> None:
    sys.stdout.write(_HOME_AND_CLEAR + "\n".join(lines) + "\n")
    sys.stdout.flush()


def art() -> str:
    return "\n".join(_frame(eyes_open=True, airborne=False))


def play(beats: int = 3, interval: float = 0.5, pulse: float = 0.18) -> None:
    rest = _frame(eyes_open=True, airborne=False)
    hop = _frame(eyes_open=False, airborne=True)

    sys.stdout.write(_ENTER_ALT_SCREEN)
    sys.stdout.flush()

    try:
        _draw(rest)
        for _ in range(beats):
            time.sleep(interval - pulse)
            _draw(hop)
            time.sleep(pulse)
            _draw(rest)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write(_EXIT_ALT_SCREEN)
        sys.stdout.flush()
        print("\n".join(rest))
