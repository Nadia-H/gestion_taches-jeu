import tkinter as tk
from tkinter import ttk
import tkinter.ttk
import mysql.connector


def database_conn():
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
        print("Error while connecting to MySQL", e)


def load_frames():
    root = tk.Tk()
    root.title("task tracker")

    nom = tk.Label(text="Nom de la tâche: ")
    nom_entry = tk.Entry()
    priority = tk.Label(text="Priorté: ")
    priority_entry = ttk.Combobox(root, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    category = tk.Label(text="Catégorie")
    cat_entry = tk.Entry()
    estim_duration = tk.Label(text="Durée")
    dur_entry = tk.Entry()
    desc = tk.Label(text="Description")
    desc_entry = tk.Entry()
    date_due = tk.Label(text="Délai")
    date_due_entry = tk.Entry()
    annuler = tk.Button(root, text="Annuler")
    confirmer = tk.Button(root, text="Confirmer")
    nom.grid(column=0, row=0, padx=5, pady=5)
    nom_entry.grid(column=1, row=0, padx=5, pady=5)
    priority.grid(column=0, row=1, padx=5, pady=5)
    priority_entry.grid(column=1, row=1, padx=5, pady=5)
    category.grid(column=0, row=2, padx=5, pady=5)
    cat_entry.grid(column=1, row=2, padx=5, pady=5)
    estim_duration.grid(column=0, row=3, padx=5, pady=5)
    dur_entry.grid(column=1, row=3, padx=5, pady=5)
    desc.grid(column=0, row=4, padx=5, pady=5)
    desc_entry.grid(column=1, row=4, padx=5, pady=5)
    date_due.grid(column=0, row=5, padx=5, pady=5)
    date_due_entry.grid(column=1, row=5, padx=5, pady=5)
    annuler.grid(column=0, row=6, padx=5, pady=5)
    confirmer.grid(column=1, row=6)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tache")
    for row in cursor:
        print(row)

    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    database_conn()
    load_frames()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
