#from persona import Persona

#persona1 = Persona('Alejo', 'Delgado', 23, '99919240124', 'M')

#print(persona1.get_persona('99919240124'))

#from clase import Clase

#clase1 = Clase('34635', 'Python', 'Programacion', '19-21h', 'lu-mi')

#clase1.set_clase()

#from alumno import Alumno

#alumno1 = Alumno('Alejo', 'Delgado', 23, '99919240124', 'M', '1234', '34635')

#alumno1.set_alumno()

#print(alumno1.get_alumno('1234'))

from profesor import Profesor

profesor1 = Profesor('Alejo', 'Delgado', 23, '99919240124', 'M', 'Developer', '12345',  '34635')

#profesor1.set_profesor()

print(profesor1.get_profesor('99919240124'))