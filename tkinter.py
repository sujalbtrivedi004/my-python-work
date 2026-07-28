import tkinter as tk
root = tk.Tk()

choice = tk.StringVar(value="select")
tk.OptionMenu(root,choice,"Python","java","php","android",".net").pack()
tk.Label(root, textvariable=choice).pack()
root.mainloop()