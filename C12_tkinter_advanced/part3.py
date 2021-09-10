import tkinter
import tkinter.messagebox

main_window = tkinter.Tk()
main_window.title('messagebox')


class TextWindow:

    def __init__(self, root_window: tkinter.Tk):
        self.root_window = root_window
        answ = self.message = tkinter.messagebox.askquestion('Ttitle', 'Are you sure?')
        if answ == 'yes':
            print('Running code...')
        else:
            print('Canceling...')

    def run(self):
        self.root_window.mainloop()


text = TextWindow(main_window)
text.run()
