import sqlite3 as sql

con = sql.connect("database/data_source.db")
cur = con.cursor()
data = cur.execute('SELECT * FROM DevilFruits').fetchall()
con.close()
f = open("public/frontEndData.json", "w")
f.write("[\n")
for row in data:
    f.write('{\n')
    f.write(f'"extID":{row[0]},\n"Name":"{row[1]}",\n"Japanese_Name":"{row[2]}",\n"Type":"{row[3]}",\n"image":"{row[4]}",\n"Description":"{row[5]}",\n"wiki":"{row[6]}"\n')
    if row == data[len(data)-1]:
        f.write("}\n")
    else:
        f.write("},\n")
f.write("]\n")
f.close()

con = sql.connect("database/data_source.db")
cur = con.cursor()
data1 = cur.execute('SELECT * FROM "DevilFruits" WHERE "Type" = "Paramecia";').fetchall()
con.close()
a = open("public/frontEndData1.json", "w")
a.write("[\n")
for row in data1:
    a.write('{\n')
    a.write(f'"extID":{row[0]},\n"Name":"{row[1]}",\n"Japanese_Name":"{row[2]}",\n"Type":"{row[3]}",\n"image":"{row[4]}",\n"Description":"{row[5]}",\n"wiki":"{row[6]}"\n')
    if row == data1[len(data1)-1]:
        a.write("}\n")
    else:
        a.write("},\n")
a.write("]\n")
a.close()

con = sql.connect("database/data_source.db")
cur = con.cursor()
data2 = cur.execute('SELECT * FROM "DevilFruits" WHERE "Type" = "Zoan";').fetchall()
con.close()
b = open("public/frontEndData2.json", "w")
b.write("[\n")
for row in data2:
    b.write('{\n')
    b.write(f'"extID":{row[0]},\n"Name":"{row[1]}",\n"Japanese_Name":"{row[2]}",\n"Type":"{row[3]}",\n"image":"{row[4]}",\n"Description":"{row[5]}",\n"wiki":"{row[6]}"\n')
    if row == data2[len(data2)-1]:
        b.write("}\n")
    else:
        b.write("},\n")
b.write("]\n")
b.close()

con = sql.connect("database/data_source.db")
cur = con.cursor()
data3 = cur.execute('SELECT * FROM "DevilFruits" WHERE "Type" = "Logia";').fetchall()
con.close()
c = open("public/frontEndData3.json", "w")
c.write("[\n")
for row in data3:
    c.write('{\n')
    c.write(f'"extID":{row[0]},\n"Name":"{row[1]}",\n"Japanese_Name":"{row[2]}",\n"Type":"{row[3]}",\n"image":"{row[4]}",\n"Description":"{row[5]}",\n"wiki":"{row[6]}"\n')
    if row == data3[len(data3)-1]:
        c.write("}\n")
    else:
        c.write("},\n")
c.write("]\n")
c.close()