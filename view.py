from tkinter import Button, Frame, Label, Entry, IntVar, StringVar, DoubleVar, Tk, Variable
from tkinter.font import Font

class Login(Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        gap=20
        font=Font(size=20)
        self.__datos={
        "user":self.form(parent, "Usuario", font=font),
        "pass":self.form(parent, "Contraseña", row=1, font=font, show="*")
        }
        self.btnIngresar=Button(parent, text="Ingresar", font=font)
        self.btnIngresar.grid(row=2, columnspan=2, sticky="we", padx=gap)
        self.lblestado=Label(parent, text="", font=font)
        self.lblestado.grid(row=3, columnspan=2, sticky="we",padx=gap)

    def form(self, parent, label:str, font, column=0, row=0, show=None, gap=6)->StringVar:
        var=StringVar()
        Label(parent, text=label, font=font).grid(column=column, row=row, padx=gap, pady=gap)
        Entry(parent, textvariable=var, font=font, show=show).grid(column=column+1, row=row, padx=gap, pady=gap)

        return var

    @property
    def datos(self)->dict:       
        return {key: value.get() for key, value in self.__datos.items()}
    @datos.setter
    def datos(self, user="", password="")->None:
        self.__datos["user"].set(user)
        self.__datos["pass"].set(password)
            

