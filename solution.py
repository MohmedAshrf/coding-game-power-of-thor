import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
    
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    if( initial_tx > light_x and initial_ty > light_y):
        print("NW")
        initial_tx+=1
        initial_ty-=1
    if( initial_tx > light_x and initial_ty < light_y):
        print("SW")
        initial_tx+=1
        initial_ty+=1
    if( initial_tx < light_x and initial_ty < light_y):
        print("SE")
        initial_tx-=1
        initial_ty+=1
    if( initial_tx < light_x and initial_ty > light_y):
        print("NE")
        initial_tx-=1
        initial_ty-=1
    while(initial_tx != light_x and initial_ty == light_y):
        if( initial_tx < light_x):
            print("E")
            initial_tx += 1
        if( initial_tx > light_x):
            print("W")
            initial_tx -= 1
    while(initial_ty != light_y and initial_tx == light_x ):
        if( initial_ty < light_y):
            print("S")
            initial_ty -= 1
        if( initial_ty > light_y):
            print("N")
            initial_ty += 1
