#Screen Taker Using Python
import pyautogui
import tkinter as tk
from tkinter.filedialog import*
root = tk.Tk()
canvas1=tk.Canvas(root, width=300,height=300)#For Creating Window
canvas1.pack()
def takeScreenshot():
    myscreensort = pyautogui.screenshot()
    save_path=asksaveasfilename()
    myscreensort.save(save_path+"_screensort.png")

button = tk.Button(text="Take Screensort",command=takeScreenshot,font=10)
canvas1.create_window(150,150,window=button)
tk.mainloop()

