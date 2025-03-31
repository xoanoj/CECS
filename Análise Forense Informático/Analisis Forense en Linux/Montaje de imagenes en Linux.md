Parte de [[Analisis Forense en Linux]]

Para montar imagenes es apropiado tenerlas en .raw, podemos convertir .E01 en .raw mediante libwef

Problemas a la hora del montado pueden ser que tengan volumen logicos, que el apagado brusco deje imagenes sucias, que el disco este cifrado o que haya un RAID

Proceso del montado:

![[Pasted image 20250331203330.png]]

Instalar libewf

``` bash
sudo apt install libewf2 ewf-tools
```

Montaje:

``` bash
sudo su
ewfmount <ARCHIVO_IMAGEN> <DIRECTORIO>
P. ej.: ewfmount imagen.E01 /tmp/disco01
```

Se habrá generado un archivo de sólo lectura llamado ewf1 en el directorio de montaje

Ahora debemos acceder a la imagen, ver el tipo de particion y analizar los sistemas de ficheros:

``` bash
cd /tmp/disco01
file ewf1
fdisk -l ./ewf
mmls ./ewf1
```

Con fdisk -l lo importante es el tamaño del sector. Con mmls es importante la direccion de inicio del sector boot y del sector LVM

Ahora se debe hacer un examen del sistema de ficheros con fsstat que viene con sleughkit.

``` bash
fsstat -o [offset] ./ewf
```

Done el offset es el inicio del sector.

El comando genera un listado muy grande, la parte mas importante (con por ejemplo causas de errores) es al principio del todo.

Un Loop Device es un dispositivo que nos permite acceder a ficheros que esten en bloques (en /dev). El comando losetup nos permite asocias un loop device con un archivo de imagen de disco sin procesar.

Es decir, hay que apuntar el loopdevice al inicio de la particion LVM especificando un offset en bytes.

>Hay que multiplicar el inicio del sector por el numero de sectores

(start\*units)(donde units se consigue mediante fdisk -l y start mediante mmls) (es importante quitar los ceros de la izquierda)

Como en esta subshell:

``` bash
echo$(([units]*[offset_sin_ceros_izquierda]))
```


Luego podremos emplear losetup:

``` bash
losetup -rf -o $(([units]*[offset_sin_ceros_izquierda])) ./ewf1
```

Donde:
- -r monta el dispositivo como solo lectura
- -o indica el offset del dispositivo a montar
- -f busca el primer loop device sin usar
- -a muestra el estado de todos los loop devices del sistema

Habremos enlazado el loop device con la imagen del disco.

Podemos comprobar el sistema montado, empezando con file. Debemos usar file con -s ya que es un archivo por bloques. Tambien podemos usar pvdisplay y vgscan.

``` bash
pvdisplay /dev/loopX
vgscan
```

Donde X es el numero del sistema montado

vgscan da informacion mas resumida.

El siguiente paso sera activar el sistema LVM:

``` bash
lvchange -a -y [nombre_grupo]
```

(No deberia dar output si sale bien)

Ahora podemos comprobarlo con lvscan:

``` bash
lvscan | grep ubuntu-vg
```

Otra comprobacion podria ser mediante fsstat para ver que los modos se montaron correctamente (pero puede dar respuestas falsas con imagenes sucias)

Para facilitar el imagen puede ser buena idea duplicarla con dd o dc3dd para no tener que repetir el proceso.

Para montar las particiones en el directorio emplearemos simplemente mount, aunque con las opciones "ro" y "noexec" para solo lectura y evitar ejecucion de programas.

Si la imagen es sucia el comando mount puede dar errores (podemos leerlos mediante ``` dmesg|tail ```) Esto se puede solucionar con la opcion "noload".

Al final, para desmontaje emplearemos umount y losetup -d o demsetup para cerrar los volumenes.

El proceso seria el inverso al inicial:

![[Pasted image 20250331205250.png]]

