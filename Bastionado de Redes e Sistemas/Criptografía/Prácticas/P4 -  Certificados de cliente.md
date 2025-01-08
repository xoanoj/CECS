Práctica de [[Criptografía]]

![[Pasted image 20241211171633.png]]

Inicio el escenario con make i me conecto al contenedor nginx instanciando una terminal de bash con docker exec -it para configurar nginx:

![[Pasted image 20241211172450.png]]![[Pasted image 20241211172719.png]]

## Generacion de certificados para trabajar con https

>Vamos a configurar el acceso https, es decir, autenticación del servidor mediante certificado SSL. Esta configuración permitirá autenticar el servidor al cliente, de modo que mediante la validación del certificado, que en este caso será autofirmado, y por tanto no validable por CA, el servidor podrá autenticar su identidad al cliente y éste determinará si confía, o no, en él.

Creamos la clave privada de la CA

![[Pasted image 20241211173231.png]]Creamos el certificado

![[Pasted image 20241211173332.png]]

Ahora generaremos la clave y el certificado del servidor redmine:

