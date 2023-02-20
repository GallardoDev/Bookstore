"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
import backend
import random
from tkinter import messagebox


def view_command():
	lista.delete(0,END)
	for article in backend.view():
		lista.insert(END, article)

def search_command():
	lista.delete(0,END)
	for article in backend.search(titleValue.get(), authorValue.get(), yearValue.get(), isbnValue.get()):
		lista.insert(END, article)

def add_command():
	backend.insert(titleValue.get(), authorValue.get(), yearValue.get(), isbnValue.get())
	lista.delete(0, END)
	lista.insert(END, (titleValue.get(), authorValue.get(), yearValue.get(), isbnValue.get()))
	messagebox.showinfo('Information', 'Book inserted succesfully')

def count():
	lista.delete(0,END)	
	numero=len(backend.view()),' books in the list'
	messagebox.showinfo('Number of books', numero)
	lista.insert(END, numero)

def get_selected_row(event):
	try:
		global selected_tuple
		index=lista.curselection()[0]
		selected_tuple=lista.get(index)
		entry_Title.delete(0, END)
		entry_Title.insert(END,selected_tuple[1])
		entry_Author.delete(0, END)
		entry_Author.insert(END,selected_tuple[2])
		entry_Year.delete(0, END)
		entry_Year.insert(END,selected_tuple[3])
		entry_ISBN.delete(0, END)
		entry_ISBN.insert(END,selected_tuple[4])
	except:
		pass

def delete_command():
	backend.delete(selected_tuple[0])
	messagebox.showinfo('Information', 'Book deleted succesfully.')

def update_command():
	backend.update(selected_tuple[0],titleValue.get(), authorValue.get(), yearValue.get(), isbnValue.get())
	messagebox.showinfo('Information', 'Book updated succesfully.')


def changeColor():
	colors=['green','blue','red','black','white','orange','yellow']
	random_colors=random.choice(colors)
	window.config(bg=random_colors)

window=Tk()
window.title('Bookstore')
window.iconbitmap()
window.resizable(0,0)
window.config(bg='white')
window.iconbitmap(r'D:\ADRIEL\PROGRAMACION\Python\Aplicaciones\bookstore\bookstore\books.ico')

barra_menu=Menu(window)
window.config(menu=barra_menu, width=300, height=300)
OPmenu=Menu(barra_menu, tearoff=0)
OPmenu.add_command(label='Number of books', command=count)
OPmenu.add_command(label='Change Color', command=changeColor)


barra_menu.add_cascade(label='Options', menu=OPmenu)


label_Title=Label(window, text='Title', relief=RAISED)
label_Title.config(bg='#aaaaaa')
label_Title.grid(row=0, column=0)
label_Author=Label(window, text='Author', relief=RAISED)
label_Author.config(bg='#aaaaaa')
label_Author.grid(row=0, column=2)
label_Year=Label(window, text='Year', relief=RAISED)
label_Year.config(bg='white')
label_Year.grid(row=1, column=0)
label_ISBN=Label(window, text='ISBN', relief=RAISED)
label_ISBN.config(bg='white')
label_ISBN.grid(row=1, column=2)

titleValue=StringVar()
entry_Title=Entry(window, textvariable=titleValue)
entry_Title.config(bg='aqua')
entry_Title.grid(row=0, column=1)
entry_Title.config(fg='green')

authorValue=StringVar()
entry_Author=Entry(window, textvariable=authorValue)
entry_Author.config(bg='aqua')
entry_Author.grid(row=0, column=3)
entry_Author.config(fg='green')

yearValue=StringVar()
entry_Year=Entry(window, textvariable=yearValue)
entry_Year.config(bg='aqua')
entry_Year.grid(row=1, column=1)
entry_Year.config(fg='green')

isbnValue=StringVar()
entry_ISBN=Entry(window, textvariable=isbnValue)
entry_ISBN.config(bg='aqua')
entry_ISBN.grid(row=1, column=3)
entry_ISBN.config(fg='green')

lista=Listbox(window, height=6, width=35)
lista.grid(row=2, column=0, columnspan=2, rowspan=6)
lista.config(bg='aqua')
lista.config(fg='green')

scroll1=Scrollbar(window, command=lista.yview)
scroll1.grid(row=2, column=2, rowspan=6)
lista.config(yscrollcommand=scroll1.set)


scroll2=Scrollbar(window, orient=HORIZONTAL, command=lista.xview)
scroll2.grid(row=7, column=0, columnspan=2, sticky='nsew')
lista.config(xscrollcommand=scroll2.set)

lista.bind('<<ListboxSelect>>', get_selected_row)

btn1=Button(window, text='View all', width=12, command=view_command)
btn1.grid(row=2, column=3)

btn2=Button(window, text='Search entry', width=12, command=search_command)
btn2.grid(row=3, column=3)

btn3=Button(window, text='Add entry', width=12, command=add_command)
btn3.grid(row=4, column=3)

btn4=Button(window, text='Update', width=12, command=update_command)
btn4.grid(row=5, column=3)

btn5=Button(window, text='Delete', width=12, command=delete_command)
btn5.grid(row=6, column=3)

btn6=Button(window, text='Close', width=12, command=window.destroy)
btn6.grid(row=7, column=3)

window.mainloop()