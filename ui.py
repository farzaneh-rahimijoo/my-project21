from tkinter import*
from tkinter import messagebox
from data import database
db=database(r'D:farzaneh\project_3\mydata21.db')
win=Tk()
win.geometry('400x400')
win.title('login form')
win.configure(bg="#8a58ff")

def insert():
    name=ent_name.get()
    lname=ent_lname.get()
    email=ent_email.get()
    password=ent_password.get()
    if name=="" or lname=="" or email=="" or password=="":
        messagebox.showerror("ERROR","FILL ALL THE BLANK")

    else:
        db.insert(name,lname,email,password)
        clear()

def login():
    email = ent_email.get().strip()
    password = ent_password.get().strip()
    a =  db.login(email,password)
    if len(a) == 0:
         messagebox.showerror("ERROR","PLEASE SIGN UP")
    else:
        clear()
        win2 = Toplevel(win)
        win2.geometry('400x400')
        win2.title('welcome')
        win2.configure(bg='light blue')
def clear():
    ent_name.delete(0,END)
    ent_lname.delete(0,END)
    ent_email.delete(0,END)
    ent_password.delete(0,END)
    ent_name.focus()

lbl_name=Label(win,text='name:',font='nazanin 20',bg="#8a58ff")
lbl_name.place(x=20,y=20)
ent_name=Entry(win,width=30)
ent_name.place(x=110,y=30)

lbl_lname=Label(win,text='lname:',font='nazanin 19',bg="#8a58ff")
lbl_lname.place(x=20,y=60)
ent_lname=Entry(win,width=30)
ent_lname.place(x=110,y=69)

lbl_email=Label(win,text='email:',font='nazanin 20',bg="#8a58ff")
lbl_email.place(x=20,y=95)
ent_email=Entry(win,width=30)
ent_email.place(x=110,y=105)

lbl_star=Label(win,text='*',font='nazanin 21',bg='#8a58ff',fg='red')
lbl_star.place(x=7,y=106)

lbl_password=Label(win,text='password:',font='nazanin 14',bg="#8a58ff")
lbl_password.place(x=16,y=130)
ent_password=Entry(win,width=30,show="*")
ent_password.place(x=110,y=138)

lbl_star2=Label(win,text='*',font='nazanin 19',bg='#8a58ff',fg='red')
lbl_star2.place(x=3,y=138)


btn_sign_up=Button(win,text='sign_up',font='nazanin 15',bg='#8a58ff',width=14,command=insert)
btn_sign_up.place(x=40,y=240)

btn_sign_in=Button(win,text='sign_in',font='nazanin 15',bg='#8a58ff',width=14,command=login)
btn_sign_in.place(x=200,y=240)


win.mainloop()