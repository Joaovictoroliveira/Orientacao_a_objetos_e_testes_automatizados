import webbrowser
from tkinter import *

root = Tk( )

root.title('Abrir browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text='Abri o Google', command=google).pack(pady=20)

root.mainloop()
