import string
from tkinter import *
import random
import pyperclip
def gen():
    small_alpha=string.ascii_lowercase
    cap_alpha=string.ascii_uppercase
    num=string.digits
    spec_char=string.punctuation

    all=small_alpha+cap_alpha+num+spec_char
    pass_len=int(boxlen.get())
    if choice.get()==1:
        passfield.insert(0,random.sample(small_alpha,pass_len))

    if choice.get()==2:
        passfield.insert(0,random.sample(small_alpha+cap_alpha,pass_len))

    if choice.get()==3:
        passfield.insert(0,random.sample(all,pass_len))

def copy():
    rabdom_pass=passfield.get()
    pyperclip.copy(rabdom_pass)
    # password=random.sample(all,pass_len)
    # passfield.insert(0,password)
def destroy_window():
    root.destroy()

root=Tk()
root.config(bg='gray32')
choice=IntVar()
Font=("Arial",13,'bold')
passLabel=Label(root,text="Password Generator",font=('arial', 20,'bold'),bg='gray32',fg="white")
passLabel.grid(pady=10)
weakradio=Radiobutton(root,text="Weak",value=1,variable=choice,font=Font)
weakradio.grid(pady=5)

medradio=Radiobutton(root,text="Medium",value=2,variable=choice,font=Font)
medradio.grid(pady=5)

strongradio=Radiobutton(root,text="Strong",value=3,variable=choice,font=Font)
strongradio.grid(pady=5) 

nameLabel=Label(root,text="Password Length",font=Font,bg='gray2',fg="white")
nameLabel.grid(pady=5)

boxlen=Spinbox(root,from_=5,to=18,width=5,font=Font)
boxlen.grid(pady=5)

genButton=Button(root,text="Generate",font=Font,command=gen)
genButton.grid(pady=5)

passfield=Entry(root,width=25,bd=2,font=Font)
passfield.grid()

copyButton=Button(root,text="Copy",font=Font,command=copy)
copyButton.grid(pady=5)

destroyButton = Button(root, text="Destroy", font=Font, command=destroy_window)
destroyButton.grid(pady=5)



root.mainloop()