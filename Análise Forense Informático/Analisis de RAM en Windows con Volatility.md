Parte de [[Analise Forense]]

Un buen analisis de RAM ofrece informacion sobre:
- Procesos en ejecucion (exes, DLL cargadas, ficheros abiertos...)
- Conexiones de red activas
- Contraseñas del sistema
- Direcciones web, correos, otras contraseñas
- Elementos ocultos, malware, rootkits

La herramienta por defecto es Volatily
- Es de codigo abierto hecha en Python
- Es compatible con Linux, Windows y Mac OS X
- Extensible mediante plugins
- Admite muchos tipos de volcado de memoria
- Ahora mismo estamos en un periodo de transicion entre la version 2 y la 3.
- Volatility2 permite el analisis hasta W10 y Server2016
- Volatility3 no necesita especificar el perfil de memoria de la captura (Volatility2 si)
- Volatility 2 ofrece mas plugins y una mayor funcionalidad que Volatility 3

Para instalacion y solucion de errores de plugins ver el pptx

- Hay dos comandos de ayuda help y info
- Existe una pagina de comprobacionde plugins equivalentes entre vol2 y vol3


- Volatility por defecto incorpora muchos perfiles de Windos y algunos de Linux
- Se pueden importar mas
- Si no sabemos que perfil usar, hay dos plugins de vol2 que nos pueden ayudar: imageinfo y kdbgscan:

``` bash
python2.7 vol.py -f <fichero_imagen> imageinfo
python2.7 vol.py -f <fichero_imagen> kdbgscan
```

- El mas fiable es imageinfo, da los perfiles por orden de probabilidad de que sea la respuesta correcta

- kpcrscan muestra estructuras kpcr
	- Threads actuales, ociosos y proximos
	- Numero de CPU, vendedor, velocidad

``` bash
python2.7 vol.py -f <fichero_imagen> kpcrscan
```

---

En cuanto a comandos sobre procesos:
- Existen muchos plugins para procesos:
![[Pasted image 20250213203713.png]]

``` bash
python2.7 vol.py -f imagen --profile=perfil pslist
python2.7 vol.py -f imagen --profile=perfil pstree
python2.7 vol.py -f imagen --profile=perfil psxview
python2.7 vol.py -f imagen --profile=perfil psscan
python2.7 vol.py -f imagen --profile=perfil cmdline
python2.7 vol.py -f imagen --profile=perfil cmdscan
python2.7 vol.py -f imagen --profile=perfil consoles
```

---

Tambien podemos coger procesos individuales, volcarlos y analizarlos:
- El plugin procdump sirve para descargar el ejecutable de un proceso:

``` bash
python2.7 vol.py -f imagen --profile=perfil
procdump -p PID -D directorio
```

- Podemos usar la opcion --unsafe para deshabilitar comprobaciones de seguridad (por ejemplo evitar que salte el antivirus si dumpeamos un malware)

---

Tambien podemos listar las librerias dinamicas que estan ejecutando uno o varios procesos. Con dlldump tenemos opciones:
- Todas las DLL de todos los procesos
- Las DLL de todos los procesos
	- Con -p PID o --pid=PID
- Las DLL de un proceso oculto o desenlazado
	- Con --offset=OFFSET
- Bajar DLL que hagan match con regex
	- Con --regex=REGEX
	- Es sensible a mayusculas (--ignore-case)

``` bash
python2.7 vol.py -f imagen --profile=perfil dlldump -p
PID -D directorio
```

---

Los handes son objetos ejecutivos asegurables, como:
- Ficheros
- Claves del registro
- Mutexes
- Tuberias con nombre
- Eventos
- Estaciones Windows
- Escritorios
- Hilos

``` bash
python2.7 vol.py -f imagen --profile=perfil
handles
```

- Se pueden limitar por:
	- PID de proceso con -p PID o --pid=PID
	- Offset fisico con el parametro --physical-offset=OFFSET
- Se puede filtrar por tipo de objeto con -t TIPO o --object-type=TIPO

---

Tambien podemos obtener SIDs con:

``` bash
python2.7 vol.py -f imagen --profile=perfil getsids
```

- Para un proceso con -p PID o de la forma --pid=PID

