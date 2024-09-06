from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic-tac-toe")
# root.iconbitmap() to set the icon on the very top left corner. Do not neeed

#frm = ttk.Frame(root, padding=10)
#frm.grid()
#ttk.Label(frm, text="This is the TicTacToe game").grid(column=0, row=0)

def b_click(b):
    pass

b1 = Button(root, text = " ", font = ("Garamond", 22), height = 3, width = 6, bg="SystemButtonFace", command = lambda: b_click(b1))
b2 = Button(root, text = " ", font = ("Garamond", 22), height = 3, width = 6, bg="SystemButtonFace", command = lambda: b_click(b1))
b3 = Button(root, text = " ", font = ("Garamond", 22), height = 3, width = 6, bg="SystemButtonFace", command = lambda: b_click(b1))

b4 = Button(root, text = " ", font = ("Garamond", 22), height = 3, width = 6, bg="SystemButtonFace", command = lambda: b_click(b1))
b5 = Button(root, text = " ", font = ("Garamond", 22), height = 3, width = 6, bg="SystemButtonFace", command = lambda: b_click(b1))
b6 = Button(root, text = " ", font = ("Garamond", 22), height = 3, width = 6, bg="SystemButtonFace", command = lambda: b_click(b1))

b7 = Button(root, text = " ", font = ("Garamond", 22), height = 3, width = 6, bg="SystemButtonFace", command = lambda: b_click(b1))
b8 = Button(root, text = " ", font = ("Garamond", 22), height = 3, width = 6, bg="SystemButtonFace", command = lambda: b_click(b1))
b9 = Button(root, text = " ", font = ("Garamond", 22), height = 3, width = 6, bg="SystemButtonFace", command = lambda: b_click(b1))


b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 0)
b3.grid(row = 0, column = 0)

b4.grid(row = 0, column = 0)
b5.grid(row = 0, column = 0)
b6.grid(row = 0, column = 0)

b7.grid(row = 0, column = 0)
b8.grid(row = 0, column = 0)
b9.grid(row = 0, column = 0)




root.mainloop()