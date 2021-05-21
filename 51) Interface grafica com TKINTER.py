from tkinter import *

class TKinter_Template (object):
    def __init__ (self, master):
        frame = Frame(master)
        frame.grid()
        hello = Label (master,
            text="Interface básica de Victor Pires usando TKinter",
            font=("Aril", 18)
        )
        hello.grid()


if __name__ == '__main__':
    root = Tk()
    root.title('Projeto básico em TKinter')
    root.geometry("600x200")
    TKinter_Template(root)
    root.mainloop()