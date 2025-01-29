import random
from tkinter import *

SIZE = 400
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = {2: "eee4da", 4: "#ede0c8", 8: "f2b179", 16: "#f59563", 32: "f67c5f", 64: "f65c5f",
                         128: "#775e65"}
_COLOR_DICT = {2: "eee4da", 4: "#ede0c8", 8: "f2b179", 16: "#f59563", 32: "f67c5f", 64: "f65c5f",
                         128: "#775e65"}