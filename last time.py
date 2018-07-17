import os
import tkinter
import tkinter.colorchooser
from tkinter import ttk, filedialog, TclError
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font, families
from tkinter import Tk
from tkinter.filedialog import *
from tkinter import messagebox
from tkinter import simpledialog
import time
import os
from tkinter.colorchooser import askcolor
from tkinter import PhotoImage

class Application(tkinter.Tk):
    def __init__(self):
        """Initialize widgets, methods."""

        tkinter.Tk.__init__(self)
        self.grid()

        fontoptions = families(self)
        font = Font(family="Verdana", size=10)

        menubar = tkinter.Menu(self)
        fileMenu = tkinter.Menu(menubar, tearoff=0)
        editMenu = tkinter.Menu(menubar, tearoff=0)
        viewMenu = tkinter.Menu(menubar, tearoff=0)
        fsubmenu = tkinter.Menu(editMenu, tearoff=0)
        ssubmenu = tkinter.Menu(editMenu, tearoff=0)
        hsubmenu = tkinter.Menu(editMenu, tearoff=0)

        # adds fonts to the font submenu and associates lambda functions
        for option in fontoptions:
            fsubmenu.add_command(label=option, command = lambda: font.configure(family=option))
        # adds values to the size submenu and associates lambda functions
        for value in range(1,31):
            ssubmenu.add_command(label=str(value), command = lambda: font.configure(size=value))

        # adds commands to the menus
        menubar.add_cascade(label="File",underline=0, menu=fileMenu)
        menubar.add_cascade(label="Edit",underline=0, menu=editMenu)
        menubar.add_cascade(label="Help",underline=0, menu=viewMenu )
        fileMenu.add_command(label="New", underline=1,
                             command=self.new, accelerator="Ctrl+N")
        fileMenu.add_command(label="Open", command=self.open, accelerator="Ctrl+O")
        fileMenu.add_command(label="Save", command=self.save, accelerator="Ctrl+S")
        fileMenu.add_command(label="Exit", underline=1,
                             command=exit, accelerator="Ctrl+Q")
        editMenu.add_command(label="Copy", command=self.copy, accelerator="Ctrl+C")
        editMenu.add_command(label="Cut", command=self.cut, accelerator="Ctrl+X")
        editMenu.add_command(label="Paste", command=self.paste, accelerator="Ctrl+V")
        editMenu.add_cascade(label="Font", underline=0, menu=fsubmenu)
        editMenu.add_cascade(label="Size", underline=0, menu=ssubmenu)
        editMenu.add_command(label="Color", command=self.color)
        editMenu.add_command(label="Bold", command=self.bold, accelerator="Ctrl+B")
        editMenu.add_command(label="Italic", command=self.italic, accelerator="Ctrl+I")
        editMenu.add_command(label="Underline", command=self.underline, accelerator="Ctrl+U")
        editMenu.add_command(label="Overstrike", command=self.overstrike, accelerator="Ctrl+T")
        editMenu.add_command(label="Undo", command=self.undo, accelerator="Ctrl+Z")
        editMenu.add_command(label="Redo", command=self.redo, accelerator="Ctrl+Y")

        self.config(menu=menubar)
        self.bind_all("<Control-n>", self.new)
        self.bind_all("<Control-o>", self.open)
        self.bind_all("<Control-s>", self.save)
        self.bind_all("<Control-q>", self.exit)
        self.bind_all("<Control-b>", self.bold)
        self.bind_all("<Control-i>", self.italic)
        self.bind_all("<Control-u>", self.underline)
        self.bind_all("<Control-T>", self.overstrike)
        self.bind_all("<Control-z>", self.undo)
        self.bind_all("<Control-y>", self.redo)

        self.text = ScrolledText(self, state='normal', height=30, wrap='word', font = font, pady=2, padx=3, undo=True)
        self.text.grid(column=0, row=0, sticky='NSEW')

        # Frame configuration
        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, True)


    def new_file(self, *args):

        app = Application()
        app.title('Python Text Editor')
        app.option_add('*tearOff', False)
        app.mainloop()

    def color(self):

        try:
            (rgb, hx) = tkinter.colorchooser.askcolor()
            self.text.tag_add('color', 'sel.first', 'sel.last')
            self.text.tag_configure('color', foreground=hx)
        except TclError:
            pass

    def bold(self, *args):
        try:
            current_tags = self.text.tag_names("sel.first")
            if "bold" in current_tags:
                self.text.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.text.tag_add("bold", "sel.first", "sel.last")
                bold_font = Font(self.text, self.text.cget("font"))
                bold_font.configure(weight="bold")
                self.text.tag_configure("bold", font=bold_font)
        except TclError:
            pass

    def italic(self, *args):
        try:
            current_tags = self.text.tag_names("sel.first")
            if "italic" in current_tags:
                self.text.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.text.tag_add("italic", "sel.first", "sel.last")
                italic_font = Font(self.text, self.text.cget("font"))
                italic_font.configure(slant="italic")
                self.text.tag_configure("italic", font=italic_font)
        except TclError:
            pass

    def underline(self, *args):
        try:
            current_tags = self.text.tag_names("sel.first")
            if "underline" in current_tags:
                self.text.tag_remove("underline", "sel.first", "sel.last")
            else:
                self.text.tag_add("underline", "sel.first", "sel.last")
                underline_font = Font(self.text, self.text.cget("font"))
                underline_font.configure(underline=1)
                self.text.tag_configure("underline", font=underline_font)
        except TclError:
            pass

    def overstrike(self, *args):
        try:
            current_tags = self.text.tag_names("sel.first")
            if "overstrike" in current_tags:
                self.text.tag_remove("overstrike", "sel.first", "sel.last")
            else:
                self.text.tag_add("overstrike", "sel.first", "sel.last")
                overstrike_font = Font(self.text, self.text.cget("font"))
                overstrike_font.configure(overstrike=1)
                self.text.tag_configure("overstrike", font=overstrike_font)
        except TclError:
            pass

    def undo(self, *args):
        try:
            self.text.edit_undo()
        except TclError:
            pass

    def redo(self, *args):
        try:
            self.text.edit_redo()
        except TclError:
            pass

    def copy(self, *args):
        self.clipboard_clear()
        self.clipboard_append(self.text.selection_get())

    def cut(self, *args):
        self.copy
        self.text.delete("sel.first", "sel.last")

    def paste(self, *args):
        insertion = self.selection_get(selection = "CLIPBOARD")
        self.text.insert(0.0, insertion)

    def open(self, *args):
        filename = tkinter.filedialog.askopenfilename()

        with open(filename) as f:
            text = f.read()

        self.text.delete("1.0", "end")
        self.text.insert('insert', text)

    def save(self, *args):
        try:
            text = self.text.get("1.0", "end")
            filename = tkinter.filedialog.asksaveasfilename()

            with open(filename, 'w') as f:
                f.write(text)
        except FileNotFoundError:
            pass

    def exit(self, *args):
        self.quit()
