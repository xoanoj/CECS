
Ejercicio de [[Hacking Ético]]

### Contar el nº de líneas del fichero Nmap.md

Comando usado:

``` bash
wc -l Nmap.md
```

Salida:

```
83 Nmap.md
```


### Encontrar las apariciones                                             de la palabra *open* en el fichero Nmap.md

Comando usado:

``` bash
grep open Nmap.md
```

Salida:

```
[Nmap](https://nmap.org) ("Network Mapper") is a **free and open source** ([license](https://nmap.org/npsl/)) utility for network discovery and security auditing. Many systems and network administrators also find it useful for tasks such as network inventory, managing service upgrade schedules, and monitoring host or service uptime. Nmap uses _raw IP packets_ in novel ways to determine what hosts are available on the network, what services (application name and version) those hosts are offering, what operating systems (and OS versions) they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics. It was designed to rapidly scan large networks, but works fine against single hosts. [Nmap][nmap] runs on all major computer operating systems, and official binary packages are available for Linux, Windows, and Mac OS X. In addition to the classic command-line Nmap executable, the Nmap suite includes an advanced GUI and results viewer ([Zenmap](https://nmap.org/zenmap/)), a flexible data transfer, redirection, and debugging tool (Ncat), a utility for comparing scan results ([Ndiff](https://nmap.org/ndiff/)), and a packet generation and response analysis tool ([Nping](https://nmap.org/nping/)). 
135/tcp  open  msrpc        Microsoft Windows RPC
139/tcp  open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds Windows Server 2003 3790 microsoft-ds
1025/tcp open  msrpc        Microsoft Windows RPC
1026/tcp open  msrpc        Microsoft Windows RPC
8089/tcp open  ssl/http     Splunkd httpd 
```

### Contar las apariciones de la palabra open en el fichero Nmap.md

Comando usado:

``` bash
grep open Nmap.md | wc -l
grep -c open Nmap.md
grep -o open Nmap.md | wc -l
grep -w open Nmap.md | wc -l
```

Salida:

```
7
```

### Mostrar las líneas asociadas a los puertos abiertos en el fichero Nmap.md

Comando usado:

``` bash
grep open Nmap.md | grep tcp
```

Salida:

```
135/tcp  open  msrpc        Microsoft Windows RPC
139/tcp  open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds Windows Server 2003 3790 microsoft-ds
1025/tcp open  msrpc        Microsoft Windows RPC
1026/tcp open  msrpc        Microsoft Windows RPC
8089/tcp open  ssl/http     Splunkd httpd
```

### Añadir al fichero una línea: `53/udp open DNS` y mostrar las líneas asociadas a los puertos abiertos en el fichero Nmap.md

Comando usado:

``` bash
echo "53/udp open DNS" >> Nmap.md
grep open Nmap.md | grep -E "tcp|udp"
grep open Nmap.md | grep -e tcp -e udp
```

Salida:

```
135/tcp  open  msrpc        Microsoft Windows RPC
139/tcp  open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds Windows Server 2003 3790 microsoft-ds
1025/tcp open  msrpc        Microsoft Windows RPC
1026/tcp open  msrpc        Microsoft Windows RPC
8089/tcp open  ssl/http     Splunkd httpd
53/udp open DNS
```

### Contar los puertos abiertos en el fichero Nmap.md

Comando usado:

``` bash
grep open Nmap.md | grep -e tcp -e udp | wc -l
```

Salida:

```
7
```

### Encontrar y contar las apariciones de la palabra nmap en el fichero Nmap.md

Comando usado:

``` bash
grep -o nmap Nmap.md | wc -l
```

Salida:

```
17
```

### Encontrar y contar las apariciones de la palabra Nmap en el fichero Nmap.md

Comando usado:

``` bash
grep -o Nmap Nmap.md | wc -l
```

Salida:

```
12
```

### Encontrar y contar las apariciones de la palabra Nmap o nmap (mayúsculas y minúsculas) en el fichero Nmap.md

Comando usado:

``` bash
grep -o -e Nmap -e nmap Nmap.md | wc -l
grep -o -E "Nmap|nmap" Nmap.md | wc -l
grep -i -o nmap Nmap.md | wc -l
```

Salida:

```
29
```

### Mostrar las líneas que contienen la palabra exacta tcp en el fichero Nmap.md

Comando usado:

``` bash
grep -w tcp Nmap.md | wc -l
```

Salida:

```
6
```

### Quedarse con las líneas de los puertos tcp abiertos guardándolas en un ficheros llamado puertos.txt

Comando usado:

