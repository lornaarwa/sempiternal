import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql
tasks=
def add_task():
  task_string=task_field.get()
  if len(task_string)==0:
    messagebox.showinfo('error','field is empty')
    else:
      tasks.append(task_string)
      the_cursor.execute('insert into tasks values(?)',(task_string))
      list_update()
      task_field.delete(0,'end')
def list_update():
  clear_list()
  for task in tasks:
    task_listbox.insert('end',task)
def delete_task():
  try:
    the_value=task_listbox.get(task_listbox.curselection())
    if the_value in tasks:
      tasks.remove(the_value)
      list_update()
      the_cursor.execute('delete from tasks where title=?',(the_value))
  except:
    messagebox.showinfo('Error','no task selected.cannot delete')
def delete_all_tasks():
  message_box=messagebox.askyesno('delete all','are you sure?')
  if message_box==True:
    while(len(tasks)!=0):
      tasks.pop()
      the_cursor.execute('delete from tasks')
      list_update()
  def clear_list():
    task_listbox.delete(0,'end')
  def close():
    print(tasks)
    guiWindow.destroy()
  def retrieve_database():
    while(len(tasks)!=0):
      tasks.pop()
    for row in the_cursor.execute('select title from tasks'):
      tasks.append(row[0])
  if__name__=="__main__"
      guiWindow=tk.Tk()
    do 
