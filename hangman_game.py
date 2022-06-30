"""Hangman CLI game
Author: Juan Leguizamon
"""

import os
import random

def game_start():

    def reading():
        archive = "./files/data.txt"
        data = []

        with open(archive, "r", encoding="utf-8") as f:
            for line in f:
                data.append(line)
        
        word = data[random.randint(0,170)]
        word = word.upper()
        word_sliced =[]
        hide_list = []

        for i in word:
            if i != "\n":
                word_sliced.append(i)

        for i in range (len(word_sliced)):
            hide_list.append("_")

        print(hide_list)


    def graphics():
        
        counter = []
        maximum = 6

        hangmanpic = ['''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
    /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
    /|\  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
    /|\  |
    /    |
            |
        =========''', '''
        +---+
        |   |
        O   |
    /|\  |
    / \  |
            |
        =========''']

    reading()

if __name__ == "__main__":
    game_start()