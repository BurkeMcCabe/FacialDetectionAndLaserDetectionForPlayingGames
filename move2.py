import pytesseract as tess
import keyboard
import pyautogui
tess.pytesseract.tesseract_cmd = r'C:\Users\burke\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image
x = 0
y = 0

while 1:
    img2 = pyautogui.screenshot(r'D:\Projects\usecomputerwithouttouchingit-inator\a.png', (10, 80, 30, 20))
    img3 = pyautogui.screenshot(r'D:\Projects\usecomputerwithouttouchingit-inator\b.png', (35, 80, 30, 20))
    text = tess.image_to_string(img2)
    text2 = tess.image_to_string(img3)
    print(x, y)
    
    try:
        x = int(text)
        if (x <= 50):
            keyboard.press("p")
            print("A")
        else:
            keyboard.release("p")
    except:
        pass


    try:
        y = int(text2)
        if (y <= 50):
            keyboard.press("o")
            print("B")
        else:
            keyboard.release("o")
    except:
        pass
