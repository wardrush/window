try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

import time


def close(event): # Event is needed for GUI activation
    root.withdraw()


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        self._geom = '200x200+0+0'  # Base non-fullscreen size
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth(), master.winfo_screenheight()))


def daytime(duration):
    wait = duration * 3600 # Duration is given in hours to make days more convenient
    root['bg'] = colors[0]
    root.update()
    time.sleep(wait)


def nighttime(duration):
    wait = duration * 3600
    root['bg'] = colors[-1]
    root.update()
    time.sleep(wait)


def sunset(duration): # Duration is given in minutes
    wait = (duration * 60) / 303
    count = 0
    while count < 303:
        time.sleep(wait)
        root['bg'] = colors[count]
        root.update()
        count += 1


def sunrise(duration):
    wait = (duration * 60) / 303
    count = 1 # Start at end of color list--off by one from sunset
    while count < 303:
        time.sleep(wait)
        root['bg'] = colors[-count]
        root.update()
        count += 1


def read_color_file(path):
    colors = []
    color_file = open(path, 'r')
    for code in color_file:
        code_frmt = code[0:-2]
        colors.append(code_frmt)
    return colors



# Create linear color progression here
colors = read_color_file("/home/pi/Desktop/lin_colors.txt")

root = Tk()
root.bind('<Escape>', close)
FullScreenApp(root)


sunrise(15)
daytime(15.5)
sunset(15)
nighttime(8)


    





