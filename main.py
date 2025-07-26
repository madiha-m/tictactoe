import numpy as np  # for craeting arrays
import random  # for generating random numbers
from time import sleep  # for adding delays


# Creating empty game board
def create_empty_board():
    board = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])
    return board


# Test: empty board created?
if __name__ == "__main__":
    print("Testing empty board creation...")
    sleep(1)  # Adding a delay for better readability
    print(create_empty_board())
