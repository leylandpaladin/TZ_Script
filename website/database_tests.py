import sqlite3

conn = sqlite3.connect('C:\\Users\Paltos\PycharmProjects\TZ_script\website\Devices.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute("SELECT * FROM devices")
test = cursor.fetchall()

for i in test:
    print(i)

conn.commit()
conn.close()


