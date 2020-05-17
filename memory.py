#!/usr/bin/env python

# Python Game: Memory
# Version: 0.0.1
# Created by: Ruben Felix
# Target: Learn Python by trying 

import random
mem_a = [ 'sheep', 'chicken', 'horse', 'pig' ]
mem_b = [ 'sheep', 'chicken', 'horse', 'pig' ]

board = mem_a + mem_b
game = random.sample(board, len(board))

counter = 0 

if counter == len(board):
    print("SUPER! YOU HAVE WON!")

else:
    while counter < len(mem_a):
        print ("Score: {}".format(counter))    
        puzzle_1 = int(input("type a number between 0-7 "))
        puzzle_2 = int(input("type a number between 0-7 "))

        print(game[puzzle_1])
        print(game[puzzle_2])
    
        if game[puzzle_1] == game[puzzle_2]: 
            print("GREAT!")
            counter = counter + 1 
        else:
            print("WRONG! Try again!")

