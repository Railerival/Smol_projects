import bext, random

width, height = bext.size()

try:
    while True:
        bext.fg('yellow')
        bext.bg('blue')
        print('DvD')
except KeyboardInterrupt:
    pass
