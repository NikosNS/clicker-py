import pyautogui as pg


# pg.size()        returns size of display
# pg.position()    return s position of mouse
def position_cursor():
    while True:
        print(pg.position())
        a = input()
        if a == "q":
            break


def loop_for_letters(text):
    for i in text:
        pg.typewrite(i, interval=0.1)
        pg.press('enter')


position_cursor()

n = 4
while n > 0:
    pg.doubleClick(x=486, y=764)  # x and y is coordinates of cursor
    text = "LERA"
    text = list(text)
    #  print(len(text))
    loop_for_letters(text)

