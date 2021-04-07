import sqlite3

connection = sqlite3.connect('attendance.db')
cursor = connection.cursor()
connection.rollback()
connection.commit()
try:
    cursor.execute(
        'CREATE TABLE MarkAttendance(id INTEGER PRIMARY KEY,UID INTEGER,datee TEXT,InTime TEXT,OutTime TEXT)')
except:
    print("File Already Exist")
finally:
    # cursor.execute('INSERT INTO MarkAttendance(UID,datee,InTime,OutTime) VALUES(?,?,?,?)',(123, "12/11", "12:00", "01:00"))
    # cursor.execute('INSERT INTO MarkAttendance(UID,InTime,OutTime) VALUES(?,?,?)', (345, "12:30", "01:30"))
    # cursor.execute('DELETE FROM MarkAttendance WHERE UID=1')
    cursor.execute('SELECT * FROM MarkAttendance')
    row = cursor.fetchone()
    while row is not None:
        uin = row[1]
        datee = row[2]
        Time = row[3]
        # call fun(uin,inTime,outTime)
        print("UIN : "+str(uin)+"\ndatee : "+datee+"\nTime : " +
              str(Time))
        row = cursor.fetchone()
    # print("id "+ str(url_id[0]))
    # cursor.execute('DROP TABLE MarkAttendance')
    connection.commit()
