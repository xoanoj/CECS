
Práctica de [[Criptografía]]

![[Pasted image 20241209164809.png]]

Lanzamiento del contenedor de la práctica:

``` bash
docker run -it --name firma --cap-add=ALL -v /tmp/.X11-unix:/tmp/.X11-unix -v ~:/host --env DISPLAY=$DISPLAY --hostname=firma debian bash
```

---

![[Pasted image 20241209165415.png]]![[Pasted image 20241209170110.png]]
![[Pasted image 20241209170239.png]]

---
## Generación de clave privada

![[Pasted image 20241209170419.png]]

Creamos la clave privada en RSA y a continuación derivamos la pública:

![[Pasted image 20241209170542.png]]

Creamos el fichero a firmar en la carpeta del usuario del host, que en el contenedor estará en en /host

![[Pasted image 20241209170900.png]]

![[Pasted image 20241209170935.png]]

Generamos la firma de fichero.pdf utilizando SHA256 y la clave privada 

![[Pasted image 20241209171513.png]]

Para efectuar la verificación de la firma

![[Pasted image 20241209171625.png]]

---
## Creacion del certificado auto firmado y Archivo de firma digital

### Creacion de certificado SSL y firma

![[Pasted image 20241209172315.png]]

### Generación de archivo de firma (certificado+clave) en formato pfs

![[Pasted image 20241209173134.png]]

### Firma con autofirma

Configuramos el anfitrión y el contenedor para tener salida gráfica:

![[Pasted image 20241209173437.png]]

![[Pasted image 20241209173502.png]]

El programa se lanza:

![[Pasted image 20241211160955.png]]![[Pasted image 20241211162108.png]]

![[Pasted image 20241211162132.png]]![[Pasted image 20241211162149.png]]