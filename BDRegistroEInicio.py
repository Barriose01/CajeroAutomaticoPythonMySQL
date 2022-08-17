import mysql.connector
class Conexion:
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="cajeroAutomatico"
        )
        cursor = db.cursor()
    except:
       print("Error al hacer la conexion a la base de datos")

    def cuentaValida(self,rut,dv,clave): #Verifica si los datos ingresados son validos
        cuentaEsValida = True
        dvValidos = []
        for i in range(0,10):
            dvValidos.append(str(i))
        dvValidos.append("k")
        numValidos = []
        for x in range(0,10):
            numValidos.append(str(x))

        if len(dv) < 1 or len(dv) > 1 or len(clave) < 1 or len(clave) > 4 or len(rut) < 1:
            cuentaEsValida = False
        else:
            for num in rut:
                if num not in numValidos:
                    cuentaEsValida = False
            for num in clave:
                if num not in numValidos:
                    cuentaEsValida = False
            for num in dv:
                if num not in dvValidos:
                    cuentaEsValida = False
        return cuentaEsValida
        
    def registrarUsuario(self,rut,dv,clave,nombre,apellido):
       
        sql = "INSERT INTO cuentaUsuario(rut,dv,clave,nombre,apellido) VALUES(%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,(rut,dv,clave,nombre,apellido))
        self.db.commit()
        
        
    def obtenerInfoCuenta(self,rut,dv):
        cuenta = []
        sql = "SELECT * FROM cuentaUsuario WHERE rut = %s AND dv = %s"
        self.cursor.execute(sql,(rut,dv))
        for i in self.cursor:
            cuenta.append(i)
        return cuenta

    def registrarLog(self, rut,dv):
        cuenta = self.obtenerInfoCuenta(rut,dv)
        id = cuenta[0][0]
        sql = "INSERT INTO logCuentaUsuario(idUsuario,informacion) VALUES(%s, %s)"
        self.cursor.execute(sql,(id,"SE CREO UNA NUEVA CUENTA"))
        self.db.commit()
        print("La cuenta ha sido registrada con exito")

    
        
