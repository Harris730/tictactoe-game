import pygame
import MinMax_algorithm
import GUI

if __name__ == "__main__":
    Board = [['-', '-', '-'] for _ in range(3)]
    G = GUI.GameDesign()
    while True:
        G.GUIF(Board)                        # player plays 'o'
        M = MinMax_algorithm.MinMax(Board)
        score, r, c = M.max()
        G.MakeMove(c, r, 'x')               # AI plays 'x'
        G.Result()
