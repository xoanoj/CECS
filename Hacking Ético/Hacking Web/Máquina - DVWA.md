[[Maquinas]] de [[Hacking Web]]

Descubrimos la IP de la máquina:

``` bash
sudo nmap -sn 192.168.56.100/24

Starting Nmap 7.95 ( https://nmap.org ) at 2025-04-22 18:58 CEST
Nmap scan report for 192.168.56.1
Host is up (0.00021s latency).
MAC Address: 0A:00:27:00:00:00 (Unknown)
Nmap scan report for 192.168.56.10
Host is up (0.00030s latency).
MAC Address: 08:00:27:12:CB:A8 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.56.112
Host is up (0.00099s latency).
MAC Address: 08:00:27:6D:30:F3 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.56.100
Host is up.
Nmap done: 256 IP addresses (4 hosts up) scanned in 1.98 seconds
```

Es 192.168.56.112.

Entramos a http://192.168.56.112/dvwa usando las credenciales admin:password.

Escaneo con fuga.sh

``` bash
./fuga.sh
--[風雅]--

--[Enumerating Ports]--
--[Scanning]--

--[Detected Services]--

Service              | Version
---------------------+--------------------------
ssh                  | OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
http                 | Apache httpd 2.4.52 ((Ubuntu))

--[Host Fingerprinting]--

Category             | Details
---------------------+--------------------------
Device Type          | general purpose
Running              | Linux 4.X|5.X
OS Details           | Linux 4.15 - 5.19
OS CPE               | cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
Service OS           | Linux
```

