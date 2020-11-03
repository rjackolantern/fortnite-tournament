from tkinter import Tk, ttk, Frame, PhotoImage, Label, LabelFrame, Text, Button, Toplevel, Scrollbar, messagebox, filedialog
import os
from Player import Player

# Initialize the list intended for storing Player objects
players = []

def close_topview():
    root.update()
    root.deiconify()
    
    top_level.withdraw()
    
def view_players():
    root.withdraw()
    
    top_level.update()
    top_level.deiconify()

# Handle exiting the program
def exit_program():

    answer = messagebox.askyesno("Exit", "Are you sure you want to exit?")

    if answer == True:

        exit()

    else:
        # do nothing
        pass

# Function passed to btnGetPlayers
def get_players():

    global players

    # Open file dialog, ask user to open a file
    # Open file dialog in the running directory of this program
    filename = filedialog.askopenfilename(initialdir=os.getcwd())

    # Begin reading the text file
    for line in filename:

        # Split the line into a list of split strings
        splitData = line.split(",")

        # Create player object using the string above split by commas
        player = Player(splitData[0], splitData[1], splitData[2], splitData[3])

        # Append previously created player object to list
        players.append(player)

root = Tk()
root.title('Fortnite Team Tournament')
root.geometry('%dx%d+%d+%d' % (912, 740, root.winfo_screenwidth() // 2 - 912 // 2,
    root.winfo_screenheight() // 2 - 740 // 2))
root.resizable(False, False)

frame = Frame(root, padx=10, pady=10, bg='white')
frame.pack()

imgBanner = PhotoImage(file='images/fortnite_banner.png')
lblBanner = Label(frame, image=imgBanner, padx=10, pady=10, borderwidth=0)
lblBanner.grid(row=0, column=0, columnspan=5, pady=5)

lblFrames = [0] * 16
txtTeams = [0] * 16
rownum, colnum = 1, 0

for i in range(len(lblFrames)):
    lblFrames[i] = LabelFrame(frame, text='TEAM ' + str(i+1), bg='white', font=('Consolas', 11, 'bold'))
    txtTeams[i] = Text(lblFrames[i], width=25, height=6, font=('Consolas', 8), state='disabled', relief='flat', bg='white')
    txtTeams[i].pack(padx=5, pady=5)
    
    lblFrames[i].grid(row=rownum, column=colnum, padx=5, pady=5)
    if (i + 1) % 4 == 0:
        rownum += 1
        colnum = 0
    else:
        colnum += 1

buttonFrame = Frame(frame, padx=10, pady=10, bg='white')
buttonFrame.grid(row=1, column=4, rowspan=4)

btnPlayers = Button(buttonFrame, text='GET PLAYERS', width=15, height=2, command=get_players)
btnPlayers.pack(side='top', padx=5, pady=5)
btnView = Button(buttonFrame, text='VIEW PLAYERS', width=15, height=2, command=view_players)
btnView.pack(side='top', padx=5, pady=5)
btnGenerate = Button(buttonFrame, text='GENERATE', width=15, height=2, state='disabled')
btnGenerate.pack(side='top', padx=5, pady=5)
btnSave = Button(buttonFrame, text='SAVE TEAMS', width=15, height=2, state='disabled')
btnSave.pack(side='top', padx=5, pady=5)
btnClear = Button(buttonFrame, text='CLEAR', width=15, height=2)
btnClear.pack(side='top', padx=5, pady=5)

btnExit = Button(buttonFrame, text='EXIT', width=15, height=2, command=exit_program)
btnExit.pack(side='top', padx=5, pady=5)

imgLogo = PhotoImage(file='images/fortnite_logo.png')
lblLogo = Label(buttonFrame, image=imgLogo, borderwidth=0, bg='white').pack(side='top', padx=5, pady=5)

img = PhotoImage(file='images/fortnite.png')
top_level = Toplevel(padx=10, pady=10, bg='white')
top_level.title('Player List')
top_level.resizable(False, False)
top_level.protocol('WM_DELETE_WINDOW', close_topview)
top_level.geometry('%dx%d+%d+%d' % (490, 635, root.winfo_screenwidth() // 2 - 490 // 2, root.winfo_screenheight() // 2 - 635 // 2))
top_level.withdraw()
 
lblImg = Label(top_level, image=img, bg='white')
lblImg.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

style = ttk.Style()
style.configure('mystyle.Treeview.Heading', font=('Consolas', 11, 'bold'))

tview = ttk.Treeview(top_level, selectmode='browse', columns=('1', '2', '3', '4'), show='headings', height=20, style='mystyle.Treeview')
tview.grid(row=1, column=0, pady=5)

headingtext = ('LAST NAME', 'FIRST NAME', 'RATING', 'TIER')
columnwidths = [150, 150, 75, 75]

for i in range(4):
    tview.column(str(i+1), width=columnwidths[i], anchor='w')
    tview.heading(str(i+1), text=headingtext[i], anchor='w')

vscroll = Scrollbar(top_level, orient='vertical', command=tview.yview)
vscroll.grid(row=1, column=1, sticky='ns')

bottomFrame = Frame(top_level, padx=5, pady=5, bg='white')
bottomFrame.grid(row=2, column=0, columnspan=2)

btnRemove = Button(bottomFrame, text='REMOVE', width=10, pady=5)
btnRemove.pack(side='left', padx=5, pady=5)
btnAdd = Button(bottomFrame, text='ADD', width=10, pady=5)
btnAdd.pack(side='left', padx=5, pady=5)
btnEdit = Button(bottomFrame, text='EDIT', width=10, pady=5)
btnEdit.pack(side='left', padx=5, pady=5)
btnSearch = Button(bottomFrame, text='SEARCH', width=10, pady=5)
btnSearch.pack(side='left', padx=5, pady=5)

root.mainloop()