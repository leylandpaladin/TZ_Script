import sqlite3
import os



conn = sqlite3.connect('D:\Документы\GitHub\TZ_Script\website\Devices.db', check_same_thread=False)
cursor = conn.cursor()
if not os.path.exists('D:\Документы\GitHub\TZ_Script\website\Devices.db'):


    cursor.execute('''CREATE TABLE devices(
            category text,
            type text,
            name text,
            description text,
            description2 text)
        ''')



#DATATYPES:
#NULL
#INTEGER
#REAL
#BLOB
#TEXT


# применить изменения
    conn.commit()
# закрть соеденение

    conn.close()
else:
    print('База данных найдена')

#cursor.execute("INSERT INTO devices VALUES ('test device','ogloblya', 'device used to beat people')")




def append_database(category, type, name, description, description2):
    cursor.execute(f"""INSERT INTO devices VALUES(
                    '{category}',
                    '{type}',
                    '{name}',
                    '{description}',
                    '{description2}')""")
    print('Запись добавлена')

    cursor.execute("SELECT * FROM devices")
    cursor.fetchall()

    conn.commit()




