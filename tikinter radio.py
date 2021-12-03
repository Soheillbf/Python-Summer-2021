import tkinter as tk
import random

root = tk.Tk()
v = tk.StringVar()
v.set('Python')
tk.Label(root, 
        text="""Let's play Rock,Paper,Scissors:""",
        justify = tk.LEFT,
        padx = 20).pack()
language=('Rock','paper','Scissor')
for item in language:
    tk.Radiobutton(root, 
                   text=item,
                   padx = 20, 
                   variable=v, 
                   value=item).pack(anchor=tk.W)
for item in random.randrange(language):
    tk.Radiobutton(root, 
                   text=item,
                   padx = 50, 
                   variable=v, 
                   value=item).pack(anchor=tk.W)
##def result():
##    if 

root.mainloop()

