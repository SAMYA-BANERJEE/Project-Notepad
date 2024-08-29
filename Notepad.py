from tkinter import *
from tkinter import messagebox as msg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os 
from datetime import datetime
#corresponding functions of the click-commands :-
def new_window_command():
    global file
    root.title("Untitled - Notepad")
    file= None
    text_widget.delete(1.0, END)

def open_command():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents",".txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+ "- Notepad")
        text_widget.delete(1.0, END)
        f= open (file,"r")
        text_widget.insert(1.0, f.read())
        f.close()

def save_command():
    global file
    if file==None:
        file= asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents",".txt")])
        if file=="":
            file = None
        else:
            #save as a new file
            f= open(file,"w")
            f.write(text_widget.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")

    else:
          #save the new file
            f= open(file,"w")
            f.write(text_widget.get(1.0, END))
            f.close()           

def Close_window_command():
    root.destroy()

def app_exit_command():
    root.destroy()

def nothing_command():
    pass

def Cut_command():
    text_widget.event_generate("<<Cut>>")
  
def Copy_command():
    text_widget.event_generate("<<Copy>>")
    
def Paste_command():
    text_widget.event_generate("<<Paste>>")

def Delete_command():
    text_widget.delete(SEL_FIRST, SEL_LAST)

def Undo_command():
    text_widget.edit_undo()

def Redo_command():
    text_widget.edit_redo()

def Select_all_command():
    text_widget.tag_add(SEL, "1.0", END)

# def Time_and_Date_command():
#     global file
#     obj = time.gmtime(1627987508.6496193)
#     time_str = time.asctime(obj)
#     text_widget.insert(1.0, f"\nDay|Mon|Date|Time|  Year\n{time_str}\n\n")

def Time_and_Date_command():
    # Get the current date and time
    now = datetime.now()
    # Format it as 'Day|Mon|Date|Time|Year'
    formatted_date = now.strftime("%a|%b|%d|%H:%M:%S|%Y")
    text_widget.insert(1.0,f"\nDay|Mon|Date|Time|  Year\n{formatted_date}\n\n")
    
def Font_command(x):
    match x:
        case "1":
            text_widget.configure(font=("Arial", 12))
        case "2":
            text_widget.configure(font=("Courier New", 12))
        case "3":
            text_widget.configure(font=("Times New Roman", 12))
        case "4":
            text_widget.configure(font=("Verdana", 12))
        case "5":
            text_widget.configure(font=("Comic Sans MS", 12))
        case "6":
            text_widget.configure(font=("Georgia", 12))
        case "7":
            text_widget.configure(font=("Tahoma", 12))
        
    

def about_info():
    msg.showinfo("About Notepad","Hii.. i am Samya Banerjee and this is my notepad-App.")

def rate_us():
    rate_value=msg.askquestion("Thanks for ratting us..","You used this gui.. was your exprience good?")
    if rate_value=="yes":
        msg.showinfo("Thanks for your ratting..","Please add a comment on My github repository.")
    else:
        msg.showinfo("Thanks for your ratting..","this is My first try of making application.. so please co-oprate..") 

def help():
    msg.showinfo("Help Center","Please wait a few moments we will reach u soon...")  


if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.geometry("1140x536")
    root.title("Samya's GUI")
    # Set the GUI window's icon using the correct path
    icon_path = os.path.join(os.path.dirname(__file__), 'notepad_2.ico')
    root.wm_iconbitmap(icon_path)
    main_menu = Menu(root)

    # File menu:
    m1 = Menu(main_menu, tearoff=False)
    m1.add_command(label="New", command=new_window_command)
    m1.add_separator()
    m1.add_command(label="Open", command=open_command)
    m1.add_command(label="Save", command=save_command)
    m1.add_command(label="Save As", command=save_command)
    m1.add_separator()
    m1.add_command(label="Close window", command=Close_window_command)
    m1.add_command(label="Exit", command=app_exit_command)
    main_menu.add_cascade(label="Files", menu=m1)

    # Edit menu:
    m2 = Menu(main_menu, tearoff=False)
    m2.add_command(label="Cut", command=Cut_command)
    m2.add_command(label="Copy", command=Copy_command)
    m2.add_command(label="Paste", command=Paste_command)
    m2.add_separator()
    m2.add_command(label="Delete", command=Delete_command)
    m2.add_command(label="Undo", command=Undo_command)
    m2.add_command(label="Redo", command=Redo_command)
    m2.add_separator()
    m2.add_command(label="Select all", command=Select_all_command)
    m2.add_command(label="Time/Date", command=Time_and_Date_command)
    font_menu = Menu(m2, tearoff=False)
    font_menu.add_command(label="Arial", command=lambda: Font_command("1"))
    font_menu.add_command(label="Courier New", command=lambda: Font_command("2"))
    font_menu.add_command(label="Times New Roman", command=lambda: Font_command("3"))
    font_menu.add_command(label="Verdana", command=lambda: Font_command("4"))
    font_menu.add_command(label="Comic Sans MS", command=lambda: Font_command("5"))
    font_menu.add_command(label="Georgia", command=lambda: Font_command("6"))
    font_menu.add_command(label="Tahoma", command=lambda: Font_command("7"))
    m2.add_cascade(label="Font", menu=font_menu)

    main_menu.add_cascade(label="Edit", menu=m2)


    # About info :
    m4 = Menu(main_menu, tearoff=False)
    m4.add_command(label="About info.",command=about_info)
    m4.add_separator()
    m4.add_command(label="Rate us.", command=rate_us)
    m4.add_separator()
    m4.add_command(label="Help. Center", command=help)
    main_menu.add_cascade(label="About", menu=m4)
    root.config(menu=main_menu)

    # Text widget and Scrollbar
    sc_bar = Scrollbar(root)
    sc_bar.pack(side="right", fill="y")
    text_widget = Text(root,undo=True,yscrollcommand=sc_bar.set)
    file = None
    text_widget.pack(expand=True,fill="both")
    sc_bar.config(command=text_widget.yview)

    root.mainloop()