from tkinter import *

count = 0
def click():
    global count
    count += 1
    print(count)


a = Tk()
photo = PhotoImage(file="C:/Users/HP/OneDrive/Web Development/Python-Projects/one-card.png")
button = Button(a,text='click',
                command=click(),
                font=('Comic Sans',30),
                fg='red',
                bg='blue',
                activeforeground='red',
                activebackground='black',
                state=ACTIVE,
                image=photo,
                compound='top')
button.pack()






a.mainloop()