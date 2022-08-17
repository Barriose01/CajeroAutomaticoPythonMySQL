# CajeroAutomaticoPythonMySQL

ATENCION: Como este programa esta pensado para una instancia local, es necesario crear la base de datos con el script de MySql que esta
incluido en los archivos, y utilizar el servidor Xampp para que funcione. Realizar los cambios necesarios de ser conveniente

Se deben tener todos los archivos en la misma ruta para que funcionen. Se debe ejecutar el archivo 'menuInicioCajero.py' para iniciar
la ejecucion. Al ejecutar el programa, nos aparece el siguiente menu:

![image](https://user-images.githubusercontent.com/107152796/180608214-553fbebc-309e-4614-82c4-58687a19678e.png)

Primero tendremos que registrar una cuenta. Para ello, elegimos la primera opcion.
Nos pedira que introduzcamos nuestros datos, como nuestro nombre, el rut con su dv (Numero de identificacion en Chile), y nuestra clave.
Si la cuenta no se encontraba registrada anteriormente, podremos registrar la cuenta:

![image](https://user-images.githubusercontent.com/107152796/180608312-493945f9-d2e5-449a-bd35-18fb3df19a91.png)

Si intentamos registrar una cuenta utilizando un RUT y DV que ya estaban registrados, no nos dejara registrar la cuenta:

![image](https://user-images.githubusercontent.com/107152796/180608399-4485eef1-7bb7-4908-befb-cf82b852bee2.png)

Una vez registrada la cuenta, podremos iniciar sesion. Nos pedira el rut, el dv y la clave que elegimos. Si los datos son correctos,
nos aparecera un nuevo menu:

![image](https://user-images.githubusercontent.com/107152796/185242591-5adc42dd-3da3-4da3-a4ce-16dc73aa1865.png)


Tendremos distintas opciones. Si queremos ver el saldo, como apenas hemos creado la cuenta, nos aparecera que tenemos saldo $0.0:

![image](https://user-images.githubusercontent.com/107152796/180608484-a55922c9-72f1-49da-8a7a-abb14945bf4f.png)

Debido a esto, si queremos realizar un retiro, independiente de la opcion que elijamos, nos aparecera que no tenemos fondos suficientes:

![image](https://user-images.githubusercontent.com/107152796/180608519-a53201a9-0960-4669-a80a-6c794f46e185.png)

Para tener fondos, es necesario hacer un deposito. Al elegir la opcion del deposito, nos pedira que elijamos el monto que queremos depositar.
Al realizar esto, ya tendremos saldo suficiente para realizar retiros:

![image](https://user-images.githubusercontent.com/107152796/180608582-a3c34aea-529a-4cf8-9033-7e2679d764a1.png)

Realizaremos ahora un deposito de $5000.0. Elegimos la opcion del retiro y, en el nuevo menu que aparece, escogemos la opcion de retirar $5000.0:

![image](https://user-images.githubusercontent.com/107152796/180608610-279d0264-d33d-46ab-9c2f-50349a00c665.png)

Al ver el saldo, nos aparecera lo siguiente:

![image](https://user-images.githubusercontent.com/107152796/180608617-e57ad6cc-d86c-4679-bc8b-643dcd9e5632.png)

Para hacer una transferencia, tenemos que conocer otro rut y dv de otro usuario que tenga una cuenta registrada. Con esto listo, llenamos el programa
con la informacion que nos pide y nos pedira que ingresemos un monto para transferir:

![image](https://user-images.githubusercontent.com/107152796/185243368-47e2cb9e-fd7d-47e5-832e-ed67ffb90e9e.png)


Si queremos ver todos los movimientos que hemos realizado con esta cuenta, elegimos la opcion "Ver Movimientos":

![image](https://user-images.githubusercontent.com/107152796/185243440-6217b33d-dc8f-4f4d-b0af-27a8aacb2f79.png)

Si vemos con atencion, nos mostrara los movimientos mas recientes hasta los mas antiguos. Tambien nos dara informacion tal como la accion que se ejecuto, 
los montos involucrados y la fecha y la hora exacta en la cual se hizo esta accion.

Para comprobar el punto de la transferencia, entraremos a la otra cuenta que ya teniamos creada y veamos los movimientos:

![image](https://user-images.githubusercontent.com/107152796/185243593-919422d5-f13c-4768-9a3e-d7ca1ca568f3.png)

Como se puede ver, nos aparece la informacion de que hemos recibido una transferencia de un usuario que cuenta con ese rut, el cual es el mismo que la cuenta
que creamos como ejemplo




