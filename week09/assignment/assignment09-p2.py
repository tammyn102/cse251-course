"""
Course: CSE 251 
Lesson Week: 09
File: assignment09-p2.py 
Author: Tammy Nolasco

Purpose: Part 2 of assignment 09, finding the end position in the maze

Instructions:
- Do not create classes for this assignment, just functions
- Do not use any other Python modules other than the ones included
- Each thread requires a different color by calling get_color()


This code is not interested in finding a path to the end position,
However, once you have completed this program, describe how you could 
change the program to display the found path to the exit position.

What would be your strategy?  

We are using stop to say if the thread didn't find a path then it will finish
the path which is going to start the path with a different color until there's
a thread that finds the exit

Why would it work?

<Answer here>

"""
from concurrent.futures import thread
import math
import os,sys
import threading

from numpy import append 
from screen import Screen
from maze import Maze

import cv2

# Include cse 251 common Python files - Dont change
from cse251 import *
# set_working_directory(__file__)

SCREEN_SIZE = 800
COLOR = (0, 0, 255)
COLORS = (
    (0,0,255),
    (0,255,0),
    (255,0,0),
    (255,255,0),
    (0,255,255),
    (255,0,255),
    (128,0,0),
    (128,128,0),
    (0,128,0),
    (128,0,128),
    (0,128,128),
    (0,0,128),
    (72,61,139),
    (143,143,188),
    (226,138,43),
    (128,114,250)
)

# Globals
current_color_index = 0
thread_count = 0
stop = False

def get_color():
    """ Returns a different color when called """
    global current_color_index
    if current_color_index >= len(COLORS):
        current_color_index = 0
    color = COLORS[current_color_index]
    current_color_index += 1
    return color

def rec_path(maze,pos,color):
    global stop
    global thread_count
    thread_list = []

    if not stop:
        if maze.at_end(pos[0], pos[1]):
            stop = True 
        
        maze.move(pos[0], pos[1], color)
        possible = maze.get_possible_moves(pos[0], pos[1])

        if len(possible) == 1:
            if maze.can_move_here(possible[0][0], possible[0][1]):
                rec_path(maze,possible[0],color)
        elif len(possible) > 1:
            # first line color
            if possible[0]:
                thread_list.append(threading.Thread(target=rec_path, args=(maze,possible[0],color)))
            # second change color for ever line after the first
            for path in possible[1:]:
                if maze.can_move_here(path[0],path[1]):
                    thread_list.append(threading.Thread(target=rec_path, args=(maze,path,get_color())))
                    
            # third start threads
            for thread in thread_list:
                thread.start()
            # fourth join threads
            for thread in thread_list:
                thread.join()

def solve_find_end(maze):
    """ finds the end position using threads.  Nothing is returned """
    # When one of the threads finds the end position, stop all of them
    global stop
    global thread_count
    pos = maze.get_start_pos()

    path = threading.Thread(target=rec_path,args=(maze,pos,get_color()))
    path.start()
    path.join()
    stop = False

            
def find_end(log, filename, delay):
    """ Do not change this function """

    global thread_count

    # create a Screen Object that will contain all of the drawing commands
    screen = Screen(SCREEN_SIZE, SCREEN_SIZE)
    screen.background((255, 255, 0))

    maze = Maze(screen, SCREEN_SIZE, SCREEN_SIZE, filename, delay=delay)

    solve_find_end(maze)

    log.write(f'Number of drawing commands = {screen.get_command_count()}')
    log.write(f'Number of threads created  = {thread_count}')

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



def find_ends(log):
    """ Do not change this function """

    files = (
        ('verysmall.bmp', True),
        ('verysmall-loops.bmp', True),
        ('small.bmp', True),
        ('small-loops.bmp', True),
        ('small-odd.bmp', True),
        ('small-open.bmp', False),
        ('large.bmp', False),
        ('large-loops.bmp', False)
    )

    log.write('*' * 40)
    log.write('Part 2')
    for filename, delay in files:
        log.write()
        log.write(f'File: {filename}')
        find_end(log, filename, delay)
    log.write('*' * 40)


def main():
    """ Do not change this function """
    sys.setrecursionlimit(5000)
    log = Log(show_terminal=True)
    find_ends(log)



if __name__ == "__main__":
    main()