Parte de [[Bastionado de Redes e Sistemas]] y [[Criptografía]]

### Criptografía simétrica:

También llamado "de clave privada".

Basa su fortaleza en el uso de una clave de cifrado/descifrado solamente conocida por el emisor y el receptor del mensaje.

Los algoritmos son conocidos y consisten en iteraciones sucesivas de operaciones matemáticas como sustituciones y trasposiciones.

La fortaleza recae en la protección de la clave.

(Cifrado de bloques, DES, Triple DES, AES)(modos de operación ECB y CBC)

### Criptografía Asimétrica:

También llamada criptografía de clave "pública/privada". 

Conceptos clave:
- Una clave pública que puede ser difundida
- Una clave privada que debe de ser protegida y mantenida en secreto
- No es posible derivar o deducir una clave de la otra
- La fortaleza del sistema depende de la longitud de las claves

Forma de interacción:
- Tpdo mensaje cifrado con la clave pública es descifrado solamente con la clave privada
- Todo mensaje cifrado con la clave privada es descifrado solamente con la clave pública

Aspectos negativos:
- Los procesos de cifrado y descifrado se basan en principios matematicos de gran complejidad y demandantes de tiempo de computo
- La gestión del par de claves puede dificultar su uso por parte de usuarios inexpertos
- Hay una cierta probabilidad de confusión de la claves cuando una de estas se difunde de modo que sin querer podemos filtrar la clave privada

![[Pasted image 20241202171226.png]]

![[Pasted image 20241202171349.png]]

