Práctica de [[Analise Forense]]
## Creación de la máquina virtual de trabajo

![[Pasted image 20241121210951.png]]

Configuro el adaptador de VMWare para poder conectar USBs directamente a la máquina virtual

![[Pasted image 20241121212631.png]]

Despues creo la evidencia, creando varios archivos con información como IPs, usuarios del dispositivo, imágenes, PDFs y registros de peticiones HTTP del comando curl.

--- 

### Clonación de un pendrive haciendo uso de la máquina virtual SIFT Workstation

#### Enunciado 1.
 
> Enchufe el segundo (no el de la evidencia) dispositivo USB (el de más de 5GB libres) y compruebe si la máquina lo monta automáticamente. En Linux, algunos comandos como dmesg y sudo fdisk -l detectan si el pendrive está enchufado (detectado), mientras que otros como mount, df, etc, detectan si el pendrive está montado.

Tras crear un filtro en la configuración de USBs de VBox logro que el disco se conecte automáticamente a la máquina virtual.

Podemos ver el pendrive montado con:

```bash 
sudo fdisk -l 
```

![[Pasted image 20241125203815.png]](donde el pendrive es /dev/sbd y /dev/sdb1)

Con 

``` bash
mount | grep /dev/sdb
```

Vemos que el disco se ha montado automáticamente

![[Pasted image 20241125204032.png]]

#### Enunciado 2

>Pruebe si los siguientes mecanismos logran que, al enchufar el pendrive, éste se detecte pero no se monte. Compruébelo también con el explorador de archivos gráfico de SIFT. No se olvide de deshacer los cambios tras probar cada uno de los métodos.

##### Enunciado 2/a

>Establecer la configuración del entorno de ventanas llamada media-handling automount al valor false. El problema es que el nombre completo de dicha configuración puede cambiar dependiendo del tipo de escritorio que tengamos. Así, puede ser org.gnome.desktop.media-handling automount, o bien org.mate.desktop.media-handling automount, etc. dependiendo de si estamos usando Gnome, Mate, etc. Para saber cuál es la nuestra, debemos emplear el comando gsettings get y ver si la variable devuelve un valor (true o false) porque existe o si da error porque no existe. Por ejemplo, para probar con la de gnome haríamos:
>
>gsettings get org.gnome.desktop.media-handling automount
> 
  Y una vez que sepamos cuál es la buena, la establecemos a false con gsettings set. Por ejemplo: 
>
>gsettings set org.gnome.desktop.media-handling automount false

Comprobamos la configuración por primera vez:

![[Pasted image 20241125204710.png]]

Esto quiere decir que automount está activado por defecto, probemos a intentar desactivarlo con:

``` bash
gsettings set org.gnome.desktop.media-handling automount false
```

![[Pasted image 20241125204836.png]]

Al usar el get del estado de nuevo vemos que está en false, lo cual quiere decir que el pendrive no se montara de forma automática.

Se puede comprobar reiniciando la máquina:

![[Pasted image 20241125205647.png]]
Vemos que el disco está detectado y que no se monta automáticamente, al comprobar mediante la IU vemos que aparece el mensaje "Mount & Open".

Dado que hemos logrado desactivar el montado por defecto podemos obviar los apartado B y C.

#### Enunciado 3

>Una vez que esté seguro de que la máquina no montará el dispositivo de forma automática, conecte el pendrive evidencia y consulte su referencia (serial number) con dmesg

Comprobamos el número de serie del pendrive de evidencia con:

```bash
dmesg | grep -i usb
```

Que tiene salida:

![[Pasted image 20241125210604.png]]

#### Enunciado 4

> Haciendo uso de la herramienta dc3dd, realice la clonación del pendrive a una imagen denominada pen_drive_1.dd, indicando a la herramienta que guarde un log y que sea verbosa (verb=on). Si puede, configure dicho comando para que calcule el hash sha256 y sha512. Si no, calcúlelo con otros comandos

Utilizare el siguiente comando de dc3dd:

``` bash
sudo dc3dd if=/dev/sdb1 of=pen_drive_1.dd hash=sha256 hash=sha512 log=pen_drive_1.log verb=on
```

Ejecuto el comando:

![[Pasted image 20241125212444.png]]
(donde /Misc/Forense es un disco duro externo de 100 Gb)

Al finalizar obtenemos los dos hashes:

![[Pasted image 20241125212902.png]]
Con lo cual tenemos una copia completa del pendrive y dos hashes para justificar su integridad como evidencia.

#### Enunciado 5

>Haciendo uso de la herramienta dd, realice la clonación del pendrive a una imagen denominada pen_drive_2.dd. No se olvide de habilitar las opciones para que la clonación continúe en caso de error y activar la opción status=progress para ver cómo va la clonación en todo momento. Si puede, configure dicho comando para que calcule el hash sha256 y sha512. Si no, calcúlelo con otros comandos (no herramientas gráficas). Guarde las imágenes obtenidas fuera de la máquina virtual para usar en posteriores prácticas.

La herramienta dd no permite calcular los hashes de forma automática, con lo cual usaremos las herramientas sha256sum y sha512sum del sistema operativo para calcular los hashes.

El comando de dd será:

``` bash
sudo dd if=/dev/sdc1 of=pen_drive_2.dd bs=64K conv=noerror,sync status=progress
```

Y depués:

``` bash
sha256sum pen_drive_2.dd | tee checksum_sha256.txt
sha512sum pen_drive_2.dd | tee checksum_sha512.txt
```

O de una forma más comoda

``` bash
sha256sum pen_drive_2.dd | tee checksum_sha256.txt && sha512sum pen_drive_2.dd | tee checksum_sha512.txt
```

Imagen de la clonación realizandose:

