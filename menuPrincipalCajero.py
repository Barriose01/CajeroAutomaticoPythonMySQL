from BDRegistroEInicio import Conexion 
from BDMenuCajero import BDCajero
cn = Conexion()
bc = BDCajero()
class MenuCajero:
    def __init__(self,rut,dv, id):
        self.rut = rut
        self.dv = dv
        self.id = id
        self.saldo = self.obtenerSaldo()
        
    def menuPrincipal(self):
        while True:
            print("\nBIENVENIDO AL CAJERO AUTOMATICO")
            print("(1): Consultar saldo")
            print("(2): Hacer retiro")
            print("(3): Hacer deposito")
            print("(4): Ver movimientos")
            print("(5): Salir")
            opcion = input().lower().strip()

            if opcion == "5":
                break
            elif opcion == "1":
                print("Su saldo es de: $" + str(self.saldo))
            elif opcion == "2":
                self.hacerRetiro()
            elif opcion == "3":
                self.deposito()
            elif opcion == "4":
                self.movimientos()
            else:
                print("\nIngrese una opcion valida")

    def obtenerSaldo(self):
        cuenta = cn.obtenerInfoCuenta(self.rut,self.dv)
        self.saldo = cuenta[0][6] #Con [0] ingreso a la tupla. Con [6] ingreso al campo 'saldo'
        return self.saldo

    def hacerRetiro(self):
        while True:
            print("\nELIJA EL MONTO A RETIRAR")
            print("(1): 1000")
            print("(2): 5000")
            print("(3): 10000")
            print("(4): 50000")
            print("(5): Ingresar monto")
            print("(6): Volver")
            opcion = input().lower().strip()
            if opcion == "6":
                break
            elif opcion == "1":
                self.retiro(1000)
            elif opcion == "2":
                self.retiro(5000)
            elif opcion == "3":
                self.retiro(10000)
            elif opcion == "4":
                self.retiro(50000)
            elif opcion == "5":
                monto = self.ingresarMonto("retirar")
                if monto != -1 and monto != -2:
                    self.retiro(monto)
            elif opcion == "6":
                break
            else:
                print("\nDebe ingresar una opcion valida")

    def retiro(self, monto):
        if self.saldo < monto:
            print("\nNo tienes saldo suficiente para realizar esta operacion")
        else:
            self.saldo -= monto
            bc.retiro(self.rut,self.dv,self.id,self.saldo,monto)
            print("\nRETIRO: $" + str(monto))
            print("\nSALDO: $" + str(self.saldo))

    def deposito(self):
        monto = self.ingresarMonto("depositar")
        if monto == -2:
            pass
        elif monto > 0:
            self.saldo += monto
            bc.deposito(self.rut,self.dv,self.id,self.saldo,monto)
            print("\nDEPOSITO: $" + str(monto))
            print("\nSALDO: $" + str(self.saldo))

    def ingresarMonto(self, tipoOperacion):
        while True:
            print("Ingrese el monto a " + tipoOperacion)
            print("Presione (q) para volver al menu anterior")
            monto = input().lower().strip()
            if monto == "q":
                monto = -2
            else:
                try:
                    if float(monto) < 0:
                        print("No se puede ingresar montos negativos")
                        monto = -1
                except:
                    print("Debe ingresar un monto valido")
                    monto = -2
            break
        return float(monto)

    def movimientos(self):
        signo = "$"
        movimientos = bc.movimientos(self.id) #Devolvera varias tuplas dentro de una lista
        if len(movimientos) > 0:
            movimientos.reverse() #Esto para que se muestren los movimientos desde el ultimo hasta el primero
            for i in range(0,len(movimientos)):
                if movimientos[i][1] == "SE REALIZO UN RETIRO": 
                    signo = "-$"                                #Accedo a la tupla [i] y al campo 'informacion' con [1]
                elif movimientos[i][1] == "SE REALIZO UN DEPOSITO":
                    signo = "+$"
                                        #[i][0] = monto         [i][1] = informacion                   [i][2] = fecha
                print(signo + str(movimientos[i][0]) + ". " + movimientos[i][1] + " con fecha: " + str(movimientos[i][2]))
        else:
            print("\nNo hay movimientos para mostrar")
        

		   
                