``` bash
grep open Nmap.md | grep tcp >> puertos.txt
```

Salida:

```

```

### Mostrar por pantalla las líneas de los puertos tcp abiertos y a la vez guardarlas en un ficheros llamado puertos.txt

Comando usado:

``` bash
grep open Nmap.md | grep tcp | tee puertos.txt
```

Salida:

```
135/tcp  open  msrpc        Microsoft Windows RPC
139/tcp  open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds Windows Server 2003 3790 microsoft-ds
1025/tcp open  msrpc        Microsoft Windows RPC
1026/tcp open  msrpc        Microsoft Windows RPC
8089/tcp open  ssl/http     Splunkd httpd
```

### Mostrar en Kali los usuarios del fichero /etc/passwd que tengan una shell del tipo nologin

Comando usado:

``` bash
grep nologin /etc/passwd
```

Salida:

```
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
systemd-timesync:x:992:992:systemd Time Synchronization:/:/usr/sbin/nologin
messagebus:x:100:102::/nonexistent:/usr/sbin/nologin
strongswan:x:102:65534::/var/lib/strongswan:/usr/sbin/nologin
tcpdump:x:103:105::/nonexistent:/usr/sbin/nologin
sshd:x:104:65534::/run/sshd:/usr/sbin/nologin
usbmux:x:105:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
dnsmasq:x:999:65534:dnsmasq:/var/lib/misc:/usr/sbin/nologin
avahi:x:106:108:Avahi mDNS daemon,,,:/run/avahi-daemon:/usr/sbin/nologin
pulse:x:108:110:PulseAudio daemon,,,:/run/pulse:/usr/sbin/nologin
saned:x:110:114::/var/lib/saned:/usr/sbin/nologin
polkitd:x:991:991:User for polkitd:/:/usr/sbin/nologin
rtkit:x:111:115:RealtimeKit,,,:/proc:/usr/sbin/nologin
colord:x:112:116:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
nm-openvpn:x:113:117:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
nm-openconnect:x:114:118:NetworkManager OpenConnect plugin,,,:/var/lib/NetworkManager:/usr/sbin/nologin
_galera:x:115:65534::/nonexistent:/usr/sbin/nologin
stunnel4:x:990:990:stunnel service system account:/var/run/stunnel4:/usr/sbin/nologin
_rpc:x:117:65534::/run/rpcbind:/usr/sbin/nologin
geoclue:x:118:122::/var/lib/geoclue:/usr/sbin/nologin
sslh:x:120:124::/nonexistent:/usr/sbin/nologin
ntpsec:x:121:127::/nonexistent:/usr/sbin/nologin
redsocks:x:122:128::/var/run/redsocks:/usr/sbin/nologin
rwhod:x:123:65534::/var/spool/rwho:/usr/sbin/nologin
_gophish:x:124:130::/var/lib/gophish:/usr/sbin/nologin
iodine:x:125:65534::/run/iodine:/usr/sbin/nologin
miredo:x:126:65534::/var/run/miredo:/usr/sbin/nologin
statd:x:127:65534::/var/lib/nfs:/usr/sbin/nologin
redis:x:128:131::/var/lib/redis:/usr/sbin/nologin
mosquitto:x:130:133::/var/lib/mosquitto:/usr/sbin/nologin
inetsim:x:131:134::/var/lib/inetsim:/usr/sbin/nologin
_gvm:x:132:135::/var/lib/openvas:/usr/sbin/nologin
cups-pk-helper:x:133:139:user for cups-pk-helper service,,,:/nonexistent:/usr/sbin/nologin
bacula:x:134:140:Bacula:/var/lib/bacula:/usr/sbin/nologin
```

### Mostrar en Kali los usuarios del fichero /etc/passwd que tengan una shell del tipo nologin o false

Comando usado:

``` bash
grep -E "nologin|false" /etc/passwd
```

Salida:

