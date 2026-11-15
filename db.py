import sqlite3

def crear_base_datos():
    conexion = sqlite3.connect("conocimiento.db")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fragmentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            archivo TEXT,
            texto TEXT,
            vector BLOB
        )
    """)
    conexion.commit()
    conexion.close()
    print("Base de datos 'conocimiento.db' creada con exito.")

if __name__ == "__main__":
    crear_base_datos()
