
Práctica de [[Criptografía]]

![[Pasted image 20241211164828.png]]

Contenedor para la práctica:

``` bash
docker run -it --name certificados --cap-add=ALL -v /tmp/.X11-unix:/tmp/.X11-unix --env DISPLAY=$DISPLAY --hostname=certificados debian bash
```

Creamos la clave privada CA.key:

![[Pasted image 20241211165245.png]]

Creamos el certificado raíz de la CA:

![[Pasted image 20241211165452.png]]

Podemos ver los detalles del certificado:

![[Pasted image 20241211165534.png]]

Incorporamos la CA al navegador, primero configuramos el sistema y lanzamos Chromium:

![[Pasted image 20241211165657.png]]

Importo el CA dandole permiso de identificar sitios web

![[Pasted image 20241211165754.png]]

---

![[Pasted image 20241211165825.png]]

> Supongamos que queremos emitir un **certificado** **digital** para un sitio web www.bastionado.isc
 
Creamos en primer lugar la clave RSA:


![[Pasted image 20241211170117.png]]

>Supongamos que queremos emitir un **certificado** **digital** para un sitio web www.bastionado.isc, de nuestra organización, para ello **creamos una CSR** que posteriormente será firmada por la CA:

Creacion de un CSR:

![[Pasted image 20241211170420.png]]

- Utiliza como clave para el certificado la clave creada en el punto anterior **www.bastionado.isc.key**
- Emite una **solicitud CSR** con los datos para el certificado y obtiene el archivo **www.bastionado.isc.csr

>Es muy importante que el **FQDN** del certificado, **www.bastionado.isc**, coincida exactamente con el **FQDN del servicio** que va a hacer uso del mismo, en este caso la URL del sitio sería: **https://www.bastionado.isc**

### Envío de la CSR a la CA para la firma y creación de la versión final del certificado

>Por último hacemos uso de los archivos de la **CA para** **firmar** **la CSR y emitir el certificado digital** del servicio solicitado:

![[Pasted image 20241211170619.png]]
- Se usan los archivos de la CA para firmar el CSR
	- La clave CA.key para la firma digital
	- El certificado CA-pem para identificacion de la CA
	- El parametro CAcreateserial crea un archivo CA.srl con el numero de serie para el certificado de manera que evite que este se repita en sucesivos certificados digitales, para ello pararemos el parametro CAserial haciendo referencia al archivo anterior.
	- El propio archivo de con la CSR y los dtaos del certificado final
	- Se emite para un período máximo de un año
	- El resumes HASH está en SHA256

Podemos comprobar el certificado:

![[Pasted image 20241211170914.png]]

Así sabemos que el certificado fue emitido por esa CA (aquí es trivial, pero esto es útil cuando se trata de CAs públicas)

### Conversión de formatos

>En ocasiones resulta útil disponer de los certificados, y sus artefactos asociados como claves privadas y certificados intermedios, en distintos formatos según el uso. Podemos utilizar openssl para realizar conversiones entre los formatos más utilizados.
>
>El certificado en el apartado anterior está en formato **PEM**, vamos a convertirlo a otros formatos.

#### PEM a PKCS#12

![[Pasted image 20241211171127.png]]

#### PEM a DER

Certificado de pem a der

![[Pasted image 20241211171153.png]]

Clave a der

![[Pasted image 20241211171253.png]]


### Inspeccion de certificados

Comprobando un certificado público

![[Pasted image 20241211171357.png]]

El comando **openssl** **s_client** nos permite establecer conexiones TLS/SSL utilizando la propia utilidad como cliente, la opción connect especifica el host y el puerto al cual nos conectamos, la respuesta es la recepción del certificado asociado a la URL indicada.

La segunda parte del comando, después de la canalización, utiliza el comando openssl x509 para mostrar la información correspondiente a las fechas asociadas al certificado (fecha de expedición y expiración).

Otras opciones:

![[Pasted image 20241211171434.png]]

Podemos ver todas las opciones con

``` bash
openssl x509 --help
```

![[Pasted image 20241211171520.png]]

