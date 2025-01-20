Parte de [[Cortafuegos con IPTables]]

![[Pasted image 20250117184314.png]]

## Requisitos:

![[Pasted image 20250117185623.png]]
![[Pasted image 20250117185645.png]]
![[Pasted image 20250117185703.png]]

---
## Configuración

Para persistencia de reglas en RL y RDI los containers contienen el paquete iptables-persistent, el cual les permite almacenar de modo persistente las reglas en un archivo de texto dentro del directorio /etc/iptables. Ademas en los container ese directorio esta asociado a un volumen de persistencia.

Politicas para todos los hosts:

``` bash
iptables -P OUTPUT DROP
iptables -P INPUT DROP
```

Trafico local:

``` bash
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
```

Conexiones ESTABLISHED y RELATED para todos los hosts:

``` bash
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
```

Trafico de salida http/https y resolucion DNS para todos los hosts:

``` bash
iptables -A OUTPUT -p tcp -m multiport --dports 80,443 -m conntrack --ctstate NEW -j ACCEPT
iptables -A OUTPUT -p udp --dport 53 -d 8.8.8.8 -j ACCEPT
iptables -A OUTPUT -p udp --dport 53 -d 8.8.4.4 -j ACCEPT
```

Trafico entrante procedente de DNS para todos los hosts:

``` bash
iptables -A INPUT -p udp --sport 53 -s 8.8.8.8 -j ACCEPT
iptables -A INPUT -p udp --sport 53 -s 8.8.4.4 -j ACCEPT
```

Acceso ssh desde sat para todos los hosts:

``` bash
iptables -A INPUT -p tcp --dport 22 -s 192.168.112.0/24 -m conntrack --ctstate NEW -j ACCEPT
```

Trafico entrante para host www:

``` bash
iptables -A INPUT -p tcp -m multiport --dports 80,443 -m conntrack --ctstate NEW -j ACCEPT
```

### Reglas de puertas de enlace:

Politicas en todas las puertas:

``` bash
iptables -P OUTPUT DROP
iptables -P INPUT DROP
iptables -P FORWARD DROP
```

#### Puerta RL:

Trafico en ambas direcciones entre eth0 y eth1:

``` bash
iptables -A FORWARD -i eth0 -s 192.168.110.0/24 -o eth1 -d 192.168.111.0/24 -j ACCEPT
iptables -A FORWARD -i eth1 -s 192.168.110.0/24 -o eth1 -d 192.168.110.0/24 -j ACCEPT
```

Trafico en ambas direcciones entre eth0 y eth2:

``` bash
iptables -A FORWARD -i eth0 -s 192.168.110.0/24 -o eth2 -d 192.168.112.0/24 -j ACCEPT
iptables -A FORWARD -i eth2 -s 192.168.112.0/24 -o eth0 -d 192.168.110.0/24 -j ACCEPT
```

Trafico en ambas direccione entre eth1 y eth2:

``` bash
iptables -A FORWARD -i eth1 -s 192.168.111.0/24 -o eth2 -d 192.168.112.0/24 -j ACCEPT
iptables -A FORWARD -i eth2 -s 192.168.112.0/24 -o eth1 -d 192.168.111.0/24 -j ACCEPT
```

Trafico ESTABLISHED y RELATED:

``` bash
iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
```

Trafico NEW saliente port eth2 hacia http/https y DNS:

``` bash
iptables -A FORWARD -p tcp -o eth2 -m multiport --dports 80,443 -m conntrack --ctstate NEW -j ACCEPT
iptables -A FORWARD -p udp -o eth2 --dport 53 -d 8.8.8.8 -j ACCEPT
iptables -A FORWARD -p udp -o eth2 --dport 53 -d 8.8.4.4 -j ACCEPT
```

Trafico entrante de servicios DNS por eth2 en RL:

``` bash
iptables -A FORWARD -p udp -i eth2 --sport 53 -s 8.8.8.8 -j ACCEPT
iptables -A FORWARD -p udp -i eth2 --sport 53 -s 8.8.4.4 -j ACCEPT
```

![[Pasted image 20250117194452.png]]

#### Puerta RDI (ejercicio):

Politicas (la misma de todas las puertas):

``` bash
iptables -P OUTPUT DROP
iptables -P INPUT DROP
iptables -P FORWARD DROP
```

> Permitido el tráfico en **ambos sentidos** **con origen y destino las redes sat y dmz**

Trafico entre eth0 y eth1:

``` bash
iptables -A FORWARD -i eth0 -s 192.168.112.0/24 -o eth1 -d 192.168.120.0/24 -j ACCEPT
iptables -A FORWARD -i eth1 -s 192.168.120.0/24 -o eth1 -d 192.168.112.0/24 -j ACCEPT
```

(Ya que la configuracion de IP es):

![[Pasted image 20250117195229.png]]

> Permitido el tráfico con **estado ESTABLISHED Y RELATED** aunque no provenga de las redes internas

Trafico ESTABLISHED y RELATED:

``` bash
iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
```

>Permitido el **tráfico saliente por eth****1** (hacia dmz) con estado **NEW** y destino servicios **http/https y consultas DNS** a las IPS **8.8.8.8 y 8.8.4.4**

Necesitaremos 2 normas para el trafico new y 2 para el trafico DNS (una por nameserver):

``` bash
iptables -A FORWARD -m conntrack --ctstate NEW -o eth1 -p tcp --dport 80 -j ACCEPT
iptables -A FORWARD -m conntrack --ctstate NEW -o eth1 -p tcp --dport 443 -j ACCEPT
iptables -A FORWARD -m conntrack  --ctstate NEW -o eth1 -p udp --dport 53 -d 8.8.8.8 -j ACCEPT
iptables -A FORWARD -m conntrack  --ctstate NEW -o eth1 -p udp --dport 53 -d 8.8.4.4 -j ACCEPT
```

>Permitido el tráfico **entrante DNS por eth****1** (desde dmz) desde **8.8.8.8 y 8.8.4.4**

Esta siguiente norma no es necesaria pero podriamos configurar el trafico inverso de DNS con:

``` bash
iptables -A FORWARD -o eth1 -s 8.8.4.4 -p udp --sport 53 -j ACCEPT
iptables -A FORWARD -o eth1 -s 8.8.8.8 -p udp --sport 53 -j ACCEPT
```

Porque no es necesario? Por la norma que configuramos antes:

``` bash
iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
```

Para guardar las normas en este escenario:

``` bash
iptables-save > /etc/iptables/rules.v4
```
#### Puerta RDE (Microtic, ejercicio):

