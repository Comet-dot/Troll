from tkinter import *

#parte principale
window = Tk()
window.title("Get trolled")
window.configure(background="purple")

#icona
photo1 = PhotoImage(file="2.png")
Label (window, image=photo1, bg="purple") .grid(row=0, column=0, sticky=E)

#loop
window.mainloop()
