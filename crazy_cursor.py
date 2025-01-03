#import directories
import pyautogui as pg
from random import randint
from time import sleep

#create class

class Programm:
    def __init__(self):
        super(Programm,self).__init__()
        #call method
        self.crazy_cursor()
    #create method
    def crazy_cursor(self):
        while True:
            x_coord = randint(1, 1920)
            y_coord = randint(1, 1080)
            #mouse random move
            pg.moveTo(x_coord,y_coord)
            sleep(0.1)
#launch
if __name__ == "__main__":
    Programm()