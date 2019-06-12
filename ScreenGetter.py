import mss
import numpy as np

def get_screen():
    sct = mss.mss()
    mon = sct.monitors[2]
    monitor = {
        "top": mon["top"] + 150,
        "left": mon["left"] + 960,
        "width": 1100,
        "height": 600,
        "mon": 2}
    screen = np.array(sct.grab(monitor))
    return screen