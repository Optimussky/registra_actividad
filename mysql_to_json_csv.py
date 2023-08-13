import mysql.connector
import json
import pandas as pd
from datetime import datetime

# Conexión a la base de datos MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tkregistro",
    port=3307
)

cursor = conn.cursor()

# Ejecutar consulta
tabla = 'registros'
#query = f"SELECT * FROM {tabla};"
query = f"""select r.idTipo,t.tipo,r.fecha,r.area,r.asunto 
from {tabla} r
inner join cattipo t on t.id=r.idTipo;"""

cursor.execute(query)
results = cursor.fetchall()

# Convertir resultados a JSON
def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')


json_data = []
for row in results:
    json_data.append({
        'ID': row[0], 
        'idTipo': row[1], 
        'fecha': row[2], 
        'area': row[3],
        'asunto': row[4],
    })

with open('resultados.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4, default=serialize_datetime)

# Convertir resultados a DataFrame de pandas
df = pd.DataFrame(results, columns=['ID', 'idTipo', 'fecha', 'area', 'asunto'])

# Guardar DataFrame en archivo CSV
df.to_csv('resultados.csv', index=False)

# Cerrar la conexión
conn.close()
