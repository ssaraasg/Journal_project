import tkinter
from tkinter import ttk
from tkinter import messagebox
import csv

class journal:
    def __init__(self):
        self.color='red'
    def open_journal(self):
        j_window = tkinter.Tk()
        j_window.title('New Journal')
        j_window.mainloop()

