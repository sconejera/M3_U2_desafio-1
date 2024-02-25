import sys

# Leer el archivo, recuerda pasarlo como argumento, viene del material del desafio.
with open(sys.argv[1], "r") as file:
    texto = file.read()

# Contar caracteres.
n_caracteres = len(set(texto))

# Contar palabras, recuerda que las palabras están separadas por espacios.
# Puedes usar el método split() para separar las palabras.
n_palabras = len(set(texto.split()))

# Output
print(f'El número de caracteres distintos es: {n_caracteres}')
print(f'El número de palabras distintas es: {n_palabras}')