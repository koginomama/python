import tkinter as tk
import random
from PIL import Image, ImageTk#imageのサイズ調整


def click_btn():
    label["text"]=random.choice(["大吉","中吉","小吉","凶","モコ吉"])
    label.update()

root = tk.Tk()
root.title("おみくじ！！")
root.resizable(False,False)
canvas = tk.Canvas(root,width=800,height=600)
canvas.pack()
new_size = (850,700)
image = Image.open('test/test1.png')
resized_image = image.resize(new_size)
photo = ImageTk.PhotoImage(resized_image)
canvas.create_image(-30, -30, anchor=tk.NW, image=photo)
label = tk.Label(root,text="??",font=("Times New Roman",140),bg="black",fg="white")
label.place(x=400,y=60)
button = tk.Button(root,text="おみくじを引く",font=("Times New Roman",36),command=click_btn, fg="skyblue")
button.place(x=390,y=400)
root.mainloop()