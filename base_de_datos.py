import sqlite3

conexion=sqlite3.connect("base_pichulas.db")

conexion.execute("""create table if not exists Pichulas(
                    id integer primary key AUTOINCREMENT,
                    nombre varchar,
                    edad integer,
                    gusto varchar
                    )""")
conexion.close()


conexion = sqlite3.connect("base_pichulas.db")

#pichula 1
conexion.execute("Insert into Pichulas(nombre,edad,gusto) values(?,?,?)",("Ortiz",19, "  Keanu Reeves"))
#pichula 2
conexion.execute("Insert into Pichulas(nombre,edad,gusto) values(?,?,?)",("Amanda",18,"  salami "))
#pichula 3
conexion.execute("Insert into Pichulas(nombre,edad,gusto) values(?,?,?)",("Islas",18,"   Capybaras"))
#pichula 4
conexion.execute("Insert into Pichulas(nombre,edad,gusto) values(?,?,?)",("Leo",19,"     WWE "))
#pichula 5
conexion.execute("Insert into Pichulas(nombre,edad,gusto) values(?,?,?)",("Michell",19," Bebé y yoshi xd "))
#pichula 6
conexion.execute("Insert into Pichulas(nombre,edad,gusto) values(?,?,?)",("Raul",18,"    el anime "))
#pichula 7
conexion.execute("Insert into Pichulas(nombre,edad,gusto) values(?,?,?)",("Renata",18,"  Gatos (supongo xd) "))
#pichula 8
conexion.execute("Insert into Pichulas(nombre,edad,gusto) values(?,?,?)",("Valud",19,"   no se que le gusta "))

conexion.commit()

pichula1 = conexion.execute("select * from pichulas where nombre = 'Ortiz'")
pichula2 = conexion.execute("select * from pichulas where nombre = 'Amanda'")
pichula3 = conexion.execute("select * from pichulas where nombre = 'Islas'")
pichula4 = conexion.execute("select * from pichulas where nombre = 'Leo'")
pichula5 = conexion.execute("select * from pichulas where nombre = 'Michell'")
pichula6 = conexion.execute("select * from pichulas where nombre = 'Raul'")
pichula7 = conexion.execute("select * from pichulas where nombre = 'Renata'")
pichula8 = conexion.execute("select * from pichulas where nombre = 'Valud'")

fila1=pichula1.fetchone()
fila2=pichula2.fetchone()
fila3=pichula3.fetchone()
fila4=pichula4.fetchone()
fila5=pichula5.fetchone()
fila6=pichula6.fetchone()
fila7=pichula7.fetchone()
fila8=pichula8.fetchone()

print(fila1)
print(fila2)
print(fila3)
print(fila4)
print(fila5)
print(fila6)
print(fila7)
print(fila8)

conexion.close()