import tkinter
from tkinter import ttk
from tkinter import messagebox
import csv
from datetime import date
import Funcs as f

window=tkinter.Tk()
window.title('My Journal')
window.minsize(300,300)
frame=tkinter.Frame(window)
frame.pack()

def selection_changed(event):
    selection = moodcombo.get()
    snt=f.sentencegenerator(selection)
    sentenceLabel = tkinter.Label(moodframe)
    if sentenceLabel.cget("text")!='':
        sentenceLabel.cle
        sentenceLabel.config(text=snt)
    sentenceLabel.grid(row=1, column=0, padx=10, pady=10)


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
select=moodcombo.bind("<<ComboboxSelected>>", selection_changed)





window.mainloop()



