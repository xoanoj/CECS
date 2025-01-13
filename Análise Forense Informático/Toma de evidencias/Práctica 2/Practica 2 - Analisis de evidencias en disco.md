
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

### Enunciados A y B

> Encontrar los dos ficheros comprimidos y averiguar qué contienen en su interior

![[Pasted image 20250113202540.png]]

Contienen dos carpetas, una con un instalador de TrueCrypt y otra con un archivo protegido bajo contraseña llamado "Your new password is..."

>Para los archivos encontrados en el punto a) que contengan documentos, acceda a su contenido

Tras analizar los documentos de la imagen descubrimos varios audios, uno de ellos tiene contenido y trata de un miembro de soporte TI haciendole a saber a una mujer que le enviara su nueva contraseña en un archivo cifrado y que la contraseña es su numero de telefono.

Podemos encontrar el numero de telefono de la mujer en:

![[Pasted image 20250113202831.png]]

Usamos el número sin guiones para extraer el archivo

![[Pasted image 20250113203001.png]]

Y finalmente vemos el contenido del documento

![[Pasted image 20250113203056.png]]

## Ejercicio 3

> Descargue la evidencia “LoneWolf.E01” a “LoneWolf.E09” dentro del fichero “ImagenPractica2.zip” que puede encontrar en: \\sarela\comun\ciberCEP\AnaliseFI\Practica2\ si se encuentra en el aula, y si se encuentra fuera de la misma en el siguiente enlace de Google Drive:
>
>https://drive.google.com/file/d/1PAtjrQlD1CokPasIK_ow5F7tDEKVeASk

Creo el caso

![[Pasted image 20250113204406.png]]
### Enunciado A

>Averiguar el sistema operativo instalado. Hacerlo en Autopsy y confirmarlo con Windows Registry Recovery
>
>http://pwww.mitec.cz/wrr.html

Segun Autopsy se trata de Windows NT:

![[Pasted image 20250113204832.png]]

Lo confirmo con el archivo SYSTEM y WRR:

![[Pasted image 20250113205448.png]]
### Enunciado B

>Averiguar el usuario o usuarios del sistema.

El unico usuario no defectivo de Windows parece ser jcloudy

![[Pasted image 20250113210557.png]]
### Enunciado C

>Averiguar cuándo fue el último inicio de sesión en el equipo del usuario jcloudy. Hacerlo en Autopsy y confirmarlo con Windows Registry Recovery. Nota: WRR no puede leer directamente de los ficheros de imagen, es necesario extraer con Autopsy los archivos del hive del registro de Windows que se quiera analizar.

Segun Autopsy:

![[Pasted image 20250113210644.png]]

Segun WRR:

![[Pasted image 20250113211049.png]]

Las horas de login no coinciden, probablemente por la diferencia de zonas horarias y como cada aplicacion intenta adaptarlas.
### Enunciado D

>Averiguar la marca y modelo de los pendrives insertados en el equipo, y cuándo se registraron en el sistema (fecha y hora).

Podemos verlo en Autopsy:

![[Pasted image 20250113212040.png]]

### Enunciado E

>Averiguar si el usuario buscó información sobre armas de fuego, su uso, compraventa, etc. Aquí, para no alargar demasiado, basta con una única búsqueda en la web y una única página visitada de prueba, no hace falta encontrar todas.

Esta busqueda muestra el canal de Youtube de Demolition Ranch, que es un canal dedicado a hablar de armas de fuego

![[Pasted image 20250113212244.png]]

Tambien visita GunBroker, una tienda de armas online:

![[Pasted image 20250113212511.png]]

### Enunciado F

>Encontrar todas las ocurrencias del archivo “Planning.docx”. ¿Cuál fue la primera en aparecer en el sistema? ¿Por qué motivo crees que hay varias?

Parece aparecer por primera vez el 2018-'3-30 a las 04:16:48 UTC+0

![[Pasted image 20250113212731.png]]

Seguramente existan varias versiones debido a variaciones en el plan (que asemeja de asesinato) que esta organizando.
### Enunciado G

>Encontrar qué marca y modelo de tarjeta gráfica tiene el equipo en base a los drivers instalados en el sistema. Confirmar que era dicha gráfica con Windows Registry Recovery.

NVIDIA NVS 5200M segun el Hive SYSTEM:

![[Pasted image 20250113214446.png]]
### Enunciado H

>¿Cómo se llama la otra persona que tiene acceso a las cuentas en la nube de jcloudy?