master=Tk()
master.iconbitmap('icons/favicon.ico')
scrollbar=Scrollbar(master)
master.title("TEXT EDITOR")
icon_frame=Frame(master,bg="black")
icon_frame.pack(expand=NO,fill=X)
text=Text(master,yscrollcommand=scrollbar.set)
text.pack(expand=YES,fill=BOTH)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config(command=text.yview())

new_file_icon = PhotoImage(file='icons/new_file.gif')
save_icon = PhotoImage(file='icons/save.gif')
cut_icon = PhotoImage(file='icons/cut.gif')
copy_icon = PhotoImage(file='icons/copy.gif')
paste_icon = PhotoImage(file='icons/paste.gif')
undo_icon = PhotoImage(file='icons/undo.gif')
redo_icon = PhotoImage(file='icons/redo.gif')


#adding shortcut icons
icons=( 'new_file','save', 'cut', 'copy', 'paste','undo', 'redo')
for i, icon in enumerate(icons):
    tool_bar_icon = PhotoImage(file='icons/{}.gif'.format(icon)).zoom(2,2)
    cmd = eval(icon)
    tool_bar = Button(icon_frame, image=tool_bar_icon, height=35,width=35, command=cmd)
    tool_bar.image = tool_bar_icon
    tool_bar.pack(side=LEFT)



if __name__ == "__main__":
    app=Application()
    app.title('Python Text Editor')
    app.option_add('*tearOff', False)
    app.mainloop()