```
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
systemd-timesync:x:992:992:systemd Time Synchronization:/:/usr/sbin/nologin
messagebus:x:100:102::/nonexistent:/usr/sbin/nologin
tss:x:101:104:TPM software stack,,,:/var/lib/tpm:/bin/false
strongswan:x:102:65534::/var/lib/strongswan:/usr/sbin/nologin
tcpdump:x:103:105::/nonexistent:/usr/sbin/nologin
sshd:x:104:65534::/run/sshd:/usr/sbin/nologin
usbmux:x:105:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
dnsmasq:x:999:65534:dnsmasq:/var/lib/misc:/usr/sbin/nologin
avahi:x:106:108:Avahi mDNS daemon,,,:/run/avahi-daemon:/usr/sbin/nologin
speech-dispatcher:x:107:29:Speech Dispatcher,,,:/run/speech-dispatcher:/bin/false
pulse:x:108:110:PulseAudio daemon,,,:/run/pulse:/usr/sbin/nologin
lightdm:x:109:112:Light Display Manager:/var/lib/lightdm:/bin/false
saned:x:110:114::/var/lib/saned:/usr/sbin/nologin
polkitd:x:991:991:User for polkitd:/:/usr/sbin/nologin
rtkit:x:111:115:RealtimeKit,,,:/proc:/usr/sbin/nologin
colord:x:112:116:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
nm-openvpn:x:113:117:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
nm-openconnect:x:114:118:NetworkManager OpenConnect plugin,,,:/var/lib/NetworkManager:/usr/sbin/nologin
_galera:x:115:65534::/nonexistent:/usr/sbin/nologin
mysql:x:116:120:MariaDB Server,,,:/nonexistent:/bin/false
stunnel4:x:990:990:stunnel service system account:/var/run/stunnel4:/usr/sbin/nologin
_rpc:x:117:65534::/run/rpcbind:/usr/sbin/nologin
geoclue:x:118:122::/var/lib/geoclue:/usr/sbin/nologin
Debian-snmp:x:119:123::/var/lib/snmp:/bin/false
sslh:x:120:124::/nonexistent:/usr/sbin/nologin
ntpsec:x:121:127::/nonexistent:/usr/sbin/nologin
redsocks:x:122:128::/var/run/redsocks:/usr/sbin/nologin
rwhod:x:123:65534::/var/spool/rwho:/usr/sbin/nologin
_gophish:x:124:130::/var/lib/gophish:/usr/sbin/nologin
iodine:x:125:65534::/run/iodine:/usr/sbin/nologin
miredo:x:126:65534::/var/run/miredo:/usr/sbin/nologin
statd:x:127:65534::/var/lib/nfs:/usr/sbin/nologin
redis:x:128:131::/var/lib/redis:/usr/sbin/nologin
mosquitto:x:130:133::/var/lib/mosquitto:/usr/sbin/nologin
inetsim:x:131:134::/var/lib/inetsim:/usr/sbin/nologin
_gvm:x:132:135::/var/lib/openvas:/usr/sbin/nologin
cups-pk-helper:x:133:139:user for cups-pk-helper service,,,:/nonexistent:/usr/sbin/nologin
bacula:x:134:140:Bacula:/var/lib/bacula:/usr/sbin/nologin
```

### Mostrar en Kali los usuarios del fichero /etc/passwd que tengan una shell que no sea del tipo nologin

Comando usado:

``` bash
grep -v "nologin" /etc/passwd
```

Salida:

```
root:x:0:0:root:/root:/usr/bin/zsh
sync:x:4:65534:sync:/bin:/bin/sync
tss:x:101:104:TPM software stack,,,:/var/lib/tpm:/bin/false
speech-dispatcher:x:107:29:Speech Dispatcher,,,:/run/speech-dispatcher:/bin/false
lightdm:x:109:112:Light Display Manager:/var/lib/lightdm:/bin/false
mysql:x:116:120:MariaDB Server,,,:/nonexistent:/bin/false
Debian-snmp:x:119:123::/var/lib/snmp:/bin/false
postgres:x:129:132:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
kali:x:1000:1000:,,,:/home/kali:/usr/bin/zsh
```

### Mostrar en Kali los usuarios del fichero /etc/passwd que tengan una shell que no sea ni del tipo nologin ni false

Comando usado:

``` bash
grep -v -E "nologin|false" /etc/passwd
```

Salida:

```
root:x:0:0:root:/root:/usr/bin/zsh
sync:x:4:65534:sync:/bin:/bin/sync
postgres:x:129:132:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
kali:x:1000:1000:,,,:/home/kali:/usr/bin/zsh
```

### Localiza los usuarios con uid 0 o gid 0 o directorio casa /root

Comando usado:

``` bash
grep -E ":0|0:|/root" /etc/passwd
grep -e ":0:" -e "/root" /etc/passwd
```

Salida:

```
root:x:0:0:root:/root:/usr/bin/zsh
```

### Mostrar por pantalla los usuarios del fichero /etc/passwd

Comando usado:

``` bash
cut -d ":" -f 1 /etc/passwd
```

Salida:

