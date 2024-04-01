import sqlite3
 # crear conexion de bd
conn = sqlite3.connect("insituto.db")
#creando taala de la carrera
conn.execute("""
    CREATE TABLE Carrera
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    duracion INTEGER NOT NULL)
""")r
# Insertar datos de carreras
conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) 
    VALUES ('Ingeniería en Informática', 5)
    """
)
conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) 
    VALUES ('Licenciatura en Administración', 4)
    """
)
