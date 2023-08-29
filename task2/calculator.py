from tkinter import *
from tkinter.messagebox import *
font=('Times New Roman Italic',22,"bold")
#### Function###
def single_clear():  ##3Single Clear
    ex=textField.get()
    ex=ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(0,ex)
def aclear():   ####AllClear button
    textField.delete(0,END)
def clickButton(ent):
    print("Btn Click")
    b=ent.widget
    text=b['text']
    print(text)
    if text=='x':
        textField.insert(END,"*")
        return
    if text=='=':
        try:
            ex=textField.get()
            res=eval(ex)
            textField.delete(0,END)
            textField.insert(0,res)
        except Exception as e:
            print("Error",e)
            showerror("Error",e)
        return
    textField.insert(END,text)
root=Tk()
root.title("My Calculator")
root.geometry('399x490')
####### pic Label
ima=PhotoImage(file='calu.png')
headingLabel=Label(root,image=ima)
headingLabel.pack(side=TOP,pady=15)

head=Label(root,text='My Calculator',font=font)
head.pack(side=TOP)

###Text Area###
textField=Entry(root,font=font,justify=CENTER)
textField.pack(side=TOP,pady=10,fill=X,padx=10)

###Button Frame  Area###
btnFm=Frame(root)
btnFm.pack(side=TOP,padx=10)

###Add Button Area#####
num=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(btnFm,text=str(num),font=font,width=5,relief='sunken',activebackground='blue',activeforeground="white")
        btn.grid(row=i,column=j,padx=4,pady=4)
        num+=1
        btn.bind('<Button-1>',clickButton)
zbtn= btn=Button(btnFm,text="0",font=font,width=5,relief='sunken',activebackground='blue',activeforeground="white")
zbtn.grid(row=3,column=0)
dbtn= btn=Button(btnFm,text=".",font=font,width=5,relief='sunken',activebackground='blue',activeforeground="white")
dbtn.grid(row=3,column=1)
ebtn= btn=Button(btnFm,text="=",font=font,width=5,relief='sunken',activebackground='blue',activeforeground="white")
ebtn.grid(row=3,column=2)
adbtn= btn=Button(btnFm,text="+",font=font,width=5,relief='sunken',activebackground='blue',activeforeground="white")
adbtn.grid(row=0,column=3)
subbtn= btn=Button(btnFm,text="-",font=font,width=5,relief='sunken',activebackground='blue',activeforeground="white")
subbtn.grid(row=1,column=3)
mulbtn= btn=Button(btnFm,text="x",font=font,width=5,relief='sunken',activebackground='blue',activeforeground="white")
mulbtn.grid(row=2,column=3)
divbtn= btn=Button(btnFm,text="%",font=font,width=5,relief='sunken',activebackground='blue',activeforeground="white")
divbtn.grid(row=3,column=3)
zzbtn= btn=Button(btnFm,text="00",font=font,width=5,relief='sunken',activebackground='blue',activeforeground="white")
zzbtn.grid(row=4,column=2)
inbtn= btn=Button(btnFm,text="/",font=font,width=5,relief='sunken',activebackground='blue',activeforeground="white")
inbtn.grid(row=4,column=3)
clbtn= btn=Button(btnFm,text="C",font=font,width=5,relief='sunken',activebackground='blue',activeforeground="white",command=single_clear)
clbtn.grid(row=4,column=0)
allclbtn= btn=Button(btnFm,text="AC",font=font,width=5,relief='sunken',activebackground='blue',activeforeground="white",command=aclear)
allclbtn.grid(row=4,column=1)

####Bindiang  Buttons####
adbtn.bind('<Button-1>',clickButton)
subbtn.bind('<Button-1>',clickButton)
mulbtn.bind('<Button-1>',clickButton)
divbtn.bind('<Button-1>',clickButton)
zbtn.bind('<Button-1>',clickButton)
ebtn.bind('<Button-1>',clickButton)
dbtn.bind('<Button-1>',clickButton)
zzbtn.bind('<Button-1>',clickButton)
inbtn.bind('<Button-1>',clickButton)
root.mainloop()