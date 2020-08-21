import pyautogui
from tkinter import filedialog
from pynput import keyboard

input_file = filedialog.askopenfilename()
interval = 0.02
counter = 0
key_to_press = keyboard.Key.pause

with open(input_file, 'r') as file:
    lines = file.readlines()


def on_press(key):
    global counter

    try:
        if key == key_to_press:
            pyautogui.write(lines[counter], interval=interval)
            counter += 1
        if key == keyboard.Key.esc:
            return False
    except IndexError:
        return False


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
