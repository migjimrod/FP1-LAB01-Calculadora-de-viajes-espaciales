age = int(input("Ingresa tu edad"))
body = int(input("Introduce en una escala del 1-10 el nivel físico que posees:"))

while not (1<=body<=10):
    print("El valor no es válido")
    body = int(input("Introduce en una escala del 1-10 el nivel físico que posees:"))
if age < 18:
    print("Debes ser mayor de edad")
elif body < 5:
    print("Debes estar en mejor forma")
else:
    print("Listo para despegar")