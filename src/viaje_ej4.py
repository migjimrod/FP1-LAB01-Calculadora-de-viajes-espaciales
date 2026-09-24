distancia_km = 225000000
for velocity in range(10000,50000,10000):
    tiempo_horas = distancia_km / velocity
    tiempo_dias = tiempo_horas / 24
    print(f"A la siguiente velocidad: {velocity}km/h, tardarías {tiempo_dias} días en llegar.")

    