![[Pasted image 20241128193650.png]]

Al finalizar el cálculo de hashes:

![[Pasted image 20241128194130.png]]

Podemos ver que son diferentes a los realizados con dc3dd, esto se debe a que al conectar el pendrive evidencia al equipo este se monto de manera automática al sistema debian12 anfitrión por un fallo en la configuración del filtro de passthrough the USBs de VirtualBox:

![[Pasted image 20241128194332.png]]

El fallo seguramente se deba a que cree el filtro para el puerto 0007 y el día de la clonación con dd el puerto aparecia como 0005

---
### Clonación de un pendrive haciendo uso de una máquina virtual con Windows 10 Professional

#### Explicación de problema con el paso de USB

Al conectar un pendrive (no el de la evidencia) a la máquina de Windows me doy cuenta de que anteriormente se monta en el anfitrión Debian12 aunque tenga un filtro de USB que debería pasar todas las conexiones, para tratar de evitar este montaje (que cambiaria metadatos y el hash en consecuencia) voy a copiar los filtros de la máquina de Debian, aunque quizás fallen como ya sospecho que hicieron en el ejercicio anterior.

![[Pasted image 20241128201453.png]]

Y copio también este filtro de USB para hacer pruebas sin comprometer la evidencia:

![[Pasted image 20241128201616.png]]

Tras hacer pruebas he logrado automontar los pendrives en Windows copiando los filtros de la máquina SIFT, aunque en este proceso el USB de evidencia se automontó en Windows con lo cual es posible que los metadatos se vieran comprometidos.

En resumen el fallo se debe a haber utilizado puertos distintos del dispositivo sin darme cuenta.

#### Enunciado 1

> Enchufe el segundo (no el de la evidencia) dispositivo USB y compruebe si la máquina lo monta automáticamente. En este caso, para saber si el pendrive se automonta basta con ver que Windows saca el popup que pregunta qué hacer con él, le asigna una unidad como F: y permite trabajar con ella

![[Pasted image 20241128205231.png]]

Si, lo hace.

#### Enunciado 2

> Pruebe si los siguientes mecanismos logran que, al enchufar el pendrive, éste se detecte pero no se monte. No se olvide de deshacer los cambios tras probar cada uno de los métodos.

##### Enunciado 2/a

> Mediante el comando automount disable de la herramienta diskpart.

![[Pasted image 20241128205637.png]]

Probamos a desconectar y volver a conectar el dispositivo y se sigue montando.

Deshago los pasos con 

``` powershell
automount enable
```

##### Enunciado 2/b

>A través del comando mountvol /N

![[Pasted image 20241128210128.png]]

Al reconectar el dispositivo tambien se monta automáticamente, deshago con:

``` powershell
mountvol /E
```

##### Enunciado 2/c

> A través de la clave de registro HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MountMgr\NoAutoMount

![[Pasted image 20241128210800.png]]

Al reconectar el disco se sigue automontando con lo que deshago los cambios y paso a la siguiente técnica.

##### Enunciado 2/d

> A través de las directivas de grupo local (gpedit.msc), yendo a Configuración del Equipo Plantillas Administrativas – Sistema – Acceso de almacenamiento extraíble, y estableciendo a “Habilitada” las tres propiedades de discos extraíbles. A saber:
	▪ Discos extraíbles: denegar acceso de ejecución.
	▪ Discos extraíbles: denegar acceso de lectura.
	▪ Discos extraíbles: denegar acceso de escritura.

Habilito estas 3 opciones:

![[Pasted image 20241128211251.png]]

Finalmente vemos que con estas opciones el volumen NO se automonta.

![[Pasted image 20241128211918.png]]

#### Enunciado 3

>Haciendo uso de la herramienta FTK® Imager, realice la clonación del pendrive evidencia a una imagen en un único archivo denominado pen_drive_3.dd. Si puede, configure dicho programa para que calcule el hash sha256 y sha512. Si no, calcúlelo con otros comandos. Finalmente, guarde la imagen obtenida fuera de la máquina virtual para usar en posteriores prácticas

Hago la instalación de FTK Imager:

![[Pasted image 20241128212325.png]]

Configuro el programa e inicio la clonación

![[Pasted image 20241128213208.png]]

El programa solo proporciona los hashes en MD5 y SHA1 asi que calculo los hashes con el sistema

![[Pasted image 20241128214416.png]]

Una vez más son diferentes, pero dado el problema explicado es de esperar

#### Enunciado 5

##### Enunciado 5/1

>Haga una fotografía de los elementos que se encuentran en el estuche e indique en qué consiste cada uno de ellos y para qué sirven

##### Enunciado 5/2

> Si no está en hora, póngalo en hora UTC. Revise la configuración por defecto de la generación de imágenes (formato, directorio de destino, compresión…)

Estaba en la hora correcta aunque adelantado por 1 minuto, con lo que reducimos la diferencia a 0 segundos configurando la hora.


##### Enunciado 5/3

>Haga una imagen en formato Ex01 del pendrive evidencia en otro pendrive con espacio libre suficiente.


##### Enunciado 5/4

>¿Cuál es el directorio de destino de la imagen? ¿Qué algoritmos de hash calcula el dispositivo al hacer una imagen? ¿Cuánto ocupa la imagen creada?

Cuál es el directorio destino de la imagen: 
![[Pasted image 20241202204842.png]]

![[Pasted image 20241202205033.png]]

Hashes: MD5, SHA1 y SHA256.
Cuanto ocupa la imagen: 126mb
##### Enunciado 5/5

>Haga otra imagen en formato RAW/dd del pendrive. ¿Cuánto ocupa la imagen creada? ¿Coinciden los hashes?

Los hashes coinciden.