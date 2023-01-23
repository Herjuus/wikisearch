import wikipedia
import tkinter as tk

window = tk.Tk()
window.title("Wikisearch") #Denne seksjonen setter jeg opp tkinter.
window.geometry("1500x950")

text = "Please search for wikipedia page"

sv = tk.StringVar()

def search(): # I denne funksjonen finner jeg ut hva man har skrevet i entry og oppdaterer teksten i appen til den riktige pagen
    sv = E.get()
    entryDirect = sv
    search = wikipedia.search(entryDirect)
    #page = wikipedia.page(search[0])
    summary = wikipedia.summary(search[0], auto_suggest=False, redirect=True)[:3600]
    textLabel.config(text=summary)

def setLang(lang):
    wikipedia.set_lang(lang)
    search()

header = tk.Label(text="Wikisearch", font=("Arial", 39)) # Her har vi alle tkinter greiene
E = tk.Entry(textvariable=sv, bg='#262626')
searchButton = tk.Button(text="Search", command=search, fg='#262626')
textLabel = tk.Message(text=text, width=1300, font=("Arial", 20))

en = tk.Button(text="English", command= lambda: setLang("en"), fg='#262626')
no = tk.Button(text="Norsk", command= lambda: setLang("no"), fg='#262626')

en.pack(side="top", anchor="ne", padx="10", pady="0")
no.pack(side="top", anchor="ne", padx="10", pady="0")

header.pack() # Her packer vi alt

E.pack()
searchButton.pack()
textLabel.pack()

copyright = tk.Label(text="©Herjus")
copyright.pack(side="bottom", anchor="sw")


window.mainloop() # Main loop
