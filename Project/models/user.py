class User:
    
    def __init__(self, nombre: str, edad: int, ocupacion: str):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
        
    def __str__(self):
        return f'Nombre: {self.nombre}\nEdad: {self.edad}\nOcupación: {self.ocupacion}'
    
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'edad': self.edad,
            'ocupacion': self.ocupacion
        }
    