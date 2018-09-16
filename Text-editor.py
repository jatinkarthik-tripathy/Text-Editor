from tkinter import *
from tkinter import filedialog, messagebox


root = Tk()
root.title('Text Editor')
root.geometry("640x480+100+100")


def newf():
    contents = text.get('1.0', END+"-1c")
    print(contents)
    if contents != "":
        if messagebox.askyesnocancel("Save Changes", "Do you want to Save your changes? ", default='yes'):
            savef()
        elif "no":
            text.delete('1.0', END)
        else:
            text.config(text=contents)


def openf():
    file = filedialog.askopenfile(defaultextension='.txt', mode='rb', title='Select your file',
                                  filetypes=[("All Files", ".*"), ("Text Documents", ".txt")])

    if file is not None:
        contents = file.read()
        text.insert('1.0', contents)
        file.close()


def savef():
    file = filedialog.asksaveasfile(defaultextension='.txt', mode='w', title="Save as",
                                    filetypes=[("All Files", ".*"), ("Text Documents", ".txt")])

    if file is not None:
        contents = text.get('1.0', END+'-1c')
        file.write(contents)
        file.close()


def font_changer():
    global font_type
    sub = Toplevel(root)
    sub.transient(root)
    sub.title("Font Changer")
    sub.geometry("320x240+150+150")

    choices_var = StringVar()
    choices = {"Verdana", "Times", "Arial", "Algerian", "Calibre"}
    choices_var.set("Calibre")

    font_popup = OptionMenu(sub, choices_var, *choices)
    Label(sub, text="Choose Font: ").grid(row=0, column=0)
    font_popup.grid(row=0, column=1)

    def changeF(*args):
        global font_type, font_size
        font_type = choices_var.get()
        text.config(font=str(font_type + ' ' + font_size))

    choices_var.trace('w', changeF)

    global font_size

    size_var = StringVar()
    sizes = {"12", "14", "16", "18", "20", "22", "24", "48", "50", "62", "72"}
    size_var.set("12")

    size_popup = OptionMenu(sub, size_var, *sizes)
    Label(sub, text="Choose Size: ").grid(row=0, column=3, padx=15)
    size_popup.grid(row=0, column=4)

    def changeS(*args):
        global font_type, font_size
        font_size = size_var.get()
        text.config(font=str(font_type + ' ' + font_size))

    size_var.trace('w', changeS)


def about():
    messagebox.showinfo("About", "This is a simple text editor!")


def end():
    if messagebox.askyesno("Quit", "Are you sure?"):
        root.destroy()


text = Text(root)
scroll = Scrollbar(root, command=text.yview)
text.configure(yscrollcommand=scroll.set)


font_type = "Calibre"
font_size = "18"

text.config(font=str(font_type + ' ' + font_size))

menu = Menu()
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=newf)
file_menu.add_command(label='Open', command=openf)
file_menu.add_command(label='Save', command=savef)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=end)


formatting = Menu(menu)
menu.add_cascade(label="Format", menu=formatting)
formatting.add_command(label="Font", command=font_changer)


help_menu = Menu(menu)
menu.add_cascade(label='Help', menu=help_menu)
# help_menu.add_command(label="Tutorial", command=tutorial)

menu.add_cascade(label='About', command=about)

scroll.pack(side='right', fill=Y)
text.pack(fill=BOTH, expand=YES)


root.protocol("WM_DELETE_WINDOW", end)
root.mainloop()
