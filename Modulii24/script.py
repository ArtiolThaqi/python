
import sqlite3

conn = sqlite3.connect('pyadvanced24.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL,
        price NUMERIC NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        date_time TEXT,
        place TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        product_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (product_id) REFERENCES products(id)
    );
''')



#cursor.execute("INSERT INTO products(product_name, price) VALUES ('IPhone18',1500);")
#cursor.execute("INSERT INTO orders(date_time,place,user_ID,product_ID) VALUES ('17-10-2026 12:30','XK',2,1);")
#cursor.execute("UPDATE products SET ID=1")
conn.commit()
cursor.execute('''
    SELECT p.product_name, u.name, o.*
    FROM orders o INNER JOIN products p
    ON o.product_id = p.id INNER JOIN users u
    ON u.id=o.user_id;

''')
record_from_db=cursor.fetchall()
for row in record_from_db:
    print(row)