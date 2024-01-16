from tkinter import *

a = Tk()
a.title('bro is back')
#photo = PhotoImage(file="one-card.png")
#photo = PhotoImage(file="one-card.png")
photo = PhotoImage(file="C:/Users/HP/OneDrive/Web Development/Python-Projects/one-card.png")

b = Label(a,text='Manoar is a bad boy',
          font=('arial',40,'bold'),
          fg='yellow',
          bg='black',
          relief=SUNKEN,
          bd=30,
          padx=20,
          pady=20,
          image=photo,
          compound='top')
#b.pack() center
#b.place(x=100,y=100)
b.pack()

a.mainloop()

c = 'manu'
print(c)