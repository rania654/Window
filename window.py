from tkinter import *
root = Tk()

root.geometry("500x500")
root.title("my first tkinter app")

label=Label(root,text = "This is a window")
label.pack()

btn = Button(root, text = "Click me",background = "purple",command = root.destroy, bd = 5)
btn.pack(side = "top")

entry = Entry(root, width=40,)
entry.pack(side = "right")

label2 =Label(root, text = "Hello Everbody", bd = 10, background = "pink")
label2.pack(side = "left")

button = Button(root, text = "Press me",command = root.destroy,background = "red")
button.pack()

entry2 = Entry(root, width = 50)
entry2.pack(side = "right")


root.mainloop()