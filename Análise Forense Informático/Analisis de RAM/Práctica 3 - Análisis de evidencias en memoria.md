Práctica de [[Analisis de RAM]]
## Objetivo

>El objetivo de esta práctica es que el alumno se familiarice con el uso de herramientas de análisis forense y sea capaz de crear imágenes de memoria y encontrar información relevante a partir de imágenes de memoria. A mayores, el alumno también se familiarizará con la forma de llevar a cabo y documentar un procedimiento forense.

## Corrección de la práctica y forma de entrega

>No se valorarán las preguntas que no se respondan explícitamente por escrito, es decir, aquellas que consistan únicamente en capturas de pantalla. Es imprescindible que se indique mediante capturas de pantalla cómo se ha obtenido y se razone la respuesta.
>
>Forrma de entrega: vía Moodle. Se habilitará una tarea a tal efecto.

## Materiales:

>Necesitarás la imagen de memoria “Caso1.zip” de una máquina Windows 7 x64 SP1 de la unidad compartida de recursos del módulo para el primer caso (o de Google Drive en https://drive.google.com/file/d/1zoxd5cTCQVA4ab1qB1N3o8n8QpdcIO82) y la imagen de memoria “Caso2.zip” de un Windows 11 para el segundo, también en la unidad compartida de recursos del módulo o en Google Drive en https://drive.google.com/file/d/1fSlf2fsINUtohVl7c-czw9893ICzfkWo. Es posible que necesites usar webs de descifrado de hashes como https://hashes.com/en/decrypt/hash 
>
>Es posible tener que usar herramientas de hacking como zip2john y John the Ripper.

## Ejercicios

### Caso 1:

>Utiliza Volatility 2 para contestar las siguientes preguntas (1 punto por pregunta):

Verifico la integridad:

``` bash
md5sum ~/afi/caso1/caso1Volatility.dmp

8922965d14b8a0ef240b62d460e6146e  
/home/kali/afi/caso1/caso1Volatility.dmp


cat ~/afi/caso1/caso1Volatility.dmp.MD5.txt

8922965d14b8a0ef240b62d460e6146e
```

El perfil apropiado será **Win7SP1x64**

1. ¿Cuál es el nombre del equipo?

Comando:

``` bash
python2 vol.py -f ~/afi/caso1/caso1Volatility.dmp --profile=Win7SP1x64 envars > ~/afi/caso1/envars.txt
```

``` bash
❯ cat ~/afi/caso1/envars.txt | grep NAME
     320 csrss.exe            0x0000000000411320 USERNAME                       SYSTEM
     368 wininit.exe          0x00000000002e9b20 COMPUTERNAME                   W7BASE
     368 wininit.exe          0x00000000002e9b20 USERNAME                       SYSTEM
     376 csrss.exe            0x0000000000141320 USERNAME                       SYSTEM
     404 winlogon.exe         0x000000000039dec0 COMPUTERNAME                   W7BASE
     404 winlogon.exe         0x000000000039dec0 USERNAME                       SYSTEM
     464 services.exe         0x00000000001b1320 COMPUTERNAME                   W7BASE
     464 services.exe         0x00000000001b1320 USERNAME                       SYSTEM
     472 lsass.exe            0x0000000000291320 COMPUTERNAME                   W7BASE
     472 lsass.exe            0x0000000000291320 USERNAME                       SYSTEM
     480 lsm.exe              0x0000000000301320 COMPUTERNAME                   W7BASE
     480 lsm.exe              0x0000000000301320 USERNAME                       SYSTEM
     572 svchost.exe          0x00000000002d1320 COMPUTERNAME                   W7BASE
```

El nombre del equipo es W7BASE

2. El usuario tenía establecida una conexión FTP con un organismo público español. ¿Cuál es?

``` bash
python2 vol.py -f ~/afi/caso1/caso1Volatility.dmp --profile=Win7SP1x64 netscan > ~/afi/caso1/netscan.txt
```

Vemos el segmento:

``` bash
0x5b034ae0         TCPv4    10.0.2.15:49171                130.206.13.2:21      ESTABLISHED      2424     ftp.exe 
```

Mediante Whois vemos que 130.206.13.2 pertenece a la Red Académica y de Investigación Española (RedIRIS)

3. Hay por lo menos un proceso que contiene malware. ¿Cuál es su nombre y su PID? Deberás justificar que está infectado usando comandos de Volatility sobre procesos.

Pruebo a descubrirlo con:

``` bash
python2 vol.py -f ~/afi/caso1/caso1Volatility.dmp --profile=Win7SP1x64 malfind > ~/afi/caso1/malfind.txt
```

Encontramos mencionados muchos procesos extraños:
- explorer.exe PID 896
- haboer.exe PID 1028
- AsustoMucho.ex PID 1004
- notepad.exe PID 2732
- perfmon.exe PID 2216
- cmd.exe PID 2796, 3428 y 2988
- firefox.exe PID 2996 y 2852
- iexplorer.exe PID 2948 y 2464
- pytcw.exe PID 3996

Dumpeo por ejemplo la memoria de explorer.exe y AsustoMucho.ex, despues genero hashes y los valido con VirusTotal

``` bash
python2 vol.py -f ~/afi/caso1/caso1Volatility.dmp --profile=Win7SP1x64 memdump -p 1004 -D ~/afi/caso1

Volatility Foundation Volatility Framework 2.6.1
************************************************************************
Writing AsustoMucho.ex [  1004] to 1004.dmp

shasum -a 1 ~/afi/caso1/1004.dmp

04e7aa2f6e370a9051ed52f022acfc5acd4242d1  /home/kali/afi/caso1/1004.dmp

python2 vol.py -f ~/afi/caso1/caso1Volatility.dmp --profile=Win7SP1x64 memdump -p 896 -D ~/afi/caso1
Volatility Foundation Volatility Framework 2.6.1
************************************************************************
Writing explorer.exe [   896] to 896.dmp
 
shasum -a 1 ~/afi/caso1/896.dmp
61e29f5c2a9b7c7f9989f3f4f678b24d4ce360d9  /home/kali/afi/caso1/896.dmp
```

Ambos aparecen  marcados como maliciosos por dos entidades.

En el primer caso:

![[Pasted image 20250219182556.png]]

En el segundo:

![[Pasted image 20250219182617.png]]

Otro proceso que llama la atención particularmente es pyctw.exe, repetimos el proceso:

``` bash
python2 vol.py -f ~/afi/caso1/caso1Volatility.dmp --profile=Win7SP1x64 memdump -p 3996 -D ~/afi/caso1

Volatility Foundation Volatility Framework 2.6.1
************************************************************************
Writing pytcw.exe [  3996] to 3996.dmp

shasum -a 1 ~/afi/caso1/3996.dmp
5fb7a141841eb0899b97912666fef794a23b38bb  /home/kali/afi/caso1/3996.dmp
```

Este proceso se identifica como algo mucho más concreto:

![[Pasted image 20250219183424.png]]

Se trata de Variant.Zusy: Trojan:win32/Waprox, un troyano que se 
conecta a ciertos servidores para recibir intrucciones C2 del atacante.

Podemos con bastante seguridad concluír que este proceso (pytcw.exe) es malicioso

4. Hay un proceso infectado que tiene establecida una conexión HTTPS. ¿Cuál es la dirección IP a la que está conectado? Deberás justificar que es un proceso infectado.

Vemos el escaneo previamente realizado con netscan y observamos que el proceso malicioso del apartado 3 ha realizado una conexión a 160.153.75.34:443 (Puerto propio de HTTPS).

``` bash
cat ~/afi/caso1/netscan.txt| grep 443

0x36281010         TCPv4    10.0.2.15:49262                216.58.213.3:443     ESTABLISHED      1608     firefox.exe    
0x3aab7010         TCPv4    -:49284                        33.161.122.39:443    ESTABLISHED      1608     firefox.exe    
0x3abc2010         TCPv4    -:49263                        188.165.205.194:443  CLOSED           1608     firefox.exe    
0x464ebcf0         TCPv4    -:49286                        118.45.153.189:443   ESTABLISHED      1608     firefox.exe    
0x62341010         TCPv4    -:49285                        -:443                ESTABLISHED      1608     firefox.exe    
0x7fa7ecf0         TCPv4    10.0.2.15:49325                2.19.61.200:443      ESTABLISHED      2464     iexplore.exe   
0x7fdf0580         TCPv4    10.0.2.15:49326                2.19.61.200:443      ESTABLISHED      2464     iexplore.exe   
0x7fe0f450         TCPv4    10.0.2.15:49525                160.153.75.34:443    ESTABLISHED      3996     pytcw.exe      
```

Justificando que el proceso es malicioso, podemos ver en el apartado 3 que el hash 5fb7a141841eb0899b97912666fef794a23b38bb (generado del volcado de memoria del proceso) es reconocido como Gen:VariantZusy por 2 entidades en VirusTotal.

5. Hay una contraseña de un fichero comprimido escrita en el bloc de notas. ¿Cuál es?

Busco el PID del proceso y vuelco su memoria:

``` bash
❯ python2 vol.py -f ~/afi/caso1/caso1Volatility.dmp --profile=Win7SP1x64 pstree | grep notepad

Volatility Foundation Volatility Framework 2.6.1
. 0xfffffa80022b2b30:notepad.exe                     2732    896      4    291 2020-12-07 18:20:23 UTC+0000
 
python2 vol.py -f ~/afi/caso1/caso1Volatility.dmp --profile=Win7SP1x64 memdump -p 2732 -D ~/afi/caso1
Volatility Foundation Volatility Framework 2.6.1
************************************************************************
Writing notepad.exe [  2732] to 2732.dmp
```

Tras buscar en los strings legibles y no encontrar nada decido extraer solo los string codificado mediante little-endian:

``` bash
strings -e l ~/afi/caso1/2732.dmp > ~/afi/caso1/2732_encoded.txt
```

En la linea 2962 podemos ver:

``` bash
2961   │ la contrase
2962   │ a del zip es abc123..
```

Gracias a:

``` bash
cat ~/afi/caso1/2732_encoded.txt | grep zip
```

6. Existe un fichero ZIP accesible en la memoria RAM. ¿Qué animal se encuentra dentro?

Lo encuentro mediante filescan:

``` bash
python2 vol.py -f ~/afi/caso1/caso1Volatility.dmp --profile=Win7SP1x64 filescan | grep zip

Volatility Foundation Volatility Framework 2.6.1
0x0000000043c1c9a0     13      0 R--r-d \Device\HarddiskVolume2\Program Files\7-Zip\7-zip.dll
0x0000000050223f20     16      0 R--r-d \Device\HarddiskVolume2\Windows\System32\es-ES\zipfldr.dll.mui
0x000000005675bdb0     16      0 R--r-d \Device\HarddiskVolume2\Windows\System32\zipfldr.dll
0x000000007eff3db0     16      0 R--r-d \Device\HarddiskVolume2\Windows\System32\zipfldr.dll
0x000000007f52e070      2      1 R--r-- \Device\HarddiskVolume2\Users\wadmin\Documents\fichero.zip
```

Puedo dumpear el archivo mediante:

``` bash
python2 vol.py -f ~/afi/caso1/caso1Volatility.dmp --profile=Win7SP1x64 dumpfiles -Q 0x000000007f52e070 --name fichero.zip -D ~/afi/caso1/
```

Es un Koala:

![[Pasted image 20250219193933.png]]

### Caso 2

> El hash SHA256 del volcado de memoria de este caso es: 
>
>a1d84fe21f42cd8073b8630c91494992303b84061b493f91ccf28333cecc7040
>
>Utiliza Volatility 3 para contestar las siguientes preguntas (1 punto por pregunta):

1. ¿Cuál es el PID del proceso del Microsoft Paint? ¿Cuál es el nombre de su proceso padre?



2. En el equipo existe un usuario llamado andres, ¿cuál es su contraseña de acceso al equipo?



3. En el Escritorio del usuario usuario existe un fichero de texto con las instrucciones para llevar a cabo unas gamberradas. ¿De qué barrio de Ferrol es el cómplice del organizador?



4. La última versión del plan, que incluye el último paso a realizar, se encuentra en un fichero ZIP cifrado en el Escritorio del usuario. No es posible encontrar la clave de descifrado en la memoria pero, ¿eres capaz de descifrar el contenido y saber cuál será el último de los pasos que piensan dar?


## Pistas:

>En caso de no encontrar la equivalencia entre el plugin en Volatility 2 y 3 en https://blog.onfvp.com/post/volatility-cheatsheet/, puedes probar a usar el mismo nombre de plugin que en Volatility 2 pero añadiéndole windows. al inicio del nombre del plugin en Volatility 3.
>
>Ejemplo:

Volatility 2:

``` bash
vol.py -f “/path/to/file” --profile <profile> pslist
```

Volatility 3:

``` bash
vol.py -f “/path/to/file” windows.pslist
```