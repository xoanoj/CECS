
Práctica de [[Analise Forense]]

## Ejercicio 1

> Utilizando Autopsy
### Enunciado A

> Cree un nuevo caso.

Abro Autopsy (versión 4.19.3) y creo un caso con un nombre distintivo y rellenando cierta información

![[Pasted image 20241216203816.png]]
![[Pasted image 20241216204046.png]]
![[Pasted image 20241216204126.png]]
(Como es una imagen pequeña, utilizo el disco C, en un futuro utilizare el D)
### Enunciado B

>Añada como fuente de datos la siguiente imagen: 
>https://drive.google.com/file/d/15TddpnzY0RnHOJX6ippe7brpaxsXijhA

Descargo la imagen y la descomprimo:

![[Pasted image 20241216204345.png]]

En la creación del caso escojo la opción de utilizar una imagen de disco como fuente de datos:

![[Pasted image 20241216204450.png]]

Y relleno la información acerca de la imagen (configura la zona horaria como UTC de forma defectiva)

![[Pasted image 20241216212254.png]]

A la hora de tener en cuenta que Ingests habilitar escojo únicamente los que me puedan ayudar con los objetivos relacionados con el apartado c.

### Enunciado C

>¿Es capaz de recuperar los archivos eliminados? ¿Y la partición eliminada?¿Que "ingest modules” ha utilizado?

Selecciono la siguiente configuración de Ingest:

![[Pasted image 20241216212327.png]]

Acabamos la configuración:

![[Pasted image 20241216205606.png]]

Una vez dado podemos ver los ficheros eliminados:

![[Pasted image 20241216212553.png]]

Y la partición eliminada:

![[Pasted image 20241216212622.png]]

Los módulos utilizados fueron:

- Recent Activity
- File Type Identification
- Embedded File Extractor
- Keyword Search
- Interesting Files Identifier
- PhotoRec Carver
- Data Source Integrity

## Ejercicio 2

>Descargue la evidencia “image.dd.zip” de la siguiente dirección y verifique su integridad:
>https://drive.google.com/file/d/15TddpnzY0RnHOJX6ippe7brpaxsXijhA
>Utilizando Autopsy, debe realizar los siguientes enunciados.

Para verificar su integridad, creo el caso pasandole el hash SHA1 incluído con la imagen

![[Pasted image 20241216213915.png]]