```
root
daemon
bin
sys
sync
games
man
lp
mail
news
uucp
proxy
www-data
backup
list
irc
_apt
nobody
systemd-network
systemd-timesync
messagebus
tss
strongswan
tcpdump
sshd
usbmux
dnsmasq
avahi
speech-dispatcher
pulse
lightdm
saned
polkitd
rtkit
colord
nm-openvpn
nm-openconnect
_galera
mysql
stunnel4
_rpc
geoclue
Debian-snmp
sslh
ntpsec
redsocks
rwhod
_gophish
iodine
miredo
statd
redis
postgres
mosquitto
inetsim
_gvm
kali
cups-pk-helper
bacula
```

### Mostrar por pantalla los usuarios del fichero /etc/passwd junto con su directorio home y su shell

Comando usado:

``` bash
cut -d ":" -f 1,6,7 /etc/passwd
```

Salida:

```
root:/root:/usr/bin/zsh
daemon:/usr/sbin:/usr/sbin/nologin
bin:/bin:/usr/sbin/nologin
sys:/dev:/usr/sbin/nologin
sync:/bin:/bin/sync
games:/usr/games:/usr/sbin/nologin
man:/var/cache/man:/usr/sbin/nologin
lp:/var/spool/lpd:/usr/sbin/nologin
mail:/var/mail:/usr/sbin/nologin
news:/var/spool/news:/usr/sbin/nologin
uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:/bin:/usr/sbin/nologin
www-data:/var/www:/usr/sbin/nologin
backup:/var/backups:/usr/sbin/nologin
list:/var/list:/usr/sbin/nologin
irc:/run/ircd:/usr/sbin/nologin
_apt:/nonexistent:/usr/sbin/nologin
nobody:/nonexistent:/usr/sbin/nologin
systemd-network:/:/usr/sbin/nologin
systemd-timesync:/:/usr/sbin/nologin
messagebus:/nonexistent:/usr/sbin/nologin
tss:/var/lib/tpm:/bin/false
strongswan:/var/lib/strongswan:/usr/sbin/nologin
tcpdump:/nonexistent:/usr/sbin/nologin
sshd:/run/sshd:/usr/sbin/nologin
usbmux:/var/lib/usbmux:/usr/sbin/nologin
dnsmasq:/var/lib/misc:/usr/sbin/nologin
avahi:/run/avahi-daemon:/usr/sbin/nologin
speech-dispatcher:/run/speech-dispatcher:/bin/false
pulse:/run/pulse:/usr/sbin/nologin
lightdm:/var/lib/lightdm:/bin/false
saned:/var/lib/saned:/usr/sbin/nologin
polkitd:/:/usr/sbin/nologin
rtkit:/proc:/usr/sbin/nologin
colord:/var/lib/colord:/usr/sbin/nologin
nm-openvpn:/var/lib/openvpn/chroot:/usr/sbin/nologin
nm-openconnect:/var/lib/NetworkManager:/usr/sbin/nologin
_galera:/nonexistent:/usr/sbin/nologin
mysql:/nonexistent:/bin/false
stunnel4:/var/run/stunnel4:/usr/sbin/nologin
_rpc:/run/rpcbind:/usr/sbin/nologin
geoclue:/var/lib/geoclue:/usr/sbin/nologin
Debian-snmp:/var/lib/snmp:/bin/false
sslh:/nonexistent:/usr/sbin/nologin
ntpsec:/nonexistent:/usr/sbin/nologin
redsocks:/var/run/redsocks:/usr/sbin/nologin
rwhod:/var/spool/rwho:/usr/sbin/nologin
_gophish:/var/lib/gophish:/usr/sbin/nologin
iodine:/run/iodine:/usr/sbin/nologin
miredo:/var/run/miredo:/usr/sbin/nologin
statd:/var/lib/nfs:/usr/sbin/nologin
redis:/var/lib/redis:/usr/sbin/nologin
postgres:/var/lib/postgresql:/bin/bash
mosquitto:/var/lib/mosquitto:/usr/sbin/nologin
inetsim:/var/lib/inetsim:/usr/sbin/nologin
_gvm:/var/lib/openvas:/usr/sbin/nologin
kali:/home/kali:/usr/bin/zsh
cups-pk-helper:/nonexistent:/usr/sbin/nologin
bacula:/var/lib/bacula:/usr/sbin/nologin
```

### Mostrar por pantalla los usuarios del fichero /etc/passwd junto con su directorio home y su shell, siempre que tengan una shell que no sea ni del tipo nologin ni false

Comando usado:

``` bash
cut -d ":" -f 1,6,7 /etc/passwd | grep -v -E "nologin|false"
```

Salida:

```
root:/root:/usr/bin/zsh
sync:/bin:/bin/sync
postgres:/var/lib/postgresql:/bin/bash
kali:/home/kali:/usr/bin/zsh
```

