import sqlite3, numpy as np
from fastembed import TextEmbedding

conexion = sqlite3.connect('conocimiento.db')
cursor = conexion.cursor()
cursor.execute('SELECT id, texto FROM fragmentos WHERE vector IS NULL')
filas = cursor.fetchall()
print('Cargando modelo de embeddings...')
modelo = TextEmbedding()
ids = [f[0] for f in filas]
textos = [f[1] for f in filas]
vectores = list(modelo.embed(textos))
for doc_id, vector in zip(ids, vectores):
    cursor.execute('UPDATE fragmentos SET vector = ? WHERE id = ?', (np.array(vector, dtype=np.float32).tobytes(), doc_id))
conexion.commit()
conexion.close()
print('Listo! Se indexaron:', len(ids), 'fragmentos')
