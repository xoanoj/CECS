
Comando para container basado en debian:

``` bash
docker run -it --name cripto --cap-add=ALL -v /tmp/.X11-unix:/tmp/.X11-unix --env DISPLAY=$DISPLAY --hostname=cripto debian bash
```

Actualizamos los repositorios de la máquina e instalamos openssl

![[Pasted image 20241209161456.png]]

Creamos el archivo a encriptar:

![[Pasted image 20241209161632.png]]

Y encriptamos el archivo

![[Pasted image 20241209161949.png]]

Ahora para descifrarlo

![[Pasted image 20241209162145.png]]

(La opción que indica la operación de descifrado es -d)

---
### Codificación

Se utiliza como forma alternativa para presentar datos, pero los algoritmos son totalmente reversibles.

Por ejemplo codificando y decodificando la carta en base64:

![[Pasted image 20241209162425.png]]

---
## Criptografía Asimétrica

![[Pasted image 20241209162528.png]]
### Pasos a realizar para Bob:

Generamos un par de claves RSA

![[Pasted image 20241209162712.png]]
(El comando genera una clave RSA de 2048 bits que se encripta utilizando AES-256 y se guarda en el archivo bob_private.pem)

Podemos eliminar la passphrase por comidad usando:

![[Pasted image 20241209162903.png]]

Para extraer la clave pública

![[Pasted image 20241209163111.png]]

### Pasos a realizar para Alice:

Creamos el archivo para enviar a bob:
![[Pasted image 20241209163333.png]]

A continuación habrá que cifrar el archivo con la clave pública de Bob

![[Pasted image 20241209163613.png]]

Ahora Bob recibe y desencripta el mensaje:

![[Pasted image 20241209163733.png]]

---
## Autenticación con criptografía asimétrica

Para añadir la certeza de que la emisora del mensaje es Alice usaremos:
- Un resumen Hash del mensaje
- La clave privada de Alice para cifrar el resumen del mensaje anterior

### Par de claves de Alice:

![[Pasted image 20241209164126.png]]

### Creación de firma digital del mensaje y comprobación de integridad

![[Pasted image 20241209164259.png]]

Al cifrar el hash con la clave privada de Alice tenemos la certeza de que el emisor es Alice ya que es la única que posee esa clave privada y de que el mensaje es íntegro.

---

### Comprobación de autoría e integridad por parte de Bob

Desencriptamos y verificamos el archivo y su autoría

![[Pasted image 20241209164654.png]]

---

![[Pasted image 20241209164729.png]]
