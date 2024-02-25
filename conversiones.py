# Importa la libreria solicitada para recibir argumentos.
import sys

# Variables a utilizar opcion A
clp_psol = float(sys.argv[1])
clp_parg = float(sys.argv[2])
clp_pusa = float(sys.argv[3])
dinero = float(sys.argv[4])

# Operación de conversión, recuerda que la fórmula es:
# cantidad_pesos * tasa_conversión = cantidad_moneda_convertida
soles = dinero * clp_psol
pesos_arg = dinero * clp_parg
dolares = dinero * clp_pusa

# Mostar el resultado de la conversión.
print(f"Los {dinero} pesos equivalen a:")
print(f"{soles} Soles")
print(f"{pesos_arg} Pesos Argentinos")
print(f"{dolares} Dólares")