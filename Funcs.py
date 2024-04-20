import csv
from tkinter import messagebox
def sentencegenerator(md):
    if md=='Sad':
        snt="Oh! So sorry to hear that!"
    if(md=='Happy'):
        snt="Oh! I would like to hear more!"
    if(md=='Mad'):
        snt='Oh! Do you want to talk about it ?'
    if md=='Confusing':
        snt='Oh dear!what makes you feel that way?'
    return snt
def color_selector(md):
    if md=='Sad':
        color="lightblue"
    if(md=='Happy'):
        color="Pink"
    if(md=='Mad'):
        color="brown"
    if md=='Confusing':
        color="gray"
    return color
def show_journal(date):
    list=[]
    try:
        with open ('MyJournal.csv','r') as filereader:
            reader=csv.DictReader(filereader)
            for item in reader:
                if item['Date']==date:
                    list.append(item['Journal'])
                    list.append(item['Mood'])
                    list.append(item['Date'])
                    return list
    except FileNotFoundError:
        messagebox.showinfo("No File Found","You Haven't start journaling yet")





