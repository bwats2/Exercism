from typing import List # Enable List type hints

colordict = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

def value(colors: List) -> int:
    return int(str(colordict[colors[0]])+str(colordict[colors[1]]))