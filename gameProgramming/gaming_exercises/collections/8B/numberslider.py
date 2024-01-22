# Number Slider, by Christian Ortiz, Based on a project by Sweigart, v0.0

import sys, random, pygame
# sys module provides acces to system resources (i.e Operating System Commands)

from pygame.locals import *
# Allows us to call functions from pygame using just the function name instead of



BOARDWIDTH = 4 # COLUMNS
BOARDHEIGHT = 4 # COLUMNS
TITLESIZE = 80 # MEASURED IN PIXELS
WINDOWWIDTH = 640
WINDOWWIDTH = 480
FPS = 30 # Maximum is a maximum value!
BLANK = None

# COLOR VALUES in (R, G, B) format.
# 0 = No Value, 255 = Max Value
BLACK = (0 ,0 ,0)
WHITE = (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQOISE = (3, 54, 73)
GREEN = (0, 204, 0)

# BOARD DESIGN SETUP
BGCOLOR = DARKTURQOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20 # pixels

# BUTTON SETUP
BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE


# ESTABLISH WINDOW MARGINS
XMARGIN = int((WINDOWWIDTH) - (TITLESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2
# int((WINDOWWIDTH) - (TITLESIZE * BOARDWIDTH + (3))) / 2)
# int((WINDOWWIDTH) - (320 +(3))) / 2)
# int((WINDOWWIDTH) - (323 / 2))
# int((640 - (161.5))
# int(478.5)
# XMARGIN = 478
print(XMARGIN)
YMARGIN = 


