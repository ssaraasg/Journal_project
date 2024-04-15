import tkinter
from tkinter import ttk
from tkinter import messagebox
import csv
from datetime import date
import Funcs as f
from JournalClass import journal

window=tkinter.Tk()
window.title('My Journal')
window.minsize(300,300)
frame=tkinter.Frame(window)
frame.pack()

new_journal=journal()


#Action_handler
def selection_changed(event):
    selection = moodcombo.get()
    snt=f.sentencegenerator(selection)
    sentenceLabel.config(text=snt)

#DateFrame
today= date.today()
dateframe=tkinter.LabelFrame(frame,text='Date' )
dateframe.grid(row=0,column=0)
datelable=tkinter.Label(dateframe,text='Today is : ')
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
yesbutton=tkinter.Button(Journalframe,text='Yes ✓',command=new_journal.open_journal)
yesbutton.grid(row=1,column=0)
yesbutton.config(fg="green")
Nobutton=tkinter.Button(Journalframe,text="No \u2716")
Nobutton.grid(row=2,column=0,pady=10,padx=10)
Nobutton.config(fg='red')



window.mainloop()



