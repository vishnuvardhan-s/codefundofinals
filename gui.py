# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 07:36:15 2020

@author: Rag
"""
import database as db
import tkinter as tk

def buttonClick():
    db.voter['voterid'] = entry_1.get()
    db.voter['name'] = entry_2.get()
    db.voter['aadhar'] = entry_3.get()
    db.voter['email-id'] = entry_4.get()
    records = db.connect()
    print(db.voter)
    db.insert(db.voter)

root = tk.Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = tk.Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = tk.Label(root, text="Voter ID",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = tk.Entry(root)
entry_1.place(x=240,y=130)

label_2 = tk.Label(root, text="Name",width=20,font=("bold", 10))
label_2.place(x=80,y=180)

entry_2 = tk.Entry(root)
entry_2.place(x=240,y=180)

label_3 = tk.Label(root, text="Aadhar",width=20,font=("bold", 10))
label_3.place(x=80,y=230)

entry_3 = tk.Entry(root)
entry_3.place(x=240,y=230)

label_4 = tk.Label(root, text="Email",width=20,font=("bold", 10))
label_4.place(x=80,y=280)

entry_4 = tk.Entry(root)
entry_4.place(x=240,y=280)

tk.Button(root, text='Submit',command=buttonClick,width=20,bg='brown',fg='white').place(x=180,y=380)

root.mainloop()
