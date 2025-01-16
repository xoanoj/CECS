Parte de [[Enumeracion de Servicios]]

Se encuentran en /usr/share/nmap/scripts/, sirven para la enumeracion de servicios (principalmente) como los modulos auxiliares de metasploit.

Tambien sirve para detectar vulnerabilidades y backdoors

Se utilizan con la flag -sC (para lanzar los basicos de reconocimiento por defecto) o con -sC=\[scriptPath\] para escoger alguno en concreto o --script \[script\].

Se escriben en Lua, se pueden añadir scripts customs a la carpeta /usr/share/nmap/scripts

Ejemplo con metasploitable2:

Comando:

``` bash
sudo nmap -n -Pn -sV -sC -O -p 22,80,81 192.168.56.102
```

Salida:

``` java
Starting Nmap 7.95 ( https://nmap.org ) at 2025-01-16 17:54 CET
Nmap scan report for 192.168.56.102
Host is up (0.00089s latency).

PORT   STATE  SERVICE   VERSION
22/tcp open   ssh       OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
| ssh-hostkey: 
|   1024 60:0f:cf:e1:c0:5f:6a:74:d6:90:24:fa:c4:d5:6c:cd (DSA)
|_  2048 56:56:24:0f:21:1d:de:a7:2b:ae:61:b1:24:3d:e8:f3 (RSA)
80/tcp open   http      Apache httpd 2.2.8 ((Ubuntu) DAV/2)
|_http-title: Metasploitable2 - Linux
|_http-server-header: Apache/2.2.8 (Ubuntu) DAV/2
81/tcp closed hosts2-ns
MAC Address: 08:00:27:7B:8B:9E (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6
OS details: Linux 2.6.9 - 2.6.33
Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.90 seconds
```

Ahora usaremos nmap para ver si vsftpd tiene un backdoor:

``` bash
sudo nmap -n -Pn --script ftp-vsftpd-backdoor -p 21 192.168.56.102
```

Salida:

``` java
Starting Nmap 7.95 ( https://nmap.org ) at 2025-01-16 18:00 CET
Nmap scan report for 192.168.56.102
Host is up (0.00051s latency).

PORT   STATE SERVICE
21/tcp open  ftp
| ftp-vsftpd-backdoor: 
|   VULNERABLE:
|   vsFTPd version 2.3.4 backdoor
|     State: VULNERABLE (Exploitable)
|     IDs:  CVE:CVE-2011-2523  BID:48539
|       vsFTPd version 2.3.4 backdoor, this was reported on 2011-07-04.
|     Disclosure date: 2011-07-03
|     Exploit results:
|       Shell command: id
|       Results: uid=0(root) gid=0(root)
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2011-2523
|       http://scarybeastsecurity.blogspot.com/2011/07/alert-vsftpd-download-backdoored.html
|       https://www.securityfocus.com/bid/48539
|_      https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/unix/ftp/vsftpd_234_backdoor.rb
MAC Address: 08:00:27:7B:8B:9E (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 1.52 seconds
```