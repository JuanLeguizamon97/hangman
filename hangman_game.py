"""Hangman CLI game
Author: Juan Leguizamon
"""

import os
import random
import unicodedata
from reading import Reading
from graphics import Graphics

def game_start():
    
    Reading("./files/data.txt")

if __name__ == "__main__":
    game_start()