import random

def flip():
    l = random.randint(1,2)
    if l == 1:
        res = "yazı"
    if l == 2:
        res = "tura"
    return res