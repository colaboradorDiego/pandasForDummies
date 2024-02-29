import pandas as pd
import tkinter as tk
from pandastable import Table, TableModel

class DataSetTasa:
    def __init__(self):

        self.data = {
            "AL30": {
            "panel": "Bonos",
            "especie": "AL30",
            "precio_cpra": 11198,
            "precio_vta": 11230,
            "tasa": 0.286,
            "ratio": 20000,
            "cantidad_max_cpra": 20000,
            "cantidad_max_vta": 1,
            "min": 0.228,
            "max": 0.568,
            "operar": False
        },
            "TX24": {
                "panel": "Bonos",
                "especie": "TX24",
                "precio_cpra": 464,
                "precio_vta": 465,
                "tasa": 0.216,
                "ratio": 0.215,
                "cantidad_max_cpra": 21456,
                "cantidad_max_vta": 100000,
                "min": -0.237,
                "max": 0.411,
                "operar": True
            }
        }

        # orient=index toma a las keys como records
        #self.data_df = pd.read_json("data/tasa.json", orient='index')

        self.data_df = pd.DataFrame.from_dict(self.data, orient='index')

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
    def __init__(self, ventana):
        self.gui = ventana

        self.frame = tk.Frame(self.gui, width=600, height=250, bd=2)
        self.frame.place(x=20, y=20)


        self.datos = pd.DataFrame()

        self.tabla = Table(
            self.frame, dataframe=self.datos,
            showtoolbar=False,
            showstatusbar=True,
            editable=False)

        # call to show
        self.dibujar()

    def set_data(self, datos):
        self.datos = datos
        self.tabla.model.df = datos
        self.tabla.redraw()


    def dibujar(self):
        # PandasTable Show
        self.tabla.show()
        self.frame.pack(fill='both', expand=True)

    def cerrar(self):
        print("entra al cierre por aca")
        self.gui.destroy()



def init():
    if __name__ == '__main__':
        gui = tk.Tk()
        gui.title('PandasTable')
        gui.geometry("800x300")

        # Dataset demostracion
        a = DataSetBonos()
        b = DataSetTasa()

        # Formularios, Frame
        f = Formulario(gui)

        gui.protocol("WM_DELETE_WINDOW", f.cerrar)

        f.set_data(b.get_data_frame())

        gui.mainloop()

init()
