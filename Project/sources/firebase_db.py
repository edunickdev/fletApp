import firebase_admin
from firebase_admin import credentials, db
from models.user import User

# Configuración de las credenciales
access = credentials.Certificate("bdflet-firebase-adminsdk-mdm4q-1a0e6f276f.json")
firebase_admin.initialize_app(
    access,
    { "databaseURL": "https://bdflet-default-rtdb.firebaseio.com/" }
)

# Referencia a la raíz de la base de datos
ref = db.reference('/')

# Datos para agregar a la base de datos
data: User = {
    'nombre': 'Juan',
    'edad': 25,
    'ocupacion': 'Desarrollador'
}

# Agregar datos a la colección "usuarios"
def add_data(colection: str, data: User):
    ref.child(colection).push(data)

# Referencia a la colección "usuarios"
usuarios_ref = ref.child('usuarios')

# Obtener un snapshot de los datos en "usuarios"
snapshot = usuarios_ref.get()

# Iterar a través de los datos y mostrarlos
for key, value in snapshot.items():
    print(f'ID: {key}')
    print(f'Nombre: {value["nombre"]}')
    print(f'Edad: {value["edad"]}')
    print(f'Ocupación: {value["ocupacion"]}')
    print('---')
