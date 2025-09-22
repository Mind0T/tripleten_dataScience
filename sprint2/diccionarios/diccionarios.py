personas={
    'Nombre':['Jaime','Irving','Dilan'],
    'Edad':[62,33,29],
    'Ocupacion':['Jubilado','Estudiante','Programador']
}

personas.update({'Edad':[63,34,30]})
for clave, valor in personas.items():
    print(f"{clave} {valor}")



claves=personas.keys()
print(f"Estas son las claves de la lista:\n{claves}")

#Update Dictionary 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year":2020})