from tkinter import*
from tkinter import messagebox
win=Tk()
win.geometry('300x300')
win.configure(bg='lightblue')

def insert():
    name=ent_name.get()
    score=ent_score.get()
    if name=="":
        messagebox.showwarning('error,name is obligatory!!')
        return
    try:
        score=float(score)
    except:
        messagebox.showwarning('error','score most number!!')
        return
    if score < 0 or score > 20 :
        messagebox.showwarning('error','score most bitwin 0or20!!')
        return
    lst_box.insert("end",name+" "+str(score))
        



lst_box=Listbox(win,width=32,height=5)
lst_box.place(x=55,y=110)

lbl_name=Label(win,text='name:',font='nazanin 18',fg='pink',bg='lightblue')
lbl_name.place(x=20,y=30)

ent_name=Entry(win,width=20)
ent_name.place(x=100,y=40)

star=Label(win,text='*',fg='red',font='nazanin 18',bg='lightblue')
star.place(x=10,y=34)

lbl_score=Label(win,text='score:',font='nazanin 18',fg='pink',bg='lightblue')
lbl_score.place(x=20,y=60)

ent_score=Entry(win,width=20)
ent_score.place(x=100,y=70)

btn_insert=Button(win,text='insert',command=insert,fg='red',font='nazanin 18',bg='lightblue')
btn_insert.place(x=110,y=220)



win.mainloop()