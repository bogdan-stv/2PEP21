import tkinter

main_window = tkinter.Tk()
main_window.title('menu')

class TextWindow:

    def __init__(self, root_window: tkinter.Tk):
        self.root_window = root_window
        self.text = tkinter.Text(self.root_window, height=25, width=80)
        self.text.pack()
        self.add_button = tkinter.Button(self.root_window, text='Add Text', command=self.add_text)
        self.add_button.pack()
        self.select_button = tkinter.Button(self.root_window, text='Highlight Text', command=self.set_background)
        self.select_button.pack()


    def add_text(self):
        self.text.insert(tkinter.END, '\n text to insert')

    def set_background(self):
        self.text.tag_add('selection', tkinter.SEL_FIRST, tkinter.SEL_LAST)
        self.text.config('selection', background='yellow')

    def run(self):
        self.root_window.mainloop()

text = TextWindow(main_window)
text.run()











