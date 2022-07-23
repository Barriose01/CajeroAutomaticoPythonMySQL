from BDRegistroEInicio import Conexion 
from menuPrincipalCajero import MenuCajero
cn = Conexion()


class MenuInicio:
    def registroDeUsuario(self):
        while True:
            print("\nREGISTRO DE CUENTA")
            print("Presione (q) para volver al menu anterior")
            nombre = input("Ingrese su primer nombre: ").title().strip()
            if nombre == "Q":
                break
            apellido = input("Ingrese su apellido: ").title().strip()
            if apellido == "Q":
                break
            rut = input("Ingrese su Rut (Sin dv, sin guiones y sin punto): ").strip()
            if rut == "q":
                break
            dv = input("Ingrese el DV: ").lower().strip()
            if dv == "q":
                break
            clave = input("Ingrese una clave de 4 digitos: ").strip()
            if clave == "q":
                break
            clave2 = input("Introduzca nuevamente la clave: ").strip()
            if clave2 == "q":
                break
            if clave != clave2:
                print("\nLas claves no coinciden")
            else:
                cuentaValida = cn.cuentaValida(rut,dv,clave)
                if cuentaValida == False:
                    print("\nDebe ingresar informacion valida. Revise su rut, dv o clave")
                else:
                    cuentaExiste = cn.obtenerInfoCuenta(rut,dv)
                    if len(cuentaExiste) > 0:
                        print("\nLo sentimos, la cuenta ingresada ya existe")
                    else:
                        cn.registrarUsuario(rut,dv,clave,nombre,apellido)
                        cn.registrarLog(rut,dv)
                        print("\nLa cuenta ha sido registrada con exito")
                        break

    def iniciarSesion(self):
        while True:
            print("\nINICIO DE SESION")
            print("Presione (q) para volver al menu anterior")
            rut = input("Ingrese su Rut (Sin dv, sin guiones y sin punto): ").strip()
            if rut == "q":
                break
            dv = input("Ingrese el DV: ").lower().strip()
            if dv == "q":
                break
            clave = input("Ingrese una clave de 4 digitos: ").strip()
            if clave == "q":
                break
            cuenta = cn.obtenerInfoCuenta(rut,dv) #Este metodo siempre devolvera una sola tupla dentro de una lista
            if len(cuenta) > 0:
                if clave == str(cuenta[0][5]): #Con [0] accedo a la tupla. Con [5] accedo al campo 'clave'
                    id = cuenta[0][0] #El segundo [0] representa la posicion donde se encuentra el id
                    mc = MenuCajero(rut,dv,id)
                    mc.menuPrincipal()
                    break
                else:
                    print("\nLa clave que ingreso es incorrecta")
            else:
                print("\nLa cuenta ingresada no esta registrada")

while True:
    menu = MenuInicio()
    print("\n(1): Registrar Cuenta")
    print("(2): Iniciar Sesion")
    print("(3): Salir")
    
    opcion = input().lower().strip()
    if opcion == "3":
        break
    elif opcion == "1":
        menu.registroDeUsuario()
    
    elif opcion == "2":
        menu.iniciarSesion()
    else:
        print("\nIngrese una opcion valida")

    