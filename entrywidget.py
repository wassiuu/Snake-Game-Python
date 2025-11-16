from tkinter import *

window = Tk()
window.title("Entry Widget")

entry = Entry()
entry.pack()

entry.config(font=("Ink Free",50))
entry.config(bg='Black')
entry.config(fg='Green')

#entry.insert(0,"Spongebob") #Default text
#entry.config(state=DISABLED) #used to make the text box ACTIVE/DISABLED

entry.config(width=10)
#entry.config(show="$")

#BUTTONS
def submit():
  username = entry.get()
  print(username)
submit=Button(window,text="submit",command=submit)
submit.pack(side=RIGHT)


def delete():
  entry.delete(0,END) #deletes the line of text (first,last)
delete=Button(window,text="delete",command=delete)
delete.pack(side=RIGHT)


def backspace():
  entry.delete(len(entry.get())-1,END) #deletes last character
backspace=Button(window,text="backspace",command=backspace)
backspace.pack(side=RIGHT)

window.mainloop()