---

En privilegios:
- El plugin privs obtiene qué privilegios del usuario están presentes, habilitados, y/o habilitados por defecto para un proceso determinado
	- Para un proceso con -p PID o de la forma --pid=PID
	- El flag --silent muestra sólo los privilegios habilitados explícitamente por el proceso
		- No estaban habilitados por defecto pero ahora sí
	- El parámetro --regex=REGEX se puede usar para filtrar por nombres de privilegio específicos

``` bash
python2.7 vol.py -f imagen --profile=perfil privs
```

---

Tambien podemos obtener las variables de entorno con kpcrscan o envars:

- Nº de CPU instaladas y arquitectur hardware
- Directorio actual
- Directorio temporal
- Nombre de la sesion
- Nombre de equipo
- Nombre de usuario

``` bash
python2.7 vol.py -f imagen --profile=perfil envars
Para un proceso con -p PID o de la forma --pid=PID
```

(Es mas fiable kpcrscan)

---

Podemos ver informacion de version con verinfo:
- Versiones de ejecutables y DLL
- Incluye tambien modulos del kernel
- No todos tienen informacion de version
- Los autores de malware pueden falsificarla
- Aun asi sirve para identificar binarios y establcer su relacion con otros ficheros
- La opcion --regex=REGEX sirve para filtrar
- Con --ignore-case es insensible a mayusculas

``` bash
python2.7 vol.py -f imagen --profile=perfil verinfo
```

---

## Comandos de Volatility sobre espacios de memoria

Podemos volcar la memoria de un proceso con memdump:

![[Pasted image 20250213205740.png]]

---

En el mapeado de memoria de un proceso podemos utilizar memmap:
- El dumpfileoffset indica el offset de dicha direccion en un fichero generado por memdump

``` bash
 python2.7 vol.py -f imagen --profile=perfil
memmap
```

---

Podemos sacar el historial de internet explorer:

``` bash
python2.7 vol.py -f imagen --profile=perfil
iehistory
```

---

## Comandos de Volatility sobre conexiones de red

- Existen varios plugins para explorar las conexiones de red
- Windows Vista y 2008 en adelante:
	- netscan: detecta listeners y endpoints TCP y UDP
- Solamente para Windows XP y 2003:
	- connections: muestra las conexiones TCP activas
	- connscan: conexiones activas y terminadas
	- sockets: detectar sockets TCP, UDP, RAW, etc.
	- sockscan: detectar sockets TCP,UDP, RAW, etc.


---

## Comandos de Volatility sobbre objetos y memoria del kernel

- El plugin modules lista los drivers del kernel cargados en el sistema
	- Recorre la lista LDR_DATA_TABLE_ENTRY, por ello:
		- Mismo orden en el que se cargaron en el sistema
		- No encuentra módulos ocultos o desenlazados
	- La opcion -P muestra direccions fisicas en lugar de virtuales

``` bash
python2.7 vol.py -f imagen --profile=perfil modules
```

En cuanto a drivers del kernel ocultos podemos usar modscan

``` bash
python2.7 vol.py -f imagen --profile=perfil modscan
```

![[Pasted image 20250213210715.png]]

---

Podemos buscar fiheros abiertos con filescan, que buscan objetos FILE_OBJECT
- Encuenta archivos abiertos incluso si un rootkit los oculta en disco y oculta los handles.

``` bash
python2.7 vol.py -f imagen --profile=perfil filescan
```

---

Podemos buscar threads mediante ETHREAD escaneando tags del pool
- Es una forma de buscar procesos ocultos, ya que llevan un campo que identifica al proceso padre
- La opcion -s o --silent hace que solo saqe los que tienen nombre

``` bash
python2.7 vol.py -f imagen --profile=perfil thrdscan
```

---

Podemos extraer ficheros cacheados con el plugin dumpfiles
- Pondra .dat, .img, .vacb en el nombre
- Como pueden no estar enteros, las partes no disponibles se llenan a 0s
- Tiene muchas opciones:
![[Pasted image 20250213211015.png]]
![[Pasted image 20250213211030.png]]

---

## Comandos de volatility sobre el registro de Windows

![[Pasted image 20250213211059.png]]

