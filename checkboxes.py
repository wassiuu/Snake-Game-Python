from tkinter import *

window = Tk()
window.title("checkboxes")


def display():
  if x.get()==1:
    print("I like python")
  else:
    print(f"I dont like python")
x = IntVar() #stores an integer in x
checkbox=Checkbutton(window,text="PYTHON",variable=x,onvalue=1,offvalue=0,command=display)
checkbox.pack()

checkbox.config(font=("Ariel",20),
                fg = "blue",
                bg = "black")

checkbox.config(activeforeground="blue",activebackground="black")

image1=PhotoImage(file='photos/python logo.png')
image2=PhotoImage(file='photos/javalogo.png')
checkbox.config(image=image1,compound="left") #sets image to photo image






window.mainloop()