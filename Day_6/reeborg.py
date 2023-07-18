def jump2():
    if right_is_clear():
        turn_right()
        move()
    elif not front_is_clear():
        turn_left()
    else:
        move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    jump2()