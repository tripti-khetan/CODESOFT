import tkinter
import tkinter.messagebox


def add():
    task = addtask_text.get("1.0", "end-1c")  # Get the task from the Text widget
    if task.strip():
        tobox.insert(tkinter.END, task)  # Insert the task into the Listbox
        addtask_text.delete("1.0", tkinter.END)


def delete():
    selected_index = tobox.curselection()
    if selected_index:
        tobox.delete(selected_index)

def edit():
    selected_index = tobox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        new_task = addtask_text.get("1.0", "end-1c")
        if new_task.strip():
            tobox.delete(selected_index)
            tobox.insert(selected_index, new_task)
            addtask_text.delete("1.0", tkinter.END)

root = tkinter.Tk()
root.title("ToDo List")
root.geometry('550x557')


heading_frame = tkinter.Frame(root, bg="black",borderwidth=4,relief="ridge")
heading_frame.pack()

heading_label = tkinter.Label(heading_frame, text="My ToDo List", font=("Times New Roman Italic", 24, "bold"), background='aquamarine4',fg="White")
heading_label.pack()

framelist = tkinter.Frame(root,bg="black",borderwidth=2,relief="solid")
framelist.pack()
tobox = tkinter.Listbox(framelist, height=10, width=25,font=("Arial", 15))
tobox.pack(side=tkinter.LEFT)

scroll = tkinter.Scrollbar(framelist)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

tobox.config(yscrollcommand=scroll.set)
addtask_frame=tkinter.Frame(root,bg="black",borderwidth=3,relief="raised")
addtask_frame.pack(pady=5)
addtask_text = tkinter.Text(addtask_frame, height=3, width=30, font=("Arial", 15))
addtask_text.pack()

addbutton = tkinter.Button(root, text="Add Task", font=("Arial", 20, "bold"), background="darkgoldenrod", width=40, command=add,borderwidth=2, relief="solid",activebackground='TAN4')
addbutton.pack()

delbutton = tkinter.Button(root, text="Delete Task", font=("Arial", 20, "bold"), background="darkkhaki", width=40,command=delete,borderwidth=2, relief="solid",activebackground='tan4')
delbutton.pack()

editbutton = tkinter.Button(root, text="Edit Task", font=("Arial", 20, "bold"), background="darkolivegreen4", width=40, command=edit,borderwidth=2, relief="solid",activebackground='tan4')
editbutton.pack()

root.mainloop()
