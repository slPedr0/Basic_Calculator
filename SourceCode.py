from tkinter import *

# Functions

def key_press(event):
    events = ("+", "-", "(", ")", "*", "/")
    if event.char.isdigit():
        button_press(event.char)
    for i in events:
        if event.char == i:
            button_press(event.char)
            break

def button_press(num):
    
    global equation_txt

    equation_txt += str(num)
    equation_label.set(equation_txt)

def equals(event=None):

    global equation_txt
    
    try:
        result = str(round(eval(equation_txt),4))

        equation_label.set(result)

        equation_txt=result
    except SyntaxError:
        equation_label.set("Invalid Syntax!")
        equation_txt=""
    except ZeroDivisionError:
        equation_label.set("Invalid Expression!")
        equation_txt=""

def Clear():
    global equation_txt
    equation_txt=""
    equation_label.set(equation_txt)

def Backspace(event=None):
    global equation_txt
    equation_txt = equation_txt[0:-1]
    equation_label.set(equation_txt)

# Window 

window = Tk()

window.title("Basic Calculator")
window.config(bg="#262423")

# Variables

equation_txt = ""
equation_label = StringVar()

# Calculator Design and Button commands

label = Label(window, textvariable=equation_label, font=("Roboto", 20), bg="#262423", fg="white", width=15, height= 2)
label.pack()

frame = Frame(bg="#2a2726")
frame.pack()

Buttons = list()

num = 1
for i in range(3):
    for j in range(3):
        Buttons.append(Button(frame, text=num, font=("Roboto, 20"),width=2, height=2, bg="#433e3d", fg="white",command= lambda number=num: button_press(number)))
        Buttons[num-1].grid(row=i,column=j)
        num+=1

Button(frame, text=0, font=("Roboto, 20"),width=2, height=2, bg="#433e3d", fg="white", command= lambda: button_press(0)).grid(row=3,column=0)
Button(frame, text='.', font=("Roboto, 20"),width=2, height=2, bg="#433e3d", fg="white", command= lambda: button_press('.')).grid(row=3,column=1)
Button(frame, text='=', font=("Roboto, 20"),width=2, height=2, bg="#433e3d", fg="white", command= equals).grid(row=3,column=2)
Button(frame, text='+', font=("Roboto, 20"),width=2, height=2, bg="#433e3d", fg="white", command= lambda: button_press('+')).grid(row=0,column=3)
Button(frame, text='-', font=("Roboto, 20"),width=2, height=2, bg="#433e3d", fg="white", command= lambda: button_press('-')).grid(row=1,column=3)
Button(frame, text='*', font=("Roboto, 20"),width=2, height=2, bg="#433e3d", fg="white", command= lambda: button_press('*')).grid(row=2,column=3)
Button(frame, text='/', font=("Roboto, 20"),width=2, height=2, bg="#433e3d", fg="white", command= lambda: button_press('/')).grid(row=3,column=3)

frame_2 = Frame()
frame_2.pack()

Button(frame_2, text="Backspace", bg="#433e3d", fg="white", command=Backspace).grid(row=0,column=0)
Button(frame_2, text="Clear", bg="#433e3d", fg="white", command=Clear).grid(row=0,column=1)

# Key Bindings

window.bind('<Return>', equals)
window.bind('<q>', Backspace)
window.bind('<BackSpace>', Backspace)
window.bind('<Key>', key_press)

window.mainloop()