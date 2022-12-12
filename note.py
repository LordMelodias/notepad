#  header file import 
import re
from tkinter import *
from tkinter.ttk import *
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog,simpledialog
from tkinter.scrolledtext import ScrolledText

# widget
root = Tk()
root.geometry('750x520')
root.title('DataFlair Notepad')
root.resizable(0, 0)

#notepad window
notepad = ScrolledText(root, width = 90, height = 40)
fileName = ' '

########################## Function define start here#####################################

#file menu New option
def New():     
    global fileName
    if len(notepad.get('1.0', END+'-1c'))>0:
        if messagebox.askyesno("Notepad", "Do you want to save changes?"):
            Save()
        else:
            notepad.delete(0.0, END)
    root.title("Notepad")

#file menu Open option
def Open():     
    filedia = filedialog.askopenfile(parent = root, mode = 'r')
    t = filedia.read()     #t is the text read through filedialog
    notepad.delete(0.0, END)
    notepad.insert(0.0, t)
    
#file menu Save option
def Save():     
    filedia = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
    if filedia!= None:
        data = notepad.get('1.0', END)
    try:
        filedia.write(data)
    except:
        messagebox.showerror(title="Error", message = "Not able to save file!")

#file menu Save As option
def SaveAs():     
    filedia = filedialog.asksaveasfile(mode='w', defaultextension = '.txt')
    t = notepad.get(0.0, END)     #t stands for the text gotten from notepad
    try:
        filedia.write(t.rstrip())
    except:
        messagebox.showerror(title="Error", message = "Not able to save file!")


def Exit():     #file menu Exit option
    if messagebox.askyesno("Notepad", "Are you sure you want to exit?"):
        root.destroy()

def Cut():     #edit menu Cut option
    notepad.event_generate("<<Cut>>")

def Copy():     #edit menu Copy option
    notepad.event_generate("<<Copy>>")

def Paste():     #edit menu Paste option
    notepad.event_generate("<<Paste>>")

def Clear():     #edit menu Clear option
    notepad.event_generate("<<Clear>>")

def Find():     #edit menu Find option
    notepad.tag_remove("Found",'1.0', END)
    find = simpledialog.askstring("Find", "Find what:")
    if find:
        idx = '1.0'     #idx stands for index
    while 1:
        idx = notepad.search(find, idx, nocase = 1, stopindex = END)
        if not idx:
            break
        lastidx = '%s+%dc' %(idx, len(find))
        notepad.tag_add('Found', idx, lastidx)
        idx = lastidx
    notepad.tag_config('Found', foreground = 'white', background = 'blue')
    notepad.bind("<1>", click)

def click(event):     #handling click event
    notepad.tag_config('Found',background='white',foreground='black')

def SelectAll():     #edit menu Select All option
    notepad.event_generate("<<SelectAll>>")
    
def TimeDate():     #edit menu Time/Date option
    now = datetime.now()
    # dd/mm/YY H:M:S
    dtString = now.strftime("%d/%m/%Y %H:%M:%S")
    label = messagebox.showinfo("Time/Date", dtString)

def About():     #help menu About option
    label = messagebox.showinfo("About Notepad", "Notepad by - \nDataFlair")


##########################Function define end here#####################################


#notepad menu items
notepadMenu = Menu(root)
root.configure(menu=notepadMenu)

#file menu
fileMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='File', menu = fileMenu)

#adding options in file menu
fileMenu.add_command(label='New', command = New)
fileMenu.add_command(label='Open...', command = Open)
fileMenu.add_command(label='Save', command = Save)
fileMenu.add_command(label='Save As...', command = SaveAs)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command = Exit)

#edit menu
editMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Edit', menu = editMenu)

#adding options in edit menu
editMenu.add_command(label='Cut', command = Cut)
editMenu.add_command(label='Copy', command = Copy)
editMenu.add_command(label='Paste', command = Paste)
editMenu.add_command(label='Delete', command = Clear)
editMenu.add_separator()
editMenu.add_command(label='Find...', command = Find)
editMenu.add_separator()
editMenu.add_command(label='Select All', command = SelectAll)
editMenu.add_command(label='Time/Date', command = TimeDate)

#help menu
helpMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Help', menu = helpMenu)

#adding options in help menu
helpMenu.add_command(label='About Notepad', command = About)


notepad.pack()
root.mainloop()