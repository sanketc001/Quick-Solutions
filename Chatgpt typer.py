import time

import cv2
from PIL import ImageGrab
import pytesseract
import pyautogui
from gtts import gTTS

def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

def type_text(text):
    pyautogui.moveTo(447,655)
    pyautogui.click()
    pyautogui.typewrite(text)
    pyautogui.press('enter')

def switch_window():
    # press the Alt+Tab keys to switch to the next window
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    time.sleep(1)

def capture_screen_and_extract_text():
    img = ImageGrab.grab()
    img.save('screenshot.png')
    screenshot = cv2.imread('screenshot.png')
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    cv2.imwrite('screenshot.png',gray)
    with open('output.txt', 'w') as file:
        file.write(text)

text_to_speech("Hello, world!", "hello_world.mp3")

text = input('Enter some text: ')
switch_window()
type_text(text)
time.sleep(60)
# switch_window()
capture_screen_and_extract_text()

