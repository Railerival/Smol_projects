from bext_upgrade import Terminal 
import bext
import sys, time

def clear_screen() -> None:
    """Clear terminal by calling this function"""
    print("\x1b[2J\x1b[H", end="")

def check_hit(mode):
    """checks hit and changes mode"""
    hit = False
    if x >= (width - 1):
        hit = True
        if mode == (0, 0):
            mode = (1, 0)
        elif mode == (0, 1):
            mode = (1, 1)
    if x <= 1:
        hit = True
        if mode == (1, 0):
            mode = (0, 0)
        if mode == (1, 1):
            mode = (0, 0)
    if y >= (height - 1):
        hit = True
        if mode == (0, 0):
            mode = (0, 1)
        elif mode == (1, 0):
            mode = (1, 1)
    if y <= 1:
        hit = True
        if mode == (0, 1):
            mode = (0, 0)
        if mode == (1, 1):
            mode = (1, 0)
    return mode, hit
terminal = Terminal("DvD_animation")
x = 0
y = 0

terminal.fill_and_move()
bext.resize(100,200)
width, height = terminal.terminal_size()
time.sleep(2)
try:
    mode = (0,0)
    while True:
        terminal.print_at_xy(f"DvD", x, y)
        time.sleep(0.5)
        clear_screen()
        old_x = x
        old_y = y
        if mode == (0, 0):
            x += 1
            y += 1
            new_mode, hit = check_hit(mode)
            if hit == True:
                x = old_x + 2
                y = old_y - 1
            mode = new_mode
            hit = False
        elif mode == (0, 1):
            x += 1
            y -= 1
            new_mode, hit = check_hit(mode)
            if hit == True:
                x = old_x + 2
                y = old_y - 1
            mode = new_mode
            hit = False
        elif mode == (1, 0):
            x -= 1 
            y += 1
            new_mode, hit = check_hit(mode)
            if hit == True:
                x = old_x - 1
                y = old_y + 2
            mode = new_mode
            hit = False
        elif mode == (1, 1):
            x -= 1
            y -= 1
            new_mode, hit = check_hit(mode)
            if hit == True:
                x = old_x - 1
                y = old_y + 2
            mode = new_mode
            hit = False
except KeyboardInterrupt:
    sys.exit()