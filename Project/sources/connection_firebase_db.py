import os
import firebase_admin
from firebase_admin import credentials, db
from models.task import Task

# Configuración de las credenciales
ruta_actual  = os.getcwd()
access = credentials.Certificate("Project/sources/bdflet-firebase-adminsdk-mdm4q-0b51280ea8.json")
firebase_admin.initialize_app(
    access,
    { "databaseURL": "https://bdflet-default-rtdb.firebaseio.com/" }
)

# Referencia a la raíz de la base de datos
ref = db.reference('/')

# Datos para agregar a la base de datos
data: Task = {
    'title': 'Tarea 8',
    'start': '2023-08-21',
    'end': '2023-08-28',
    'description': 'Cenar con Roxi',
    'category': 'Daily',
    'suggestGPT': 'Tarea 8'
}

# Agregar datos a la colección "task"
def add_data(colection: str, data: Task):
    ref.child(colection).push(data)

# Referencia a la colección "task"
task_ref = ref.child('task')
print(f'lista de tareas {task_ref.get()}')

# Obtener un snapshot de los datos en "task"
snapshot = task_ref.get()

# Iterar a través de los datos y mostrarlos
for key, value in snapshot.items():
    print(f'ID: {key}')
    print(f'Titulo tarea: {value["title"]}')
    print(f'Fecha Inicio: {value["start"]}')
    print(f'Fecha Fin: {value["end"]}')
    print(f'Descripción: {value["description"]}')
    print(f'Categoría: {value["category"]}')
    print(f'Sugerencia GPT: {value["suggestGPT"]}')
    print('---------------------------')


add_data('task', data)
