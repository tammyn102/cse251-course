"""
Course: CSE 251 
Lesson Week: 09
File: assignment09-p1.py 
Author: <Add name here>

Purpose: Part 1 of assignment 09, finding a path to the end position in a maze

Instructions:
- Do not create classes for this assignment, just functions
- Do not use any other Python modules other than the ones included

"""
import math
import os,sys
from numpy import absolute, append
from screen import Screen
from maze import Maze
import cv2

# Include cse 251 common Python files - Dont change
from cse251 import *
# set_working_directory(__file__)

SCREEN_SIZE = 800
COLOR = (0, 0, 255)


# TODO add any functions
def rec_restore(maze,path,last_inter,pos):
    row = pos[0]
    col = pos[1]
    if not last_inter:
        return 

    if (path and last_inter[-1]) != pos:
        maze.restore(row,col)
        rec_restore(maze,path,last_inter,path.pop())

    else:
        last_inter.pop()
        if last_inter.count(pos) == 0:
            path.append(pos)
            return 
        else:
            rec_restore(maze,path,last_inter,pos)
            

def rec_path(maze,path,last_inter,pos):
    path.append(pos)
    row = pos[0]
    col = pos[1]

    maze.move( row, col, COLOR)
    
    if maze.at_end(row, col):
        return 0

    else:
        possible_moves = maze.get_possible_moves(row, col)
        if len(possible_moves) == 0:
            for inter in last_inter:
                rdiff = abs(row - inter[0])
                cdiff = abs(col - inter[1])
                if rdiff <= 1 and cdiff <= 1 and (rdiff + cdiff < 2):
                    last_inter.remove(inter)
            rec_restore(maze,path,last_inter,path.pop())
        else:
            if len(possible_moves) >= 2:
                for _ in range(len(possible_moves)-1):
                    last_inter.append(pos)
            for pos in possible_moves:
                if maze.can_move_here(pos[0], pos[1]):
                    if rec_path(maze,path,last_inter,pos) == 0:
                        return 0
            


def solve_path(maze):
    """ Solve the maze and return the path found between the start and end positions.  
        The path is a list of positions, (x, y) """
        
    # TODO start add code here
    path = []
    last_inter = []
    pos = maze.get_start_pos()

    rec_path(maze,path,last_inter,pos)

    return path

def get_path(log, filename):
    """ Do not change this function """

    # create a Screen Object that will contain all of the drawing commands
    screen = Screen(SCREEN_SIZE, SCREEN_SIZE)
    screen.background((255, 255, 0))

    maze = Maze(screen, SCREEN_SIZE, SCREEN_SIZE, filename)

    path = solve_path(maze)

    log.write(f'Number of drawing commands for = {screen.get_command_count()}')

    done = False
    speed = 1
    while not done:
        if screen.play_commands(speed): 
            key = cv2.waitKey(0)
            if key == ord('+'):
                speed = max(0, speed - 1)
            elif key == ord('-'):
                speed += 1
            elif key != ord('p'):
                done = True
        else:
            done = True

    return path


def find_paths(log):
    """ Do not change this function """

    files = ('verysmall.bmp', 'verysmall-loops.bmp', 
            'small.bmp', 'small-loops.bmp', 
            'small-odd.bmp', 'small-open.bmp', 'large.bmp', 'large-loops.bmp')

    log.write('*' * 40)
    log.write('Part 1')
    for filename in files:
        log.write()
        log.write(f'File: {filename}')
        path = get_path(log, filename)
        log.write(f'Found path has length          = {len(path)}')
    log.write('*' * 40)


def main():
    """ Do not change this function """
    sys.setrecursionlimit(5000)
    log = Log(show_terminal=True)
    find_paths(log)


if __name__ == "__main__":
    main()