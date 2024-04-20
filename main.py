import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import Funcs as f
from JournalClass import journal
from tkcalendar import Calendar
from tkinter import font

new_journal=journal()

def open_calender():

    def get_selected_date():
        try:
            selected_date = cal.selection_get()
            data=f.show_journal(str(selected_date))
            new_journal.color=f.color_selector(data[1])
            new_journal.edit_journal(data[2],data[0])
        except TypeError:
            response=messagebox.askyesno("No Journal Found","Do you want to add this date?")
            if(response==True):
                todaylabel.config(text=cal.selection_get())
                new_journal.date=cal.selection_get()
    root = tk.Toplevel(window)
    root.minsize(250,250)
    root.maxsize(250,250)
    root.geometry("300x300+600+180")
    root.title("Date Selection")
    cal = Calendar(root,selectmode="day", date_pattern="y-mm-dd")
    cal.grid(row=0,column=0)
    cal.pack()
    selectbutton=tkinter.Button(root,text='Select',command=get_selected_date)
    selectbutton.place(x=100,y=200)

window=tkinter.Tk()
window.title('My Journal')
window.minsize(400,400)
window.maxsize(400,400)
window.geometry("300x400+550+180")
frame=tkinter.Frame(window)
frame.pack()

#Action_handler
def selection_changed(event):
    selection = moodcombo.get()
    snt=f.sentencegenerator(selection)
    sentenceLabel.config(text=snt)
    new_journal.color=f.color_selector(selection)
    new_journal.mood=selection

#DateFrame
today= date.today()
dateframe=tkinter.LabelFrame(frame,text='Date' )
dateframe.grid(row=0,column=0)
datelable=tkinter.Label(dateframe,text='The date is : ')
datelable.grid(row=0,column=0,padx=10,pady=10)
todaylabel=tkinter.Label(dateframe,text=today)
todaylabel.grid(row=0,column=1)

#MoodFrame
moodframe=tkinter.LabelFrame(frame,text='Mood' )
moodframe.grid(row=1,column=0,padx=5,pady=5)
moodlable=tkinter.Label(moodframe,text='How Do you feel today?  ')
moodlable.grid(row=0,column=0,padx=10,pady=10)
moodcombo=ttk.Combobox(moodframe,values=['Happy','Sad','Mad','Confusing'])
moodcombo.grid(row=0,column=1,padx=10,pady=10)
sentenceLabel = tkinter.Label(moodframe, text='')
sentenceLabel.grid(row=1, column=0, padx=10, pady=10)
select=moodcombo.bind("<<ComboboxSelected>>", selection_changed)

#JournalFrame
Journalframe=tkinter.LabelFrame(frame,text='Journal' )
Journalframe.grid(row=2,column=0,padx=5,pady=5)
Journallable=tkinter.Label(Journalframe,text='Do you want to journal anything about today?  ')
Journallable.grid(row=0,column=0,padx=10,pady=10)
new_journal.date=date.today()
yesbutton=tkinter.Button(Journalframe,text='Yes ✓',command=new_journal.open_journal)
yesbutton.grid(row=1,column=0)
yesbutton.config(fg="green")
Nobutton=tkinter.Button(Journalframe,text="No \u2716")
Nobutton.grid(row=2,column=0,pady=10,padx=10)
Nobutton.config(fg='red')
viewbutton=tkinter.Button(window, text='View my Journals',command=open_calender)
viewbutton.place(x=150,y=320)


window.mainloop()



