Parte de [[Analisis Forense en Linux]]

Jerarquia de ficheros Linux:

![[Pasted image 20250331205422.png]]
![[Pasted image 20250331205444.png]]
![[Pasted image 20250331205457.png]]

Desde el punto de cista forense, los ficheros mas interesentes son home, root, etc, var/log, tmp y var/tmp.

---

## Timestamps en ficheros en Linux

En sistemas antiguos (EXT3) no hay fecha de creacion de los ficheros, solo de creacion y acceso.

En EXT4, existen crtime y btime. Podemos accceder mediante

``` bash
debugfs -R 'stat <FICHERO>' <RUTA_FS>
```

Por defecto ls -l muestra timestamps de modificacion. Podemos cambiarlo mediante ```touch -t AAAAMMDDhhmm.ss```.

Con el comando debugfs tambien se puede cambiar el fichero de creacion. El comando set_inode_field escribe en el inodo.

Puede ser que estos cambios solo se muestren despues de un reinicio.

Un atacante puede cambiar estos timestamps, si no lo hace podemos buscar ficheros mediante find:

``` bash
find <DIR_COMIENZO> -mtime <-DÍAS>
```

Donde -dias es el numero de dias anteriores al actual.

Con el parametro newer de find tambien podemos buscar ficheros que se hayan modificado despues de otros:

``` bash
find <DIR_COMIENZO> -newer <FICHERO_BASE>
```

Tambien podemos añadirlo -printf podemos imprimir entre otros el path y timestamps:

![[Pasted image 20250331210338.png]]

El comando ls tambien tiene comandos que pueden ayudar como --time=palabra. El -u da el access time, el -c da el change time y la palabra "birth" la de creacion. -t ordena por tiempo, -r al reves y -A es para no incluir ficheros como "." y "..".

Los sistemas Linux suelen utilizar una opcion del sistema de archivos conocida como relatime. Con esta opcion el timestamp de acceso al archivo (atime) se actualiza solo si:

- El atime es mas antiguo que mtime o ctime
- El atime se actualizo por ultima vez hace mas de 24 horas

---

## Informacion basica del sistema

![[Pasted image 20250331210712.png]]
![[Pasted image 20250331210729.png]]


Linux no guarda la fecha/hora de instalacion por defecto, por lo que se debe aproximar por informacion de los logs, la creacion de un sistema de ficheros o la fecha de creacion o modificacion de un fichero que suela existir y no cambiar.

![[Pasted image 20250331210842.png]]

En Debian y etc. existe el syslog:  sudo head /var/log/installer/syslog

En Arch existen los logs pacman que pueden devolver fecha y hora: head /var/log/pacman.log

En Fedora etc. tenemos basesystem: sudo rpm -qi basesystem

En muchos sistemas podemos emplear tune2fs o similar (dumpe2fs)

---
## Zonas horarias

La zona horaria predeterminada del sistema se almacena en el archivo /etc/localtime (el archivo esta en binario). Se puede sacar con el comando zdump (timezone dumper) sobre el fichero.

Los sistemas de archivos de Linux almacenan marcas de tiempo internamente en UTC

Los programas de línea de comandos muestran las horas en la zona horaria predeterminada

---

## Usuarios y grupos:

![[Pasted image 20250331211230.png]]

En cuanto a /etc/shadow:

![[Pasted image 20250331211325.png]]

En /etc/group:

![[Pasted image 20250331211451.png]]

En /etc/sudoers:

![[Pasted image 20250331211509.png]]

---

## Que buscar?

• Cuentas del sistema que tengan un password activado cuando no deberían (cuentas SSH con clave pública/privada)
• Cuentas que tienen un shell asignado cuando deberían tener /sbin/nologin o /bin/false (daemon)
• Usuarios miembros del grupo sudo cuando no deberían
• Privilegios de sudoers que no deberían


