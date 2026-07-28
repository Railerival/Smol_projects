import bext

class Terminal:
    def __init__(self, Terminal_title):
        self.Terminal_title = Terminal_title
        bext.title = Terminal_title

    @staticmethod
    def terminal_size():
        """returns the terminal size"""
        return bext.size()

    @staticmethod
    def fill_and_move():
        """fills the screen and moves the cursor to (0, 0)"""
        bext.clear()

    @staticmethod
    def clear_line():
        """clears the line at which cursor is"""
        bext.clear_line()

    @staticmethod
    def print_at_xy(msg:str, x:int, y:int, colour = "Random"):
        """clears previous line """
        bext.goto(x, y)
        print(msg)
        bext.fg(colour)

#These need direct access from bext
#bg colour use directly
#size use directly
#resize not working?
#clear_line
#hide_cursor(), show_cursor(), get_key(blocking=True)
