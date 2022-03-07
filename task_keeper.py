from tkinter import *
from tkinter import messagebox
#import mysql.connector


"""def database_conn():
    import mysql.connector
    from mysql.connector import Error

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='task_manager',
                                             user='root',
                                             password='mysql')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)"""


def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Veuillez entrer une tâche.")


def deleteTask():
    lb.delete(ANCHOR)


root = Tk()
root.geometry('500x450+500+200')
root.title('Task Keeper')
root.config(bg='#08a950')
root.resizable(width=True, height=False)

frame = Frame(root)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=30,
    height=10,
    font=('Times', 18),
    bd=0,
    fg='#120078',
    highlightthickness=0,
    selectbackground='#010101',
    activestyle="none",

)
lb.pack(side=LEFT, fill=BOTH)


task_list = ['prendre un café',
    'étudier',
    'aller à la salle de gym',
    'write software',
    'write documentation',
    'take a nap',
    'read something',
    'aller à epi',
    'faire les mini projets',
    'dormir'
]
"""conn = database_conn()
conn.execute("SELECT * FROM tache")
for row in conn:
    task_list.append(row)
"""
for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    root,
    font=('times', 24)
)

my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Ajouter une tache',
    font=('times 14'),
    bg='#c0a776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Supprimer une tache',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=15,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

root.mainloop()