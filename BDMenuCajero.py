from BDRegistroEInicio import Conexion 
cn = Conexion()

class BDCajero():
    def retiro(self,rut,dv,id,saldo,monto):
        sql = "CALL retiro(%s,%s,%s,%s,%s)"
        cn.cursor.execute(sql,(rut,dv,id,saldo,monto))
        cn.db.commit()
    
    def deposito(self,rut,dv,id,saldo,monto):
        sql = "CALL deposito(%s,%s,%s,%s,%s)"
        cn.cursor.execute(sql,(rut,dv,id,saldo,monto))
        cn.db.commit()

    def movimientos(self,id):
        movimientos = []
        sql = "SELECT monto, informacion, fecha FROM vistaLog WHERE id = %s"
        cn.cursor.execute(sql,(id,))
        for i in cn.cursor:
            movimientos.append(i)
        return movimientos