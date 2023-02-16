#Hurdle 1-4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
        
    turn_right()
    move()
    turn_right() 
    
    while front_is_clear():
        move()
    turn_left()
        

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

#CODE FOR MAZE(POTD)
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        elif wall_in_front():
            turn_left()
    elif right_is_clear:
        turn_right()
        move()
