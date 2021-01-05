import sqlite3

conn = sqlite3.connect(r'D:\Projects\recipes\recipes.db')
cursor = conn.cursor()

cursor.execute(f"select * from `order`")
data = cursor.fetchall()

cursor.close()
conn.close()

conn = sqlite3.connect(r'D:\Projects\kitchen\db.sqlite3')
cursor = conn.cursor()
print(data)
cursor.executemany('insert into main_order VALUES (Null, ?, ?, ?)', data)
conn.commit()
cursor.close()
conn.close()