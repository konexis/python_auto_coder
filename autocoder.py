import pyautogui
from tkinter import filedialog

input_file = filedialog.askopenfilename()

with open(input_file, 'r') as file:
    lines = file.readlines()


from pynput import keyboard


counter = 0

def on_press(key):
    global counter
    try:
        if key == keyboard.Key.pause:
            pyautogui.write(lines[counter], interval=0.04)
            counter +=1
        if key == keyboard.Key.esc:
            return False
    except IndexError:
        return False

with keyboard.Listener(
    on_press= on_press) as listener:
    listener.join()


