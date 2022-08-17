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
            print("(4): Hacer transferencia")
            print("(5): Ver movimientos")
            print("(6): Salir")
            opcion = input().lower().strip()

            if opcion == "6":
                break
            elif opcion == "1":
                print("\nSu saldo es de: $" + str(self.saldo))
            elif opcion == "2":
                self.hacerRetiro()
            elif opcion == "3":
                self.deposito()
            elif opcion == "4":
                self.transferencia()
            elif opcion == "5":
                self.movimientos()
            else:
                print("\nIngrese una opcion valida")

    def obtenerSaldo(self):
        self.saldo = 0
        try:
            cuenta = cn.obtenerInfoCuenta(self.rut,self.dv)
            self.saldo = cuenta[0][6] #Con [0] ingreso a la tupla. Con [6] ingreso al campo 'saldo'
        except:
            print("\nError al obtener el saldo")
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
            try:
                bc.retiro(self.rut,self.dv,self.id,self.saldo,monto)
                print("\nRETIRO: $" + str(monto))
                print("SALDO: $" + str(self.saldo))
            except:
                print("\nError al realizar el retiro")

    def deposito(self):
        monto = self.ingresarMonto("depositar")
        if monto == -2:
            pass
        elif monto > 0:
            self.saldo += monto
            try:
                bc.deposito(self.rut,self.dv,self.id,self.saldo,monto)
                print("\nDEPOSITO: $" + str(monto))
                print("SALDO: $" + str(self.saldo))
            except:
                print("\nError al realizar el deposito")

    def transferencia(self):
        while True:
            print("Presione (q) para volver al menu principal")
            rutTransferencia = input("Ingrese el rut de la persona a transferir (Sin puntos, guion ni dv): ").lower().strip()
            if rutTransferencia == "q":
                break
            dvTransferencia = input("Ingrese el dv de la persona a transferir: ").lower().strip()
            if dvTransferencia == "q":
                break
            if rutTransferencia == self.rut and dvTransferencia == self.dv:
                print("\nNo es posible hacerte una transferencia a ti mismo")
            else:
                cuentaValida = cn.cuentaValida(rutTransferencia,dvTransferencia, "1111") #Hice hardcode con la clave. No se va a hacer nada con esto.
                                                                                        #esto es solo para que funcione el metodo
                if cuentaValida == True:
                    cuenta = cn.obtenerInfoCuenta(rutTransferencia,dvTransferencia)
                    if len(cuenta) > 0:
                        saldoTransferencia = cuenta[0][6] #Con [0] ingreso a la tupla. Con [6] ingreso al campo 'saldo'
                        idTransferencia = cuenta[0][0] #Con el segundo [0] accedo al id
                        monto = self.ingresarMonto("transferir")
                        if monto == -1 or monto == -2:
                            break
                        else:
                            if monto > self.saldo:
                                print("\nNo tienes saldo suficiente para realizar esta operacion")
                            else:
                                self.saldo -= monto
                                saldoTransferencia += monto
                                try:
                                    bc.transferencia(self.rut,self.dv,self.id,self.saldo,rutTransferencia,dvTransferencia,idTransferencia,saldoTransferencia,monto)
                                    print("\nLa transferencia se ha realizado con exito")
                                    print("\nMONTO: $" + str(monto))
                                    print("SALDO: $" + str(self.saldo))
                                except:
                                    print("\nError al realizar la transferencia")
                            pass
                    else:
                        print("\nEl usuario ingresado no esta registrado")
                else:
                    print("\nLos datos ingresados no son validos")
            break

    def ingresarMonto(self, tipoOperacion):
        while True:
            print("\nIngrese el monto a " + tipoOperacion)
            print("Presione (q) para volver al menu anterior")
            monto = input().lower().strip()
            if monto == "q":
                monto = -2
            else:
                try:
                    if float(monto) <= 0:
                        print("No se puede ingresar montos negativos o cero (0)")
                        monto = -1
                except:
                    print("Debe ingresar un monto valido")
                    monto = -2
            break
        return float(monto)

    def movimientos(self):
        signo = "$"
        try:
            movimientos = bc.movimientos(self.id) #Devolvera varias tuplas dentro de una lista
            if len(movimientos) > 0:
                movimientos.reverse() #Esto para que se muestren los movimientos desde el ultimo hasta el primero
                for i in range(0,len(movimientos)):
                    if movimientos[i][1] == "SE REALIZO UN RETIRO" or  "SE REALIZO UNA TRANSFERENCIA" in movimientos[i][1]: 
                        signo = "-$"                                #Accedo a la tupla [i] y al campo 'informacion' con [1]
                    elif movimientos[i][1] == "SE REALIZO UN DEPOSITO" or "RECIBIO UNA TRANSFERENCIA" in movimientos[i][1]:
                        signo = "+$"
                                            #[i][0] = monto         [i][1] = informacion                   [i][2] = fecha
                    print(signo + str(movimientos[i][0]) + ". " + movimientos[i][1] + " con fecha: " + str(movimientos[i][2]))
            else:
                print("\nNo hay movimientos para mostrar")
        except:
            print("\nError al mostrar los movimientos")
        

		   
                
