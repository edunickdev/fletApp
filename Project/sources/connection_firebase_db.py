import os
import firebase_admin
from firebase_admin import credentials, db
from Project.sources.models.task import Task

# Configuración de las credenciales
ruta_actual  = os.getcwd()
access = credentials.Certificate("Project/sources/bdflet-56a12-firebase-adminsdk-nlgsb-7dfdd8293a.json")
firebase_admin.initialize_app(
    access,
    { "databaseURL": "https://bdflet-56a12-default-rtdb.firebaseio.com/" }
)

# Referencia a la raíz de la base de datos
ref = db.reference('/')

# Datos para agregar a la base de datos
# data: Task = {
#     'title': 'Tarea 8',
#     'start_date': '2023-08-21',
#     'end_date': '2023-08-28',
#     'description': 'Cenar con Roxi',
#     'category': 'Daily',
#     'suggestGPT': 'Tarea 8'
# }

# # Agregar datos a la colección "task"
def add_data(colection: str, data: Task):
    ref.child(colection).push(data)

# Referencia a la colección "task"
# task_ref = ref.child('task')

# Obtener un snapshot de los datos en "task"
# snapshot = task_ref.get()

def get_data(colection: str):
    colection_data = ref.child(colection)
    data = colection_data.get()
    return data

# db_tasks = get_data('task')


# Iterar a través de los datos y mostrarlos
# for key, value in snapshot.items():
#     pass
    # print(f'ID: {key}')
    # print(f'Titulo tarea: {value["title"]}')
    # print(f'Fecha Inicio: {value["start_date"]}')
    # print(f'Fecha Fin: {value["end_date"]}')
    # print(f'Descripción: {value["description"]}')
    # print(f'Categoría: {value["category"]}')
    # print(f'Sugerencia GPT: {value["suggestGPT"]}')
    # print('---------------------------')


# add_data('task', data)
