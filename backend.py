import sqlite3

def conect():
	conex=sqlite3.connect('bookstore.db')
	curs=conex.cursor()
	curs.execute('CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
	conex.commit()
	conex.close()

def insert(title, author, year, isbn):
	conex=sqlite3.connect('bookstore.db')
	curs=conex.cursor()
	curs.execute('INSERT INTO book VALUES(NULL,?,?,?,?)',(title,author,year,isbn))
	conex.commit()
	conex.close()

def view():
	conex=sqlite3.connect('bookstore.db')
	curs=conex.cursor()
	curs.execute('SELECT * FROM book')
	rows=curs.fetchall()
	conex.close()
	return rows

def search(title='', author='', year='', isbn=''):
	conex=sqlite3.connect('bookstore.db')
	curs=conex.cursor()
	curs.execute('SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?', (title, author, year, isbn))
	rows=curs.fetchall()
	conex.close()
	return rows

def delete(item):
	conex=sqlite3.connect('bookstore.db')
	curs=conex.cursor()
	curs.execute('DELETE FROM book WHERE id=?', (item,))
	conex.commit()
	conex.close()

def update(id, title, author, year, isbn):
	conex=sqlite3.connect('bookstore.db')
	curs=conex.cursor()
	curs.execute('UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?', (title, author, year, isbn, id))
	conex.commit()
	conex.close()

conect()
#insert('Harry Potter5', 'J. K. Rowlins', 2007, 1000001)
print(view())
#print(search(isbn=1000000))
#delete(4)
#update(1, 'John Wick', 'Juan Lopez', 2021, 1000002)