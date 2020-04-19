import time

from PIL import ImageGrab
import pyautogui

# bg_color = (255, 255, 255)
# dino_color = (83, 83. 83)


def capture_screen():
    screen = ImageGrab.grab ()
    return screen


def detect_enemy(screen):
    for x in range (100, 170):
        for y in range (400, 480):
             color = screen.getpixel ((x, y))
             if color == (83, 83, 83):
                return True
    
def jump():
    pyautogui.press('up')

print('Começa em 3 segundos...')
time.sleep(3)

while True:
    screen = capture_screen ()
    if detect_enemy(screen):
        jump()