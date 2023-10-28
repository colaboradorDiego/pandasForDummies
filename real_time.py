import pandas as pd

"""
Lo importante a destacar en el siguiente ejemplo es la recomendacion de
NO AGREGAR FILAS AL DATAFRAME UNA VEZ CREADO, ESTO ES UNA MUY MALA IDEA, en su
lugar trabajar sobre una lista y luego agregar la lista al dataframe
"""

columnas = [
    "Venta",
    "Compra",
    "Spread TNA %",
    "Spread %",
    "Spread Last %",
    "P&L $",
    "Caucion $",
    "Comision $",
    "Venta $",
    "Compra $"
]

data = [
    ["AL30-CI", "AL30-48hs", 203.48, 0.07, -0.23, 1007, 467.347, 1676, 15525.20, 15510.80],
    ["GD30-CI", "GD30-48hs", 139.06, -0.40, 0.38, 346, 302210, 663, 23440.5, 23535.00]
]

df = pd.DataFrame(data, columns=columnas)

print(df)
