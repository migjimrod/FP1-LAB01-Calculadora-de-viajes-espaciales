limit = 150000
ask = int(input("Ingresa la distancia a la que deseas llegar en km:"))
stops = 0
while ask > limit:
    print(f"Tienes que parar en {limit}km")
    stops += 1
    limit += 150000
print(f"El total de paradas para repostar es:{stops}")
