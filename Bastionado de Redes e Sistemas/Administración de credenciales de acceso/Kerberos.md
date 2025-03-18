Parte de [[Bastionado de Redes e Sistemas]], ver también [[P1 - Kerberos]]

Sistema de utilizado para implementar autorización a lo largo de una red

Está diseñado para operar de forma segura, por defecto en entornos de Directorio Activo. Los detalles de su protocolo están estandarizados pero son muy complicados.

La versión mas difundida es la que incorporan por defecto los sistemas de entorno activo por defecto de Windows Server

Se basa en la concesión de tickets, que identifican usuarios y permiten utilizar esa credencial para solicitar a otros servicios de terceros.

Tiene 3 elementos
- Principal (usuario)
- Servicio (AP (Aplication Server)) (al que quiere acceder al usuario)
- KDC (Key Distribution Server)
	- AS (Authentication server)
	- TGS (Ticket Granting server)

El AS otorga un TGT (ticket granting ticket) que nos identifica y nos permite solicitar tickets de acceso al TGS, los cuales en cambio permiten solicitar acceso a servicios de terceros.

No confundir TGS (Parte del KDC) con el TGS (Ticket que da acceso a un servicio (AP))

El cifrado empleado por kerberos es simetrico
Utiliza por defecto los puertos 88/tcp y 88/udp

El intercambio cuenta con 5 fases:

![[Pasted image 20241216161849.png]]
La autenticación utiliza marcas de tiempo para que solo sea aceptable durante una cantidad limitada de tiempo y asi evitar ataques de repetición. Se utiliza el hash NTLM como clave para cifrar el desafio(PERO NO SE ENVIA EL HASH NTLM), ya que este solo lo debe tener el usuario la base de datos del AS. Si se valida se responde con un KRB_AS_REP (que contiene el TGT):

![[Pasted image 20241216162208.png]]

El TGT esta cifrado con una clave privada compartida por el AS y el TGS, con lo que el usuario no lo puede descifrar. A continuación se interactua con el TGS con un KRB_TGS_REQ que lleva adjunto el TGT para certificar que es el usuario el que envia la solicitud:

![[Pasted image 20241216162629.png]]

Si el TGS determina que el usuario tiene permisos para acceder al servicio que se solicita le envia de respuesta un KRB_TGS_REP que incluye u TGS (ticket), que esta cifrado por el TGS y el servicio

![[Pasted image 20241216162744.png]]

Tras esto el usuario puede acceder al servicio:

![[Pasted image 20241216162954.png]]