### Mostrar por pantalla los diferentes shells de los usuarios del /etc/passwd

Comando usado:

``` bash
cut -d ":" -f 1,7 /etc/passwd
```

Salida:

```
root:/usr/bin/zsh
daemon:/usr/sbin/nologin
bin:/usr/sbin/nologin
sys:/usr/sbin/nologin
sync:/bin/sync
games:/usr/sbin/nologin
man:/usr/sbin/nologin
lp:/usr/sbin/nologin
mail:/usr/sbin/nologin
news:/usr/sbin/nologin
uucp:/usr/sbin/nologin
proxy:/usr/sbin/nologin
www-data:/usr/sbin/nologin
backup:/usr/sbin/nologin
list:/usr/sbin/nologin
irc:/usr/sbin/nologin
_apt:/usr/sbin/nologin
nobody:/usr/sbin/nologin
systemd-network:/usr/sbin/nologin
systemd-timesync:/usr/sbin/nologin
messagebus:/usr/sbin/nologin
tss:/bin/false
strongswan:/usr/sbin/nologin
tcpdump:/usr/sbin/nologin
sshd:/usr/sbin/nologin
usbmux:/usr/sbin/nologin
dnsmasq:/usr/sbin/nologin
avahi:/usr/sbin/nologin
speech-dispatcher:/bin/false
pulse:/usr/sbin/nologin
lightdm:/bin/false
saned:/usr/sbin/nologin
polkitd:/usr/sbin/nologin
rtkit:/usr/sbin/nologin
colord:/usr/sbin/nologin
nm-openvpn:/usr/sbin/nologin
nm-openconnect:/usr/sbin/nologin
_galera:/usr/sbin/nologin
mysql:/bin/false
stunnel4:/usr/sbin/nologin
_rpc:/usr/sbin/nologin
geoclue:/usr/sbin/nologin
Debian-snmp:/bin/false
sslh:/usr/sbin/nologin
ntpsec:/usr/sbin/nologin
redsocks:/usr/sbin/nologin
rwhod:/usr/sbin/nologin
_gophish:/usr/sbin/nologin
iodine:/usr/sbin/nologin
miredo:/usr/sbin/nologin
statd:/usr/sbin/nologin
redis:/usr/sbin/nologin
postgres:/bin/bash
mosquitto:/usr/sbin/nologin
inetsim:/usr/sbin/nologin
_gvm:/usr/sbin/nologin
kali:/usr/bin/zsh
cups-pk-helper:/usr/sbin/nologin
bacula:/usr/sbin/nologin
```

### Igual que antes pero ordenados alfabéticamente

Comando usado:

``` bash
cut -d ":" -f 7 /etc/passwd | sort
```

Salida:

```
/bin/bash
/bin/false
/bin/false
/bin/false
/bin/false
/bin/false
/bin/sync
/usr/bin/zsh
/usr/bin/zsh
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
```

### Igual que antes pero sin que aparezcan repetidos

Comando usado:

``` bash
cut -d ":" -f 7 /etc/passwd | sort -u
```

Salida:

```
/bin/bash
/bin/false
/bin/sync
/usr/bin/zsh
/usr/sbin/nologin
```

### Di cuantos usuarios tienen cada uno de los tipos de shell 

Comando usado:

``` bash
cut -d ":" -f 7 /etc/passwd | sort | uniq -c
```

Salida:

```
      1 /bin/bash
      5 /bin/false
      1 /bin/sync
      2 /usr/bin/zsh
     50 /usr/sbin/nologin
```

### Di cuantos usuarios tienen cada uno de los tipos de shell , ordenándolos de mayor a menor

Comando usado:

``` bash
cut -d ":" -f 7 /etc/passwd | sort | uniq -c | sort -n
```

Salida:

```
      1 /bin/bash
      1 /bin/sync
      2 /usr/bin/zsh
      5 /bin/false
     50 /usr/sbin/nologin
```

### Mostrar usuarios usando `awk`

Comando usado:

``` bash
awk -F ":" '{print $1}' /etc/passwd
```

Salida:

```
root
daemon
bin
sys
sync
games
man
lp
mail
news
uucp
proxy
www-data
backup
list
irc
_apt
nobody
systemd-network
systemd-timesync
messagebus
tss
strongswan
tcpdump
sshd
usbmux
dnsmasq
avahi
speech-dispatcher
pulse
lightdm
saned
polkitd
rtkit
colord
nm-openvpn
nm-openconnect
_galera
mysql
stunnel4
_rpc
geoclue
Debian-snmp
sslh
ntpsec
redsocks
rwhod
_gophish
iodine
miredo
statd
redis
postgres
mosquitto
inetsim
_gvm
kali
cups-pk-helper
bacula
```

