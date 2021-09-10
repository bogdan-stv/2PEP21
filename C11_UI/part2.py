import tkinter

main_window = tkinter.Tk()
main_window.title('Python M2 UI')

label1 = tkinter.Label(main_window, text='Red Label', bg='red')
label1.grid(row=0, column=0)
label1.config(font=('Arial', 24))
label2 = tkinter.Label(main_window, text='Green Label', bg='green')
label2.grid(row=1, column=0)
label2.config(width=100)
label3 = tkinter.Label(main_window, text='Blue Label', bg='blue')
label3.grid(row=0, column=1)
label4 = tkinter.Label(main_window, text='Yellow Label', bg='yellow')
label4.grid(row=1, column=1)
label5 = tkinter.Label(main_window, text='Pink Label', bg='pink')
label5.grid(row=2, column =0, columnspan=2, sticky=tkinter.E)

main_window.mainloop()
print('All done')