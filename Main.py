print("Jose Antonio Ronquillo Meza")
print("Estudiante de ingenieria en sistemas")
print("Carnet: 1547223")
print("Universidad rafael landivar")

import os

mi_ubicacion = os.getcwd()
if os.path.exists("modulos"):
    print("La carpeta ya existe")
else:
    os.mkdir(mi_ubicacion + "\\modulos")
    archivo = open('./modulos/prueba.txt', 'w')
    archivo.write('Hola mundo')
    archivo.close()