### Mostrar por pantalla los usuarios del fichero /etc/passwd junto con su directorio home y su shell usando `awk`

Comando usado:

``` bash
awk -F ":" '{print $1,$6,$7}' /etc/passwd
```

Salida:

```
root /root /usr/bin/zsh
daemon /usr/sbin /usr/sbin/nologin
bin /bin /usr/sbin/nologin
sys /dev /usr/sbin/nologin
sync /bin /bin/sync
games /usr/games /usr/sbin/nologin
man /var/cache/man /usr/sbin/nologin
lp /var/spool/lpd /usr/sbin/nologin
mail /var/mail /usr/sbin/nologin
news /var/spool/news /usr/sbin/nologin
uucp /var/spool/uucp /usr/sbin/nologin
proxy /bin /usr/sbin/nologin
www-data /var/www /usr/sbin/nologin
backup /var/backups /usr/sbin/nologin
list /var/list /usr/sbin/nologin
irc /run/ircd /usr/sbin/nologin
_apt /nonexistent /usr/sbin/nologin
nobody /nonexistent /usr/sbin/nologin
systemd-network / /usr/sbin/nologin
systemd-timesync / /usr/sbin/nologin
messagebus /nonexistent /usr/sbin/nologin
tss /var/lib/tpm /bin/false
strongswan /var/lib/strongswan /usr/sbin/nologin
tcpdump /nonexistent /usr/sbin/nologin
sshd /run/sshd /usr/sbin/nologin
usbmux /var/lib/usbmux /usr/sbin/nologin
dnsmasq /var/lib/misc /usr/sbin/nologin
avahi /run/avahi-daemon /usr/sbin/nologin
speech-dispatcher /run/speech-dispatcher /bin/false
pulse /run/pulse /usr/sbin/nologin
lightdm /var/lib/lightdm /bin/false
saned /var/lib/saned /usr/sbin/nologin
polkitd / /usr/sbin/nologin
rtkit /proc /usr/sbin/nologin
colord /var/lib/colord /usr/sbin/nologin
nm-openvpn /var/lib/openvpn/chroot /usr/sbin/nologin
nm-openconnect /var/lib/NetworkManager /usr/sbin/nologin
_galera /nonexistent /usr/sbin/nologin
mysql /nonexistent /bin/false
stunnel4 /var/run/stunnel4 /usr/sbin/nologin
_rpc /run/rpcbind /usr/sbin/nologin
geoclue /var/lib/geoclue /usr/sbin/nologin
Debian-snmp /var/lib/snmp /bin/false
sslh /nonexistent /usr/sbin/nologin
ntpsec /nonexistent /usr/sbin/nologin
redsocks /var/run/redsocks /usr/sbin/nologin
rwhod /var/spool/rwho /usr/sbin/nologin
_gophish /var/lib/gophish /usr/sbin/nologin
iodine /run/iodine /usr/sbin/nologin
miredo /var/run/miredo /usr/sbin/nologin
statd /var/lib/nfs /usr/sbin/nologin
redis /var/lib/redis /usr/sbin/nologin
postgres /var/lib/postgresql /bin/bash
mosquitto /var/lib/mosquitto /usr/sbin/nologin
inetsim /var/lib/inetsim /usr/sbin/nologin
_gvm /var/lib/openvas /usr/sbin/nologin
kali /home/kali /usr/bin/zsh
cups-pk-helper /nonexistent /usr/sbin/nologin
bacula /var/lib/bacula /usr/sbin/nologin
```

### Idem pero separando los campos con :

Comando usado:

``` bash
awk -F ":" '{print $1":"$6":"$7}' /etc/passwd
```

Salida:

