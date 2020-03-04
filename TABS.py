from tkinter import *
from tkinter import ttk
root=Tk()



class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Tab Controls")
        self.minsize(640, 400)

        tabControl=ttk.Notebook(self)

        self.tab1=ttk.Frame(tabControl)
        tabControl.add(self.tab1, text='Basic Parameters')

        self.tab2=ttk.Frame(tabControl)
        tabControl.add(self.tab2, text="Num. Options")

        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab3, text="In & Out Parameters")

        self.tab4 = ttk.Frame(tabControl)
        tabControl.add(self.tab4, text="Statistics")

        self.tab5 = ttk.Frame(tabControl)
        tabControl.add(self.tab5, text="Optional Parameters")

        tabControl.pack(expan=1, fill="both")
        self.addingWidgets()

    def addingWidgets(self):
        def retrieve_input():
            inputValue = entry1.get()
            int_inputValue = int(inputValue)
            print(int_inputValue + 100)

# ...................................BASIC PARAMETERS..........................................................................................

        labelFrame1 = ttk.LabelFrame(self.tab1, text="Flow Type (0-6)")
        labelFrame1.grid(column=0, row=0)

        label=ttk.Label(labelFrame1, text="Insert Flow Type:")
        label.grid(column=0,row=0,sticky='W')
        entry1=Entry(labelFrame1)
        entry1.grid(column=1,row=0)

        label = ttk.Label(labelFrame1, text="Insert Parameter Y:")
        label.grid(column=0, row=1, sticky='W')
        entry12 = Entry(labelFrame1)
        entry12.grid(column=1, row=1)

        buttonCommit = Button(labelFrame1, text="Submit", command=lambda: retrieve_input())
        buttonCommit.grid(column=0,row=2)

        labelFrame2 = ttk.LabelFrame(self.tab1, text="Boundary Cond")
        labelFrame2.grid(column=0)

        label = ttk.Label(labelFrame2, text="Insert Flow Type:")
        label.grid(column=0, row=0, sticky='W')
        entry1 = Entry(labelFrame2)
        entry1.grid(column=1, row=0)

        label = ttk.Label(labelFrame2, text="Insert Parameter Y:")
        label.grid(column=0, row=1, sticky='W')
        entry12 = Entry(labelFrame2)
        entry12.grid(column=1, row=1)

        buttonCommit = Button(labelFrame2, text="Submit", command=lambda: retrieve_input())
        buttonCommit.grid(column=0, row=2)

        #.............................................................................................................................

        labelFrame2 = ttk.LabelFrame(self.tab2, text="Tab2_TEST")
        labelFrame2.grid(column=0, row=0)

        label = ttk.Label(labelFrame2, text="Insert Parameter X:")
        label.grid(column=0, row=0, sticky='W')
        entry = Entry(labelFrame2)
        entry.grid(column=1, row=0)

        label = ttk.Label(labelFrame2, text="Insert Parameter Y:")
        label.grid(column=0, row=1, sticky='W')
        entry = Entry(labelFrame2)
        entry.grid(column=1, row=1)

        buttonCommit = Button(labelFrame2, text="Submit", command=lambda: retrieve_input())
        buttonCommit.grid(column=0, row=2)


if __name__ == '__main__':
    root = Root()
    root.mainloop()