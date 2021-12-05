import pyautogui as pg
import time
import hashlib


def hash_check():
    try:
        with open("screen.png", "rb") as original:
            bytes1 = original.read()
            or_hash = hashlib.sha256(bytes1).hexdigest()
            original.close()
        with open("new.png", "rb") as new:
            bytes2 = new.read()
            new_hash = hashlib.sha256(bytes2).hexdigest()
            new.close()
    except FileNotFoundError:
        print("files not created, something went wrong")
        return 1
    if or_hash == new_hash:
        print(or_hash, "\n", new_hash)
        pass
    else:
        return 1


print('Press Ctrl-C to quit.')
while True:
    pg.moveTo(x=1073, y=154)
    pg.click(clicks=2, interval=3)
    time.sleep(7)
    pg.screenshot('new.png', region=(200, 500, 300, 200))
    hash_check()
    if hash_check() == 1:
        print('screenshot problems or file not found')
        break
    pg.click(x=299, y=529)
    time.sleep(725)