```
root:/root:/usr/bin/zsh
daemon:/usr/sbin:/usr/sbin/nologin
bin:/bin:/usr/sbin/nologin
sys:/dev:/usr/sbin/nologin
sync:/bin:/bin/sync
games:/usr/games:/usr/sbin/nologin
man:/var/cache/man:/usr/sbin/nologin
lp:/var/spool/lpd:/usr/sbin/nologin
mail:/var/mail:/usr/sbin/nologin
news:/var/spool/news:/usr/sbin/nologin
uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:/bin:/usr/sbin/nologin
www-data:/var/www:/usr/sbin/nologin
backup:/var/backups:/usr/sbin/nologin
list:/var/list:/usr/sbin/nologin
irc:/run/ircd:/usr/sbin/nologin
_apt:/nonexistent:/usr/sbin/nologin
nobody:/nonexistent:/usr/sbin/nologin
systemd-network:/:/usr/sbin/nologin
systemd-timesync:/:/usr/sbin/nologin
messagebus:/nonexistent:/usr/sbin/nologin
tss:/var/lib/tpm:/bin/false
strongswan:/var/lib/strongswan:/usr/sbin/nologin
tcpdump:/nonexistent:/usr/sbin/nologin
sshd:/run/sshd:/usr/sbin/nologin
usbmux:/var/lib/usbmux:/usr/sbin/nologin
dnsmasq:/var/lib/misc:/usr/sbin/nologin
avahi:/run/avahi-daemon:/usr/sbin/nologin
speech-dispatcher:/run/speech-dispatcher:/bin/false
pulse:/run/pulse:/usr/sbin/nologin
lightdm:/var/lib/lightdm:/bin/false
saned:/var/lib/saned:/usr/sbin/nologin
polkitd:/:/usr/sbin/nologin
rtkit:/proc:/usr/sbin/nologin
colord:/var/lib/colord:/usr/sbin/nologin
nm-openvpn:/var/lib/openvpn/chroot:/usr/sbin/nologin
nm-openconnect:/var/lib/NetworkManager:/usr/sbin/nologin
_galera:/nonexistent:/usr/sbin/nologin
mysql:/nonexistent:/bin/false
stunnel4:/var/run/stunnel4:/usr/sbin/nologin
_rpc:/run/rpcbind:/usr/sbin/nologin
geoclue:/var/lib/geoclue:/usr/sbin/nologin
Debian-snmp:/var/lib/snmp:/bin/false
sslh:/nonexistent:/usr/sbin/nologin
ntpsec:/nonexistent:/usr/sbin/nologin
redsocks:/var/run/redsocks:/usr/sbin/nologin
rwhod:/var/spool/rwho:/usr/sbin/nologin
_gophish:/var/lib/gophish:/usr/sbin/nologin
iodine:/run/iodine:/usr/sbin/nologin
miredo:/var/run/miredo:/usr/sbin/nologin
statd:/var/lib/nfs:/usr/sbin/nologin
redis:/var/lib/redis:/usr/sbin/nologin
postgres:/var/lib/postgresql:/bin/bash
mosquitto:/var/lib/mosquitto:/usr/sbin/nologin
inetsim:/var/lib/inetsim:/usr/sbin/nologin
_gvm:/var/lib/openvas:/usr/sbin/nologin
kali:/home/kali:/usr/bin/zsh
cups-pk-helper:/nonexistent:/usr/sbin/nologin
bacula:/var/lib/bacula:/usr/sbin/nologin
```

### Quedarse con el campo 1 del fichero puertos.txt usando `cut`

Comando usado:

``` bash
cut -d " " -f 1 puertos.txt
```

Salida:

```
135/tcp
139/tcp
445/tcp
1025/tcp
1026/tcp
8089/tcp
```

### Quedarse con el campo 3 (servicio) del fichero puertos.txt usando `cut`

Comando usado:

``` bash
---
```

Salida:

```
---
```

### Repetir anterior usando `awk`

Comando usado:

``` bash
awk -F " " '{print $3}' puertos.txt
```

Salida:

```
msrpc
netbios-ssn
microsoft-ds
msrpc
msrpc
ssl/http
```

### Partiendo del fichero nmap_A_scan_tcp.txt hacer un listado de los puertos abiertos y en cuantos equipos en total están abiertos. Ordena el resultado de mayor a menor.

Comando usado:

``` bash
grep 'open' nmap_A_scan_tcp.txt | sort -n | awk -F " " '{print $1}' | grep -v 'Warning' | uniq -c | sort -nr
```

Salida:

```
      5 445/tcp
      5 139/tcp
      4 135/tcp
      3 8089/tcp
      2 80/tcp
      2 53/tcp
      1 88/tcp
      1 8180/tcp
      1 8009/tcp
      1 6667/tcp
      1 636/tcp
      1 6000/tcp
      1 593/tcp
      1 5900/tcp
      1 5432/tcp
      1 514/tcp
      1 513/tcp
      1 512/tcp
      1 49161/tcp
      1 49158/tcp
      1 49157/tcp
      1 49155/tcp
      1 49154/tcp
      1 464/tcp
      1 389/tcp
      1 3306/tcp
      1 3269/tcp
      1 3268/tcp
      1 25/tcp
      1 23/tcp
      1 22/tcp
      1 21/tcp
      1 2121/tcp
      1 2049/tcp
      1 1524/tcp
      1 111/tcp
      1 1099/tcp
      1 1026/tcp
      1 1025/tcp
                 
```

