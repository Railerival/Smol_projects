from bext_upgrade import Terminal 
import bext
import sys, time

def clear_screen() -> None:
    """Clear terminal by calling this function"""
    print("\x1b[2J\x1b[H", end="")

def iscollision() -> bool:
    collision = False
    edge = 0
    if x >= (width - step - 2):
        collision = True
        edge = 1
    elif y >= (height - step):
        collision = True
        edge = -1
    elif y <= step:
        collision = True
        edge = -1
    elif x <= step:
        collision = True
        edge = 1
    return collision, edge

def update_mode(mode, edge):
    #edge -1 hor edge 1 ver
    if mode == [+1, +1] and edge == 1:
        mode[0] = mode[0]*(-1)
    elif mode == [+1, +1] and edge == -1:
        mode[1] = mode[1]*(-1)
    elif mode == [+1, -1] and edge == 1:
        mode[0] = mode[0]*(-1)
    elif mode == [+1, -1] and edge == -1:
        mode[1] = mode[1]*(-1)
    elif mode == [-1, +1] and edge == 1:
        mode[0] = mode[0]*(-1)
    elif mode == [-1, +1] and edge == -1:
        mode[1] = mode[1]*(-1)
    elif mode == [-1, -1] and edge == 1:
        mode[0] = mode[0]*(-1)
    elif mode == [-1, -1] and edge == -1:
        mode[1] = mode[1]*(-1)
    return mode
  
step = 1
x = step + 1
y = step + 1
terminal = Terminal("DvD_animation")
terminal.fill_and_move()
width, height = terminal.terminal_size()
time.sleep(2)
mode = [1, 1]
bext.hide_cursor()

try:
    while True:
        terminal.print_at_xy("DvD", x, y)
        collision, edge = iscollision()
        if collision and edge != 0:
            mode = update_mode(mode, edge)
        if mode == [+1, +1]:
            x += step
            y += step
        elif mode == [+1, -1]:
            x += step
            y -= step
        elif mode == [-1, +1]:
            x -= step
            y += step
        elif mode == [-1, -1]:
            x -= step
            y -= step
        time.sleep(0.1)
        bext.clear()

        
except KeyboardInterrupt:
    sys.exit()