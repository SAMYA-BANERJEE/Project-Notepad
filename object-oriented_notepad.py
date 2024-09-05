import tkinter as tk
from tkinter import messagebox as msg
from tkinter.filedialog import askopenfilename,asksaveasfilename
from datetime import datetime
import os

class MenuBar:
    def __init__(self, parent):
        self.main_menu = tk.Menu(parent)
        parent.config(menu=self.main_menu)

           # File menu:
        m1 = tk.Menu(self.main_menu, tearoff=False)
        m1.add_command(label="New", command=parent.new_command)
        m1.add_separator()
        m1.add_command(label="Open", command=parent.open_command)
        m1.add_command(label="Save", command=parent.save_command)
        m1.add_command(label="Save As", command=parent.save_command)
        m1.add_separator()
        m1.add_command(label="Close window", command=parent.Close_window_command)
        m1.add_command(label="Exit", command=parent.Close_window_command)
        self.main_menu.add_cascade(label="Files", menu=m1)

        # Edit menu:
        m2 = tk.Menu(self.main_menu, tearoff=False)
        m2.add_command(label="Cut", command=parent.Cut_command)
        m2.add_command(label="Copy", command=parent.Copy_command)
        m2.add_command(label="Paste", command=parent.Paste_command)
        m2.add_separator()
        m2.add_command(label="Delete", command=parent.Delete_command)
        m2.add_command(label="Undo", command=parent.Undo_command)
        m2.add_command(label="Redo", command=parent.Redo_command)
        m2.add_separator()
        m2.add_command(label="Select all", command=parent.Select_all_command)
        m2.add_command(label="Time/Date", command=parent.Time_and_Date_command)
        font_menu = tk.Menu(m2, tearoff=False)
        font_menu.add_command(label="Arial", command=lambda: parent.Font_command("1"))
        font_menu.add_command(label="Courier New", command=lambda: parent.Font_command("2"))
        font_menu.add_command(label="Times New Roman", command=lambda: parent.Font_command("3"))
        font_menu.add_command(label="Verdana", command=lambda: parent.Font_command("4"))
        font_menu.add_command(label="Comic Sans MS", command=lambda: parent.Font_command("5"))
        font_menu.add_command(label="Georgia", command=lambda: parent.Font_command("6"))
        font_menu.add_command(label="Tahoma", command=lambda:parent.Font_command("7"))
        m2.add_cascade(label="Font", menu=font_menu)

        self.main_menu.add_cascade(label="Edit", menu=m2)


        # About info :
        m4 = tk.Menu(self.main_menu, tearoff=False)
        m4.add_command(label="About info.",command=parent.about_info)
        m4.add_separator()
        m4.add_command(label="Rate us.", command=parent.rate_us)
        m4.add_separator()
        m4.add_command(label="Help. Center", command=parent.help)
        self.main_menu.add_cascade(label="About", menu=m4)

    
class Text:
    def __init__(self,parent):
        
        self.text_widget=tk.Text(parent,undo=True)
        self.text_widget.pack(expand=True,fill="both")

class APP(tk.Tk):

    def __init__(self, win_title):
        super().__init__()
        # Main setup:
        self.geometry("1140x536")
        self.title(f"{win_title}")
        #icon
        icon_path = os.path.join(os.path.dirname(__file__), 'notepad_2.ico')
        self.wm_iconbitmap(icon_path) 
         
        #window-minimum size:      
        self.minsize(1140,536)

        # Create the menu bar
        self.menu = MenuBar(self)
        # Create the text widget:
        self.text_widget = Text(self).text_widget
        # Run:
        self.mainloop() 
    
    def Close_window_command(self):
        self.destroy()
    def new_command(self):
        self.geometry()
        self.title(" Untitled - Notepad ")
        self.text_widget.delete(1.0,"end")
        self.text_widget.update()
        self.mainloop()

    def Cut_command(self):
        self.text_widget.event_generate("<<Cut>>")
        
    def Copy_command(self):
        self.text_widget.event_generate("<<Copy>>") 

    def Paste_command(self):
        self.text_widget.event_generate("<<Paste>>") 

    def about_info(self):
        msg.showinfo("About us","this is my first object-oriented tkinter project.")

    def open_command(self):

        file_path = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file_path=="":
            pass
        else:
            self.title(os.path.basename(file_path)+ "- Notepad")
            self.text_widget.delete(1.0, "end")
            f= open(file_path,"r")
            self.text_widget.insert(1.0,f.read()) 
            f.close()      

    def save_command(self):
        file_path = asksaveasfilename(defaultextension=".txt",filetypes=[("All Types","*.*"),("Text Document","*.txt")])

        if file_path=="":
            pass
        else:
            f = open(file_path,"a")
            f.write(self.text_widget.get(1.0,"end"))
            f.close()

    def help(self):
        msg.showinfo("Help Center","Please wait a few moments we will reach u soon...") 

    def rate_us(self):
        rate_value=msg.askquestion("Thanks for ratting us..","You used this gui.. was your exprience good?")

        if rate_value=="yes":
            msg.showinfo("Thanks for your ratting..","Please add a comment on My github repository.")
        else:
            msg.showinfo("Thanks for your ratting..","this is My first try of making application.. so please co-oprate..")

    def Font_command(self,x):
        match x:
            case "1":
                self.text_widget.configure(font=("Arial", 12))
            case "2":
                self.text_widget.configure(font=("Courier New", 12))
            case "3":
                self.text_widget.configure(font=("Times New Roman", 12))
            case "4":
                self.text_widget.configure(font=("Verdana", 12))
            case "5":
                self.text_widget.configure(font=("Comic Sans MS", 12))
            case "6":
                self.text_widget.configure(font=("Georgia", 12))
            case "7":
                self.text_widget.configure(font=("Tahoma", 12))  

    def Time_and_Date_command(self):
        # Get the current date and time
        now = datetime.now()
        # Format it as 'Day|Mon|Date|Time|Year'
        formatted_date = now.strftime("%a|%b|%d|%H:%M:%S|%Y")
        self.text_widget.insert(1.0,f"\nDay|Mon|Date|Time|  Year\n{formatted_date}\n\n")   

    def Delete_command(self):
        try:
            self.text_widget.delete("sel.first", "sel.last")
        except:
            pass  # This will silently handle cases where no text is selected

    def Select_all_command(self):
        self.text_widget.tag_add("sel", "1.0", "end-1c")

    def Undo_command(self):
        self.text_widget.edit_undo()

    def Redo_command(self):
        self.text_widget.edit_redo()               

window_1 = APP(" Untitled - Notepad ")