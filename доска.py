
import tkinter as tk
 
rows = int(input('Количество строк >> '))
columns = int(input('Количество колонок >> '))
 
root = tk.Tk()
mainframe = tk.Frame(root)
mainframe.pack(fill=tk.BOTH)
 
for row in range(rows):
    for column in range(columns):
        cell = tk.Frame(mainframe, width=30, height=30, bg=('red' if (row+column)%2 == 0 else 'yellow'))
        cell.grid(row=row, column=column)
        cell.configure(highlightthickness=3)
 
root.mainloop()