Tambien podemos utilizar printkey para tomar la direccion virtual de un hive y un nombre de clave y muestra su valor, su timestamp y sus subclaves.

Tambien podemos utilizar hashdump para obtener hashes LanMan y NT del registro e lsadump para obtener los secretos LSA (credenciales de usuarios del dominio que hayan usado ese equipo para loggearse). Cachedump obtienen hashes de passwords de dominio que se hayan hasheado en el registro (solo funciona si la memoria viene de una maquina que es parte de un dominio)

>Uso común: Obtener dirección física con hivescan -> dirección virtual con hivelist -> imprimir con printkey, hashdump, lsadump, cachedump

Las shellbags tienen preferencias de visualizacion y de que ejecutables a utilizado en el pasado

El plugin dumpregistry hace el volcado de un
hive del registro al disco
- Por defecto obtiene todos los ficheros de registro, incluidos los virtuales como HARDWARE
- Se puede especificar un offset virtual con -o
- Ciertas partes del registro pueden no estar en memoria, las rellenará con nulos

---

## Comandos de Volatility sobre el sistema de ficheros

El plugin mbrparser escanea y parsea posibles Master Boot Records (MBR), y saca info de las particiones

El plugin mftparser busca posibles entradas Master File Table (MFT) e imprime ciertos atributos informativos
- Opciones:
	- --machine da el nombre de la máquina para añadir a la cabecera timeline
	- -D/--dump-dir especifica el directorio donde se volcarán los ficheros residentes
	- --output=body -> salida en formato Sleuthkit 3.X body
	- --no-check muestra entradas con timestamps nulos
	- -E/--entry-size cambia el tamaño de entrada MFT por defecto (1024 bytes)
	- -o/--offset imprime las entradas de los offset especificados, delimitados por comas

---

## Miscelánea de comandos de Volatility para el core de Windows

El plugin strings saca procesos y direcciones virtuales
que contienen una cadena
- Recibe un fichero con formato
	- ``` <decimal_offset>:<string> o <decimal_offset> <string> ```
	- P. ej. la salida de Strings de Sysinternals
	- P. ej. EnCase Keyword Export (UTF-16 with a BOM, que hay que convertir a ANSI o UTF-8 con iconv o similar)
	- No puede haber líneas en blanco
- Puede buscar en ficheros ocultos con -S

``` bash
python2.7 vol.py -f imagen --profile=perfil strings -s
fichero_cadenas -output-file fichero_salida
```

El plugin volshell provee una consola interactiva
para emplear las funciones internas de Volatility

- Listar procesos, cambiar al contexto de un proceso, mostrar tipos de estructuras/objetos, superponer un tipo sobre una dirección dada, desensamblar código en una cierta dirección de memoria, recorrer listas…
- Si IPython está activado, añadirá completado con tabulador y guardará el historial de comandos

El plugin bioskbd sirve para leer pulsaciones de teclado desde el área de la BIOS
- Puede revelar passwords en BIOS HP, Intel, Lenovo, y programas como SafeBoot, TrueCrypt, BitLocker, etc.
- No todas las herramientas de adquisición contienen memoria del área de la BIOS

El plugin timeliner crea una línea temporal a partir de varios artefactos en memoria
- Usa como fuentes gran parte de los plugins vistos
- Se pueden configurar con --type
- Para añadir un nombre de máquina, --machine
- Para elegir el formato de salida se usa --output
	- Por ejemplo: --output=xlsx, --output=body, etc.
- Para elegir el fichero de salida --output-file=FICHERO
- También se puede limitar el foco de timestamps de registro configurando lo que se quiere obtener
	- --hive=SYSTEM
	- --user=Jim
	- --hive=UserClass.dat --user=Jim

El plugin clipboard recupera datos usuario del
portapapeles, así como su formato y handle

El plugin malfind: ayuda a buscar código o DLL ocultas o inyectadas usando los tags de VAD, permisos de páginas, etc.
- No detecta DLL inyectadas con CreateRemoteThread->LoadLibrary porque no están ocultas (se encuentran con dlllist)
- Se pueden extraer copias de los segmentos identificados a través de --dump-dir=DIRECTORIO