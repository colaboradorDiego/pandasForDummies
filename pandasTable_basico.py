import pandas as pd
import tkinter as tk
from pandastable import Table, TableModel

class DataSetTasa:
    def __init__(self):
        # orient=index toma a las keys como records
        self.data_df = data_df = pd.read_json("data/tasa.json", orient='index')

    def get_data_frame(self):
        return self.data_df

class DataSetBonos:
    def __init__(self):
        self.columnas = [
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

        self.data = [
            ["AL30-CI", "AL30-48hs", 203.48, 0.07, -0.23, 1007, 467.347, 1676, 15525.20, 15510.80],
            ["GD30-CI", "GD30-48hs", 139.06, -0.40, 0.38, 346, 302210, 663, 23440.5, 23535.00]
        ]

    def get_data_frame(self):
        return pd.DataFrame(self.data, columns=self.columnas)


class Formulario:
    def __init__(self, ventana, data):
        self.ventana = ventana

        self.ventana_tabla = tk.Frame(ventana, width=600, height=250, bd=2)
        self.ventana_tabla.place(x=20, y=20)

        self.tabla = Table(
            self.ventana_tabla, dataframe=data,
            showtoolbar=False,
            showstatusbar=True,
            editable=False)

        # PandasTable Show
        self.tabla.show()

        # Frame show
        self.ventana_tabla.pack(fill='both', expand=True)


gui = tk.Tk()

def init():
    if __name__ == '__main__':
        gui.title('PandasTable')
        gui.geometry("800x300")

        a = DataSetBonos()
        b = DataSetTasa()
        f = Formulario(gui, b.get_data_frame())

        gui.mainloop()

init()
