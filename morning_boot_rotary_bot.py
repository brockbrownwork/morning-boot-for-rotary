from bot import *
import time
import pyautogui

start = time.time()

# grab the files in the working directory that have numbers for names
files = [file for file in listdir() if file.split('.')[0].isnumeric()]

print(files)

# for each of the templates
for file in files:
    # pop open the template
    show_desktop()
    search_and_click('gravotech.png', double = True)
    find('ring_and_check.png')
    pyautogui.press('esc')
    time.sleep(0.1)
    search_and_click('folder.png')
    search_and_click(file, double = True)
    search_and_click('no.png')
    search_and_click('lock.png')


end = time.time()
pyautogui.alert("Time taken: {0} seconds".format(end - start))


# move the mouse every once in a while to stay awake
start = time.time()
while True:
    time.sleep(60 * 10)
    pyautogui.hotkey("F15")
    print("pressed F15 to stay awake")
