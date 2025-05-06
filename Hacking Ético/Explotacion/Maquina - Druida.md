[[Maquinas]]

Escaneo de puertos:

``` bash
sudo nmap -sS -p- -T4 192.168.56.218 -oN portscan.txt

Starting Nmap 7.95 ( https://nmap.org ) at 2025-05-02 16:12 CEST
Nmap scan report for 192.168.56.218
Host is up (0.000074s latency).
Not shown: 65526 closed tcp ports (reset)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
111/tcp   open  rpcbind
2049/tcp  open  nfs
8080/tcp  open  http-proxy
37373/tcp open  unknown
42273/tcp open  unknown
45673/tcp open  unknown
46255/tcp open  unknown
MAC Address: 08:00:27:6C:5D:6D (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 4.44 seconds
```

Escaneo agresivo:

``` bash
sudo nmap -sS -sC -sV -O -p 21,22,80,111,2049,8080,37373,42273,45673,46255 192.168.56.218 -oN services.txt

Starting Nmap 7.95 ( https://nmap.org ) at 2025-05-02 16:15 CEST
Nmap scan report for 192.168.56.218
Host is up (0.0011s latency).

PORT      STATE  SERVICE  VERSION
21/tcp    closed ftp
22/tcp    open   ssh      OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 bd:96:ec:08:2f:b1:ea:06:ca:fc:46:8a:7e:8a:e3:55 (RSA)
|   256 56:32:3b:9f:48:2d:e0:7e:1b:df:20:f8:03:60:56:5e (ECDSA)
|_  256 95:dd:20:ee:6f:01:b6:e1:43:2e:3c:f4:38:03:5b:36 (ED25519)
80/tcp    open   http     Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Bolt - Installation error
111/tcp   open   rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      40631/udp   mountd
|   100005  1,2,3      46255/tcp   mountd
|   100005  1,2,3      46415/tcp6  mountd
|   100005  1,2,3      52078/udp6  mountd
|   100021  1,3,4      41713/udp6  nlockmgr
|   100021  1,3,4      42273/tcp   nlockmgr
|   100021  1,3,4      45951/tcp6  nlockmgr
|   100021  1,3,4      58812/udp   nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
2049/tcp  open   nfs      3-4 (RPC #100003)
8080/tcp  open   http     Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: PHP 7.3.27-1~deb10u1 - phpinfo()
| http-open-proxy: Potentially OPEN proxy.
|_Methods supported:CONNECTION
37373/tcp open   mountd   1-3 (RPC #100005)
42273/tcp open   nlockmgr 1-4 (RPC #100021)
45673/tcp open   mountd   1-3 (RPC #100005)
46255/tcp open   mountd   1-3 (RPC #100005)
MAC Address: 08:00:27:6C:5D:6D (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 4.X|5.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
OS details: Linux 4.15 - 5.19, OpenWrt 21.02 (Linux 5.4)
Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.26 seconds
```

Empleamos el script de enumeracion showmount:

``` bash
sudo nmap --script=nfs-showmount 192.168.56.218

Starting Nmap 7.95 ( https://nmap.org ) at 2025-05-02 16:19 CEST
Nmap scan report for 192.168.56.218
Host is up (0.00028s latency).
Not shown: 995 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
111/tcp  open  rpcbind
| nfs-showmount: 
|_  /srv/nfs 172.16.0.0/12 10.0.0.0/8 192.168.0.0/16
2049/tcp open  nfs
8080/tcp open  http-proxy
MAC Address: 08:00:27:6C:5D:6D (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 0.38 seconds
``` 

Como estoy en 192.168.56.100/24 puedo acceder a la share expuesta por 192.168.0.0/16:

``` bash
sudo mount -t nfs 192.168.56.218:/srv/nfs /mnt
   
cd /mnt

ls
backup.zip

unzip backup.zip
Archive:  backup.zip
[backup.zip] id_rsa password:   
```

Vemos que necesita una password, podemos intentar crackearla mediante john.

``` bash
zip2john backup.zip > ~/maquinas/druida/zip.hash

john ~/maquinas/druida/zip.hash --wordlist=/usr/share/wordlists/rockyou.txt

Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
java101          (backup.zip/id_rsa)     
1g 0:00:00:00 DONE (2025-05-02 16:27) 4.347g/s 3989Kp/s 3989Kc/s 3989KC/s jmakm5..jam183
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

Descomprimimos el archivo:

``` bash
sudo unzip backup.zip

Archive:  backup.zip
[backup.zip] id_rsa password: 
password incorrect--reenter: 
  inflating: id_rsa                  
  inflating: todo.txt                
  
ls

backup.zip  id_rsa  todo.txt

cat todo.txt

- Descubrir cómo instalar el sitio web principal correctamente, el archivo de configuración 
parece correcto...
- Actualización del sitio web de desarrollo.
- Seguir codificando en Java porque es fantástico.
 
jp

```

Haciendo fuzzing de directorios web descubro un directory listing en /app/, entre ellos hay una configuracion de BD:

``` bash
database:
    driver: sqlite
    databasename: bolt
    username: bolt
    password: I_love_java

```

En el puerto 8080 vemos un PHP config.