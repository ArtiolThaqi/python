import sqlite3

connection = sqlite3.connect('example.db')
cursor = connection.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          position TEXT NOT NULL,
          department TEXT NOT NULL,
          salary REAL NOT NULL
          
       )

''')

#Commit the changes

connection.commit()


cursor.execute('''
      INSERT INTO employees (name, position, department, salary)
      VALUES (?, ?, ?, ?)
    


''',('John Doe','Software Engineer','IT',7000.00))

connection.commit()

cursor.execute('SELECT * FROM employees')

rows = cursor.fetchall() #shfaq krejt rezultatet

for row in rows:
    print(row)

cursor.execute('''
   UPDATE employees
   SET Salary = ?
   WHERE name = ?
''',(7500, 'John Doe'))
connection.commit()
cursor.execute('SELECT * FROM employees')

rows = cursor.fetchall() #shfaq krejt rezultatet

for row in rows:
    print(row)

cursor.execute('''
DELETE FROM employees
WHERE name = ?
''', ('John Doe',))
connection.commit()
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
connection.close()