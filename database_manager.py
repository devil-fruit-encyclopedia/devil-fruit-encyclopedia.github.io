import sqlite3 as sql
con = sql.connect("database/data_source.db")
cur = con.cursor()
data = cur.execute('SELECT * FROM DevilFruits').fetchall()
con.close()
f = open("public/frontEndData.json", "w")
f.write("[\n")
for row in data:
    f.write('{\n')
    f.write(f'"extID":{row[0]},\n"Num":"{row[1]}",\n"Name":"{row[2]}",\n"Japanese_Name":"{row[3]}",\n"Type":"{row[4]}",\n"image":"{row[5]}",\n"User":"{row[6]}",\n"Description":"{row[7]}",\n"wiki":"{row[8]}",\n"Use":"{row[9]}"\n')
    if row == data[len(data)-1]:
        f.write("}\n")
    else:
        f.write("},\n")
f.write("]\n")
f.close()

con = sql.connect("database/data_source.db")
cur = con.cursor()
datac = cur.execute('SELECT * FROM "DevilFruits" WHERE "CanonDesign" = "canon";').fetchall()
con.close()
z = open("public/frontEndDataC.json", "w")
z.write("[\n")
for row in datac:
    z.write('{\n')
    z.write(f'"extID":{row[0]},\n"Num":"{row[1]}",\n"Name":"{row[2]}",\n"Japanese_Name":"{row[3]}",\n"Type":"{row[4]}",\n"image":"{row[5]}",\n"User":"{row[6]}",\n"Description":"{row[7]}",\n"wiki":"{row[8]}",\n"Use":"{row[9]}"\n')
    if row == datac[len(datac)-1]:
        z.write("}\n")
    else:
        z.write("},\n")
z.write("]\n")
z.close()

con = sql.connect("database/data_source.db")
cur = con.cursor()
datam = cur.execute('SELECT * FROM "DevilFruits" WHERE "Mine" = "yes";').fetchall()
con.close()
m = open("public/frontEndDataM.json", "w")
m.write("[\n")
for row in datam:
    m.write('{\n')
    m.write(f'"extID":{row[0]},\n"Num":"{row[1]}",\n"Name":"{row[2]}",\n"Japanese_Name":"{row[3]}",\n"Type":"{row[4]}",\n"image":"{row[5]}",\n"User":"{row[6]}",\n"Description":"{row[7]}",\n"wiki":"{row[8]}",\n"Use":"{row[9]}"\n')
    if row == datam[len(datam)-1]:
        m.write("}\n")
    else:
        m.write("},\n")
m.write("]\n")
m.close()

con = sql.connect("database/data_source.db")
cur = con.cursor()
data1 = cur.execute('SELECT * FROM "DevilFruits" WHERE "Type" = "Paramecia";').fetchall()
con.close()
a = open("public/frontEndData1.json", "w")
a.write("[\n")
for row in data1:
    a.write('{\n')
    a.write(f'"extID":{row[0]},\n"Num":"{row[1]}",\n"Name":"{row[2]}",\n"Japanese_Name":"{row[3]}",\n"Type":"{row[4]}",\n"image":"{row[5]}",\n"User":"{row[6]}",\n"Description":"{row[7]}",\n"wiki":"{row[8]}",\n"Use":"{row[9]}"\n')
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
    b.write(f'"extID":{row[0]},\n"Num":"{row[1]}",\n"Name":"{row[2]}",\n"Japanese_Name":"{row[3]}",\n"Type":"{row[4]}",\n"image":"{row[5]}",\n"User":"{row[6]}",\n"Description":"{row[7]}",\n"wiki":"{row[8]}",\n"Use":"{row[9]}"\n')
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
    c.write(f'"extID":{row[0]},\n"Num":"{row[1]}",\n"Name":"{row[2]}",\n"Japanese_Name":"{row[3]}",\n"Type":"{row[4]}",\n"image":"{row[5]}",\n"User":"{row[6]}",\n"Description":"{row[7]}",\n"wiki":"{row[8]}",\n"Use":"{row[9]}"\n')
    if row == data3[len(data3)-1]:
        c.write("}\n")
    else:
        c.write("},\n")
c.write("]\n")
c.close()

con = sql.connect("database/data_source.db")
cur = con.cursor()
datad = cur.execute('SELECT * FROM "DevilFruits" WHERE "Real" = "canon";').fetchall()
con.close()
d = open("public/frontEndDataCanon.json", "w")
d.write("[\n")
for row in datad:
    d.write('{\n')
    d.write(f'"extID":{row[0]},\n"Num":"{row[1]}",\n"Name":"{row[2]}",\n"Japanese_Name":"{row[3]}",\n"Type":"{row[4]}",\n"image":"{row[5]}",\n"User":"{row[6]}",\n"Description":"{row[7]}",\n"wiki":"{row[8]}",\n"Use":"{row[9]}"\n')
    if row == datad[len(datad)-1]:
        d.write("}\n")
    else:
        d.write("},\n")
d.write("]\n")
d.close()

con = sql.connect("database/data_source.db")
cur = con.cursor()
datae = cur.execute('SELECT * FROM "DevilFruits" WHERE "Real" = "not";').fetchall()
con.close()
e = open("public/frontEndDataNot.json", "w")
e.write("[\n")
for row in datae:
    e.write('{\n')
    e.write(f'"extID":{row[0]},\n"Num":"{row[1]}",\n"Name":"{row[2]}",\n"Japanese_Name":"{row[3]}",\n"Type":"{row[4]}",\n"image":"{row[5]}",\n"User":"{row[6]}",\n"Description":"{row[7]}",\n"wiki":"{row[8]}",\n"Use":"{row[9]}"\n')
    if row == datae[len(datae)-1]:
        e.write("}\n")
    else:
        e.write("},\n")
e.write("]\n")
e.close()