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

---
### Clonación de un pendrive haciendo uso de una máquina virtual con Windows 10 Professional

Al conectar un pendrive (no el de la evidencia) a la máquina de Windows me dio cuenta de que anteriormente se monta en el anfitrión Debian12 aunque tenga un filtro de USB que debería pasar todas las conexiones, para tratar de evitar este montaje (que cambiaria metadatos y el hash en consecuencia) voy a copiar los filtros de la máquina de Debian, aunque quizás fallen como ya sospecho que hicieron en el ejercicio anterior.

![[Pasted image 20241128201453.png]]

Y copio también este filtro de USB para hacer pruebas sin comprometer la evidencia:

![[Pasted image 20241128201616.png]]

Al conectar el USB de prueba se monta en el afitrión de forma automática, con lo que esta técnica no funciona y al conectar la evidencia el montado en Debian12 podría potencialmente cambiar metadatos. De encontrar cambios en los hashes otra vez podriamos asumir que se debe a esto.

De todos modos, cuando a continuación se vea que el SSD Sabrent pasa a la máquina virtual de Windows automáticamente se debe tener en cuenta que esto es porque se monto a Debian12 primero y despúes se creo un filtro, esto funciona correctamente, el problema surge con la evidencia ya que idealmente no queremos arriesgarnos a montarlo ni para crear el filtro.

Otra opción que podemos probar es utilizar el host de Windows del sistema para ver si así logramos que no se automonten en el sistema.
#### Enunciado 1

> Enchufe el segundo (no el de la evidencia) dispositivo USB (el de más de 5GB libres) y compruebe si la máquina lo monta automáticamente. En Linux, algunos comandos como dmesg y sudo fdisk -l detectan si el pendrive está enchufado (detectado), mientras que otros como mount, df, etc, detectan si el pendrive está montado.

