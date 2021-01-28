import tkinter as tk
from tkinter import filedialog, Text
import os
import ScrollableFrameClass

# CREATE MAIN WINDOW
root = tk.Tk()
root.title("Tkinter Tutorial")
root.geometry("606x670")
root.resizable(False,False)


# BLOCK OF CODE TO RUN THE MAIN WINDOW AT THE CENTER OF THE SCREEN
w = 600
h = 700
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
print(w,h,ws,hs)
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('+%d+%d' % (x, y))


apps = []
savedApps = []


# LOAD SAVE FILE AT THE START OF THE PROGRAM
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        savedApps = [x for x in tempApps if x]


# FUNCTION TO ADD THE PATH OF THE SELECTED APPS INSIDE THE FRAME
def addApp():
    filename = filedialog.askopenfilename(title='Select File',
                                          filetypes=[("Application", "*.app"), ("all files", "*.*")])

    # IF A FILE IS SELECTED, FILENAME SHOULD NOT BE EMPTY
    if filename != "":
        if filename not in apps:
            apps.append(filename)
            label = tk.Label(frame, text=filename, pady=5, fg='black')
            label.bind('<Button-1>', displayXButton)
            label.pack()
            print("apps from addApp: ", apps)
        else:
            print("file already in list")
    root.focus_force()


# FUNCTION TO RUN THE APPS
def runApps():
    for app in apps:
        os.system("open \"" + app + "\"")


# FUNCTION TO LOAD SAVED APPS ONCE PROGRAM STARTS
def loadApps():
    for app in apps:
        label = tk.Label(frame, text=app, pady=5, fg='black')
        label.bind('<Button-1>', displayXButton)
        label.pack()


def displayXButton(event):
    delExistingXButtonInFrame()
    xposition = event.widget.winfo_x()
    yposition = event.widget.winfo_y()
    global selectedLabelText
    selectedLabelText = event.widget['text']
    xButton = tk.Button(frame, text="x", fg="red", padx=5, command=deleteFromList)
    xButton.place(x=xposition-25, y=yposition-25)


# I PUT event = 0 BECAUSE A BINDING FUNCTION REQUIRES ATLEAST 1 ARGUMENT
# I SET ITS VALUE TO 0 TO MAKE IT OPTIONAL SO THAT I CAN CALL IT WITHOUT PASSING A VALUE
def delExistingXButtonInFrame(event=0):
    print("canvas size is:", canvas.winfo_width(), canvas.winfo_height())
    for button in frame.winfo_children():
        if type(button) == tk.Button:
            button.destroy()


# FUNC TO REMOVE ALL CHILDREN OF FRAME TO REFRESH IT
def delAllWidgetInFrame():
    for widget in frame.winfo_children():
        widget.destroy()


# FUNC TO REMOVE THE SELECTED LABEL FROM THE LIST
def deleteFromList():
    apps.remove(selectedLabelText)
    print("Hello from remove func")
    delAllWidgetInFrame()
    loadApps()


# CREATE GREEN BACKGROUND
canvas = tk.Canvas(root, height=600, width=600, bg="#4ea65c")
canvas.pack()

# CREATE WHITE IN THE MIDDLE
frame = tk.Frame(canvas, bg="white", pady=30)
frame.bind('<Button-1>', delExistingXButtonInFrame)
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

# CREATE OPEN FILE BUTTON
openFile = tk.Button(root, text="Open File", width=20, pady=5, fg="#4ea65c", command=addApp)
openFile.pack()

# CREATE RUN APPS BUTTON
runApps = tk.Button(root, text="Run Apps", width=20, pady=5, fg="#4ea65c", command=runApps)
runApps.pack()


# IF THERE ARE SAVED APPS PASS IT ONTO "APPS" VARIABLE THEN PERFORM "loadApps" FUNC
if savedApps:
    apps = savedApps
    loadApps()
    print("Has saved apps")
    print(savedApps)
# IF THERE IS NO SAVED APP, PRINT NO SAVED APPS
else:
    print("no saved apps")


root.mainloop()


# SAVE THE VALUE OF APPS IN THE SAVE TEXT FILE
print("Apps from exit area: ", apps)
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ",")
