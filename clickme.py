from tkinter import *
def click():
  print("Hello!")

window = Tk()
window.geometry("620x620")
window.title("First Click Me Program")

button = Button(window,text='Click Me!!!') #performs callback of function
button.config(command=click)
button.config(font=('Ink Free',50,'bold'),bg='orange',fg='black')
button.config(activebackground='red')
button.config(activeforeground='black')
image=PhotoImage(file='point_image.png')
button.pack()

#button.config(bg='orange')
#button.config(fg='black')



window.mainloop()
