recordatorios = [
    ['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]
]

# Requerimiento 3.1.
recordatorios.insert(0, ['2021-02-02', "06:00", "Empezar el año"])

# Requeri)miento 3.2.
recordatorios[3][0] = "2021-07-16"

# Requerimiento 3.3.
recordatorios.pop(1)

# Requerimiento 3.4.
recordatorios.append(["2021-12-24", "22:00", "Cena de Navidad"])
recordatorios.append(["2021-12-31", "22:00", "Cena de Año Nuevo"])

# Ordenar los recordatorios 
recordatorios.sort()

# Mostrar los recordatorios
print(recordatorios)