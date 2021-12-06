import pyautogui as pg
import time
import hashlib


def hash_check(old, new):
    try:
        with open(old, "rb") as original:
            bytes1 = original.read()
            or_hash = hashlib.sha256(bytes1).hexdigest()
            original.close()
        with open(new, "rb") as new:
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


def clicker():
    pg.moveTo(x=1073, y=154)
    pg.click(clicks=2, interval=4)
    time.sleep(7)
    pg.screenshot('new.png', region=(200, 500, 300, 200))
    if hash_check("screen.png", "new.png") == 1:
        print('screenshot problems or file not found')
        return 1
    pg.click(x=299, y=529)
    time.sleep(2)
    pg.screenshot('check_cpu.png', region=(1550, 910, 350, 1200))


print('Press Ctrl-C to quit.')
while True:
    if clicker() == 1:
        pg.screenshot('new_main_screen.png', region=(350, 500, 150, 200))
        if hash_check("main_screen.png", "new_main_screen.png") == 1:
            break
        else:
            print("bugs in webapp")
            time.sleep(525)
            print("200 sec left")
            time.sleep(180)
            print("20 sec left")
            time.sleep(20)
    else:
        if hash_check("if_norm_cpu.png", "check_cpu.png") == 1:
            print('out of cpu')
            time.sleep(10)
        else:
            time.sleep(525)
            print("200 sec left")
            time.sleep(180)
            print("20 sec left")
            time.sleep(20)

