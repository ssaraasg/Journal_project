import tkinter
from tkinter import ttk
from tkinter import messagebox
import csv
from datetime import date

class journal:
    def __init__(self):
        self.color=''
        self.mood=''
        self.txt=''
        self.date=''
    def save(self):
        with open('MyJournal.csv', 'a') as filewriter:
            self.txt=self.text_box.get("1.0", "end-1c")
            data={'Journal': self.txt,'Mood': self.mood, 'Date':self.date}
            csvfilewriter = csv.DictWriter(filewriter,fieldnames=['Journal','Mood','Date'])
            csvfilewriter.writeheader()
            csvfilewriter.writerow(data)
            self.j_window.destroy()
    def clear(self):
        self.text_box.delete("1.0", "end-1c")
    def exit(self):
        self.j_window.destroy()
    def open_journal(self):
        if(self.mood==''):
            messagebox.showwarning("Mood","Please select your Mood")
        else:
            self.j_window = tkinter.Tk()
            self.textframe = tkinter.LabelFrame(self.j_window, text='Journal\t'+str(self.date), bg=self.color)
            self.text_box = tkinter.Text(self.textframe,height=15,width=35)
            self.j_window.title('New Journal')
            self.j_window.minsize(400,400)
            self.j_window.maxsize(400,400)
            self.j_window.geometry("400x400+550+180")
            self.j_window.configure(background=self.color)
            self.text_box.grid(row=0,column=0,padx=10,pady=10)
            font_specifications = ("Arial", 11)
            self.text_box.configure(font=font_specifications)
            Savebutton = tkinter.Button(self.textframe, text='Save',command=self.save)
            Savebutton.grid(row=1,column=0, pady=10, padx=10)
            clearbutton = tkinter.Button(self.textframe, text='Clear',command=self.clear)
            clearbutton.grid(row=2, column=0, pady=10, padx=10)
            self.textframe.pack()
            self.j_window.mainloop()
    def edit_journal(self,date,jtxt):
        self.j_window = tkinter.Tk()
        self.textframe = tkinter.LabelFrame(self.j_window, text='Journal\t'+str(date), bg=self.color)
        self.text_box = tkinter.Text(self.textframe,height=15,width=35)
        self.text_box.insert(tkinter.END, jtxt)
        self.j_window.title('Journal')
        self.j_window.minsize(400,400)
        self.j_window.maxsize(400,400)
        self.j_window.configure(background=self.color)
        self.text_box.grid(row=0,column=0,padx=10,pady=10)
        self.text_box.config(state=tkinter.DISABLED)
        Exitbutton = tkinter.Button(self.textframe, text='Exit',command=self.exit)
        Exitbutton.grid(row=1,column=0, pady=10, padx=10)
        self.textframe.pack()
        self.j_window.mainloop()



