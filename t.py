from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('My Profile Card')
window.geometry('400x400')

def show_profile():
    name = name_entry.get()
    hobby = hobby_entry.get()
    about = about_text.get("1.0", END).strip()
    
    if not name:
        messagebox.showwarning("Missing Data", "Please enter your name!")
        return
        
    profile_info = f"Name: {name}\nHobby: {hobby}\n\nAbout Me:\n{about}"
    messagebox.showinfo("Your Profile Card", profile_info)

title = Label(window, text='My Profile Card', fg='white', bg='purple', width=40)
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

name_label = Label(window, text='Name:')
name_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
name_entry = Entry(window, fg='blue', bg='lightyellow', width=25)
name_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

hobby_label = Label(window, text='Hobby:')
hobby_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
hobby_entry = Entry(window, fg='blue', bg='lightyellow', width=25)
hobby_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')

about_frame = Frame(window, relief=RAISED, borderwidth=3)
about_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

about_label = Label(about_frame, text='About Me')
about_label.pack(padx=5, pady=2)

about_text = Text(about_frame, fg='green', bg='lightyellow', width=40, height=4)
about_text.pack(padx=5, pady=5)

submit = Button(window, text='Show My Card', bg='purple', fg='white', width=20, command=show_profile)
submit.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()