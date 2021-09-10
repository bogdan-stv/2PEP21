import tkinter

def user_pass():
    usern = 'Username'
    passw = 'Password'
    if state.get() == 1:
        if username.get() != usern:
            print('username is wrong')
        if password.get() != passw:
            print('password is wrong')
    else:
        print('box not checked')

main_window = tkinter.Tk()
main_window.title('App 1')

label1 = tkinter.Label(main_window, text='Username: ')
label1.grid(row=0, column=0)
label2 = tkinter.Label(main_window, text='Password: ')
label2.grid(row=1, column=0)

username = tkinter.Entry(main_window)
username.grid(row=0, column=1)
password = tkinter.Entry(main_window)
password.grid(row=1, column=1)

login= tkinter.Button(main_window, text='Login', command=user_pass)
login.grid(row=2, column=0, sticky=tkinter.E)
cancel = tkinter.Button(main_window, text='Cancel', command=quit)
cancel.grid(row=2, column=1, sticky=tkinter.W)

state = tkinter.IntVar()
check_box = tkinter.Checkbutton(main_window, text= "I'm not a robot", variable=state)
check_box.grid(row=3, columnspan=2)

main_window.mainloop()