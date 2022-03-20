import tkinter as tk
from tkinter.font import names

window =tk.Tk()
xeb=tk.StringVar()

lbl_text= tk.Label(textvariable=xeb)
lbl_text.pack()
 
text_input= tk.Entry(textvariable=xeb)
text_input.pack()

window.mainloop()
