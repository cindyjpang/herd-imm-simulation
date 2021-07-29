import numpy as np
import random
import matplotlib.pyplot as plt

# set grid size, M*N (row, col)
M: int = 5
N: int = 5

def moves(pos: tuple, dpos: tuple) -> tuple:
    return (pos[0] + dpos[0], pos[1] + dpos[1])


def check_neighbors(white_pos: tuple, black_pos: tuple) -> bool:
    stationary = white_pos
    up = (white_pos[0], white_pos[1] + 1)
    upper_right = (white_pos[0] + 1, white_pos[1] + 1)
    upper_left = (white_pos[0] - 1, white_pos[1] + 1)
    left = (white_pos[0] - 1, white_pos[1])
    right = (white_pos[0] + 1, white_pos[1])
    lower_left = (white_pos[0] - 1, white_pos[1] - 1)
    down = (white_pos[0], white_pos[1] - 1)
    lower_right = (white_pos[0] + 1, white_pos[1] - 1)

    if (black_pos == stationary) or (black_pos == up) or (black_pos == upper_right) or (black_pos == upper_left) or (black_pos == left) or (black_pos == right) or (black_pos == lower_left) or (black_pos == down) or (black_pos == lower_right):
        return True
    else:
        return False
def run_sim():
    w_x0 = random.sample([i for i in range(0,M)], 1)
    w_y0 = random.sample([j for j in range(0,N)], 1)

    b_x0 = random.sample([i for i in range(0,M)], 1)
    b_y0 = random.sample([j for j in range(0,N)], 1)


    white = [(x,y) for x, y in zip(w_x0, w_y0)]
    black = [(x,y) for x, y in zip(b_x0, b_y0)]
    stop: bool = False
    n: int = 0
    t: int = 0
    while stop != True:
        if check_neighbors(white[n], black[n]) == True:
            stop = True
        else:
            dt_w = random.sample([i for i in range(-1,2)], 2)
            dt_bl = random.sample([i for i in range(-1,2)], 2)
            white.append(moves(white[n], dt_w))
            black.append(moves(black[n], dt_bl))
            t = t+1
            n = n+1
    return n

t_dist = [run_sim() for i in range(100)]
print(t_dist)

