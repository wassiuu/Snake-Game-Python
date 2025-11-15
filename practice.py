from tkinter import*
window = Tk()# instantiate an instance of a window

window.geometry("620x620") #dimensions of the window
window.title("First GUI Program")

icon = PhotoImage(file='images.png')
photo = PhotoImage(file='c:\\Users\\wasia\\Downloads\\images.png')
window.iconphoto(True,icon)

window.config(background="black") #background colour changer

#LABELS
label = Label(window,
              text="Hello World",
              font=('Ariel',40,'bold'),
              fg='green',
              bg='black',
              relief = RAISED,
              bd = 10,
              padx = 20,
              pady = 20,
              image=photo,
              compound='bottom')

label.pack() #needed for the text to appear in the window in the CENTER
#label.place(x=0,y=0) #used for changing the position of the text


window.mainloop() #place window on a computer screen listen for events