### Para hacer un ataque de contraseñas, extrae una lista de usuarios a partir del fichero nmap_smb_users.txt y guardala en un fichero llamado usuarios.txt

Comando usado:

``` bash
grep "METASPLOITABLE" nmap_smb_users.txt | awk -F "\\" '{print $2}' | awk -F " " '{print $1}' | tee usuarios.txt
```

Salida:

```
backup
bin
bind
daemon
dhcp
distccd
ftp
games
gnats
irc
klog
libuuid
list
lp
mail
man
msfadmin
mysql
news
nobody
postfix
postgres
proftpd
proxy
root
service
sshd
sync
sys
syslog
telnetd
tomcat55
user
uucp
www-data
```

### Log Apache --> fichero access_log.txt

#### Nº de líneas

Comando usado:

``` bash
wc -l access_log.txt
```

Salida:

```
1173 access_log.txt
```

#### Ver última línea y analizar la estructura

Comando usado:

``` bash
tail -n 1 access_log.txt
```

Salida:

```
70.194.129.34 - - [25/Apr/2013:15:55:42 -0700] "GET / HTTP/1.1" 200 4023 "-" "Mozilla/5.0 (Linux; U; Android 4.1.2; en-us; SCH-I535 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30" "www.random-site.com"
```

#### Ver IPs de clientes

Comando usado:

``` bash
cut -d " " -f 1 access_log.txt | sort -u
```

De ordenar con sort -uV usaria toda la ip en vez de solo los primeros digitos

Salida:

```
201.21.152.44
208.115.113.91
208.54.80.244
208.68.234.99
70.194.129.34
72.133.47.242
88.112.192.2
98.238.13.253
99.127.177.95
```

#### Ver IPs de clientes y el nº de peticiones que hacen ordenadas de mayor a menor

Comando usado:

``` bash
cut -d " " -f 1 access_log.txt | sort | uniq -c | sort -nr
```

Salida:

```
   1038 208.68.234.99
     59 208.115.113.91
     22 208.54.80.244
     21 99.127.177.95
      8 98.238.13.253
      8 88.112.192.2
      8 72.133.47.242
      8 70.194.129.34
      1 201.21.152.44
```

#### Ver códigos de respuesta

Comando usado:

``` bash
cut -d " " -f 9 access_log.txt
```

Salida:

```
[...]
```

#### Ver peticiones del equipo más activo

Comando usado:

``` bash
grep $(cut -d " " -f 1 access_log.txt | sort | uniq -c | sort -nr | awk -F " " '{print $2}' | head -n 1) access_log.txt
```

Salida:

```
[...]
```

#### Ver user-agent y cuantas peticiones se ejecutan con cada uno de ellos

Comando usado:

``` bash

```

Salida:

```

```

#### Buscar las peticiones realizadas por el User-Agent _Teh Forest Lobster_

Comando usado:

``` bash

```

Salida:

```

```

#### Ver peticiones donde aparezca la palabra admin

Comando usado:

``` bash

```

Salida:

```

```

#### Buscar la IP de los solicitantes entre las peticiones donde apareza la palabra 

#### admin 

Comando usado:

``` bash

```

Salida:

```

```

#### Buscar entre las peticiones donde apareza la palabra admin, los códigos de 

#### respuesta para ver si alguna solicitud tuvo éxito

Comando usado:

``` bash

```

Salida:

```

```

#### Localizar la línea donde la solicitud _admin_ obtuvo éxito y mostrar 2 líneas anteriores y posteriores

- con `grep/awk` y `sed` en dos comandos
- con `awk` y `grep`

Comando usado:

``` bash

```

Salida:

```

```

#### Búsquedas peticiones donde aparezca la palabra dallas

Comando usado:

``` bash

```

Salida:

```

```

###  ENISA 1: fichero 24022007.txt

#### Nº de líneas

Comando usado:

``` bash

```

Salida:

```

```

#### Ver las primeras líneas para hacernos una idea de la estructura de las mismas

Comando usado:

``` bash

```

Salida:

```

```

#### Crear una lista de IPs de posibles atacantes ordenándolas en base al número de apariciones y después mostrar el nº  de apariciones y el nº total de equipos

> Generate a list of unique attacking IP addresses. How many distinct source hosts were taking part in the attack? (Assume that attacking packets = UDP packets). Descartando las IPs privadas de clase A:

Comando usado:

``` bash

```

Salida:

```

```