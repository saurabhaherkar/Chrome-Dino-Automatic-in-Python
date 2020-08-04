import pyautogui
from PIL import Image, ImageGrab
from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(220, 240):
        for j in range(310, 395):
            if data[i, j] < 100:
                hit('down')
                return

    # Draw the rectangle for Cactus
    for i in range(260, 300):
        for j in range(430, 460):
            if data[i, j] < 100:
                hit('up')
                return
    return

if __name__ == '__main__':
    print('Hey... Dino game is about to start in 3 sec..')
    time.sleep(2)
    # hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # Draw the rectangle for cactus
        # for i in range(260, 300):
        #     for j in range(430, 460):
        #         data[i, j] = 0

        # Draw the rectangle for birds
        # for i in range(220, 240):
        #     for j in range(310, 395):
        #         data[i, j] = 150

        # image.show()
        # break