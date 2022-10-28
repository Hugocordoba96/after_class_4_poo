class Persona:

    def __init__(self, nombre=None, apellido=None, edad=None, dni=None, sexo=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.sexo = sexo
    
    def get_persona(self, dni):
        with open('recursos/datapersona.txt', 'r') as personas:
            for persona in personas:
                detalles = persona.split('|')
                if dni == detalles[0]:
                    return detalles
                else:
                    return None

    def set_persona(self):
        with open('recursos/datapersona.txt', 'a') as persona:
            persona.write(f'{self.dni}|{self.nombre}|{self.apellido}|{self.edad}|{self.sexo}|\n')