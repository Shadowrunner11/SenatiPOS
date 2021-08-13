from tkinter import Tk
from view import Login
from model import searchPass, searchUser


class Controller_login:
    def __init__(self):
        self._ventana_login=Tk()
        self._ventana_login.title("Login facherito")
        self._login=Login(self._ventana_login)
        self._login.btnIngresar["command"]=self.ingresar
        self._login.mainloop()

    def ingresar(self):
        self._login.lblestado["text"]=self.validar()
        self._login.datos=""

    def validar(self)->str:
        """
        Validamos que no esten vacias las entradas y que el usuario exista,
        y su existe, validamos su contraseña

        :return "Ingresando", "Contraseña incorrecta", "No existe usuario"
        """
        d=self._login.datos
        if d["pass"] and d["user"]:
            if searchUser(d["user"]):
                return "Ingresando" if searchPass(d["user"], d["pass"]) else "Contra incorrecta"
            else:
                return "No existe el usuario"
        else:
            return "Campos vacios"
        
       
Controller_login()