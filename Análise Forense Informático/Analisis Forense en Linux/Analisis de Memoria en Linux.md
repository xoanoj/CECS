Parte de [[Analisis Forense en Linux]]

La instalación de volatility (tanto 2.7 como 3) es trivial en el contexto de archivos python para Linux.

Los perfiles empiezan siempre con Linux y despues aparee el nombre de la distro.

La comprobacion del perfil se puede hacer mediante el modulo linux_banner

Los plugins de volatility son iguales que en windows, pero comienzan por "linux_".

---
## Comandos para procesos:

![[Pasted image 20250403194451.png]]

Los comandos del ejecutable de un proceso se hace mediante linux_procdump. Las librerias mediante linux_library_list o linux_librarydump.

---
## Handles

En Linux todo es un archivo, asi que solo existen HANDLES de tipo file.
Los descriptores de ficheros abiertos se obtienen con el plugin linux_lsof.

---
## Variables de Entorno

![[Pasted image 20250403194954.png]]

---
## Comandos de volatility sobre espacios de memoria

El comando linux_memmap saca el mapa de memoria. Con linux_proc_maps podemos ver detalles de la memoria de un proceso (esto nos puede ayudar a detectar malware). Tambien podemos usar linux_dump_map.

---
## Comandos sobre conexiones de red

![[Pasted image 20250403200701.png]]

---
## Comandos de Volatility sobre objetos y memoria del kernel

El plugin linux_lsmod recorre la lista de módulos del kernel cargados en memoria (modules.list)

---
## Sistemas de ficheros tmpfs

Siempre tiene dos pasos:

![[Pasted image 20250403200958.png]]

---
## Comandos para deteccion de rootkits

![[Pasted image 20250403201055.png]]![[Pasted image 20250403201105.png]]![[Pasted image 20250403201113.png]]

---
## Comandos sobre informacion del sistema

linux_cpuinfo para info sobre la CPU. linux_dmesg para ver el buffer de debug del kernel. La memoria de E/S se puede ver con linux_iomem que muestra las direcciones disicas reservadas para dispositivos. Slabindo mediante linux_slabinfo permite lee /proc/slabinfo en un sistema de ejecucion.

Dispositivos monstando con linux_mount y linux_mount_cache. Entradas de directorio con linux_dentry_cache, que recupera el sistema de ficheros de cada punto de montaje y tambien pueden recuperar nombres de archivos de ficheros.

Podemos buscar ficheros mediante linux_find_file.

---
## Miscelanea de comandos

Linux_volshell provee una consola interactiva para cargar funciones de volatility. linux_yarascan busca patrones textuales o binarios, expresiones regulares, cadenas ANSI o unicode etc. en memoria de usuario O DEL KERNEL.

