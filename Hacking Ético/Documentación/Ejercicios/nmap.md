Parte de [[Hacking Ético]]
# Nmap

[Nmap](https://nmap.org) ("Network Mapper") is a <b>free and open Source</b> ([license](https://nmap.org/npsl)) utility for network discovery and security auditing. Many systems and network administrators also find it useful for tasks such as network inventory, managing service upgrade schedules, and monitoring host or service uptime. Nmap uses raw IP packets in novel ways to determine what hosts are available on the network, what services (application name and version) those hosts are offering, what operating systems (and OS versions) they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics. It was designed to rapidly scan large networks, but works fine against single hosts. [Nmap](https://nmap.org) runs on all major computer operating systems, and official binary packages are available for Linux, Windows, and Mac OS X. In addition to the classic command-line Nmap executable, the Nmap suite includes an advanced GUI and results viewer ([ZenMap](https://nmap.org/zenmap)), a flexible data transfer, redirection, and debugging tool (Ncat), a utility for comparing scan results ([Ndiff](https://nmap.org/ndiff)), and a packet generation and response analysis tool ([Nping](https://nmap.org/nping))

### Ejemplos de salida

El comando ``` nmap -A -n -T4 -oN nmap_tcp.txt 10.0.0.104``` es un ejemplo de donde se realiza una exploración de puertos, detección de sistema operativo y salida guardada en el fichero ```nmap_tcp.txt```.

Para ver el fichero:

``` java
Nmap scan report for 10.0.0.104
Host is up (0.00057s latency).
Not shown: 994 closed ports
PORTSTATE SERVICE
VERSION
135/tcpopenmsrpc
Microsoft Windows RPC
139/tcpopennetbios-ssn
Microsoft Windows netbios-ssn
445/tcpopenmicrosoft-ds Windows Server 2003 3790 microsoft-ds
1025/tcp openmsrpcMicrosoft Windows RPC
1026/tcp openmsrpcMicrosoft Windows RPC
8089/tcp openssl/httpSplunkd httpd
|_http-server-header: Splunkd
|_http-title: splunkd
| ssl-cert: Subject: commonName=SplunkServerDefaultCert/organizationName=SplunkUser
| Not valid before: 2018-02-10T06:05:40
|_Not valid after:
2021-02-09T06:05:40
|_ssl-date: 2018-02-12T00:51:45+00:00; 0s from scanner time.
| sslv2:
|SSLv2 supported
|ciphers:
|SSL2_RC4_128_WITH_MD5
|SSL2_DES_192_EDE3_CBC_WITH_MD5
|_SSL2_RC2_128_CBC_WITH_MD5
MAC Address: 08:00:27:2C:3E:44 (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Microsoft Windows XP|2003
OS CPE: cpe:/o:microsoft:windows_xp::sp2:professional cpe:/o:microsoft:windows_server_2003
OS details: Microsoft Windows XP Professional SP2 or Windows Server 2003
Network Distance: 1 hop
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows, cpe:/o:microsoft:windows_server_2003Host
script results:
|_nbstat: NetBIOS name: SECURITYNIK-2K3, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:2c:3e:44
(Oracle VirtualBox virtual NIC)| smb-os-discovery:
|OS: Windows Server 2003 3790 (Windows Server 2003 5.2)
|OS CPE: cpe:/o:microsoft:windows_server_2003::-
|Computer name: securitynik-2k3
|NetBIOS computer name: SECURITYNIK-2K3\x00
|Workgroup: WORKGROUP\x00
|_System time: 2018-02-11T19:51:43-05:00
| smb-security-mode:
|account_used: guest
|authentication_level: user
|challenge_response: supported
|_message_signing: disabled (dangerous, but default)
|_smb2-time: Protocol negotiation failed (SMB2)
TRACEROUTE
HOP RTT
1
ADDRESS
0.57 ms 10.0.0.104
```

### In the movies
##### Matrix Reload

>While Nmap had been used in some previous obscure movies, it was The Matrix Reloaded (Wikipedia,IMDB, Amazon) which really turned Nmap into a movie star! We have all seen many movies like Hackers which pass off ridiculous 3D animated eye-candy scenes as hacking. So Fyodor was shocked to find that Trinity does it properly in The Matrix Reloaded. Needing to hack the city power grid, she whips out Nmap version 2.54BETA25, uses it to find a vulnerable SSH server, and then proceeds to exploit it using the SSH1 CRC32 exploit from 2001. Shame on the city for being vulnerable (timing notes).

![[trinity-nmapscreen-hd-crop-1200x728.jpg]]

##### Ocean's 8

>Ocean's 8 (Wikipedia, IMDB, Amazon) is a 2018 comedy heist film starring Sandra Bullock, Rihanna, Cate Blanchett, and Anne Hathaway that continues the series started by Ocean's Eleven in 2001. Rihanna plays the film's main hacker, Nine Ball. She uses Nmap in many scenes to compromise people and companies responsible for guarding the $150 million diamond necklace they want to steal. Nmap is normally shown in the background as context to her hacks rather than taking the leading role.

![[oceans8-samy-video-nmap-scene-cropscalefix-640x317.jpg]]