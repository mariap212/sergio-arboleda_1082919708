persona = {"nombre": "maria", "edad": 17, "ciudad": "santa marta"}

for clave in persona:
    print(clave) 
    
for clave, valor in persona.items():
    print(clave + ": " + str(valor))