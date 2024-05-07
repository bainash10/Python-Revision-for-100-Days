#Use case

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(2)
    print("You studied!")



eat_breakfast()
drink_coffee()
study()


    