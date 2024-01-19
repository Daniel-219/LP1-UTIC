nombre = "Daniel"
apellido = "Rodriguez"
edad = 26
peso = 65.5
# array o arreglo
print("El nombre es {}". format(nombre))
print(type(nombre))
print(type(edad))
print(type(peso))

# intentar el parsing
edad_en_string = str(edad)
print(f"""La edad anterior era {type(edad)},
       la edad parseada es de tipo 
      {type(edad_en_string)}""")