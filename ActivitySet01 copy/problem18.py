import sqlite3


connection = sqlite3.connect('Email_DB.sqlite')
cursor = connection.cursor()

cursor.execute('''
        DROP TABLE IF EXISTS EMAIL_COUNT
    ''')

cursor.execute('''
        CREATE TABLE EMAIL_COUNT (
            EMAIL VARCHAR(100),
            COUNT INTEGER
        )
    ''')

# Process .txt file to DB
fname = input('Enter the file name : ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhandle = open(fname)

for line in fhandle:
    if not line.startswith('From: '):
        continue
    email = line.split()[1]

    # Check if the email is already in TABLE
    cursor.execute('SELECT COUNT FROM EMAIL_COUNT WHERE EMAIL = ?', (email,))
    row = cursor.fetchone()

    
    if row is None:
        cursor.execute('INSERT INTO EMAIL_COUNT (EMAIL, COUNT) VALUES(?,1)', (email,))

    
    else:
        cursor.execute('UPDATE EMAIL_COUNT SET COUNT = COUNT + 1 WHERE EMAIL = ?', (email,))

    connection.commit()


sql_query = 'SELECT * FROM EMAIL_COUNT ORDER BY COUNT DESC'

for row in cursor.execute(sql_query):
    print(row[0], row[1])

cursor.close()