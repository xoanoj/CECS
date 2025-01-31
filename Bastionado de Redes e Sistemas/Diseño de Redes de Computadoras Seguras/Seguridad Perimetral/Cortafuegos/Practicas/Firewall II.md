Practica de [[Cortafuegos con IPTables]]

![[Pasted image 20250120161329.png]]
![[Pasted image 20250120161352.png]]

## Reglas de Host:

### Conexiones smtp e imap a google

``` bash
iptables -A OUTPUT -p tcp -d smtp.gmail.com -m multiport --dports 587,465 -m conntrack --ctstate NEW -j ACCEPT
iptables -A OUTPUT -p tcp -d imap.gmail.com --dport 993 -m conntrack --ctstate NEW -j ACCEPT
```

(Esto parte de que las reglas de la practica 1 estan establecidas)
(Por ejemplo el -d requeriria resolver nombres, en este caso se utiliza la norma configurada en el ejercicio 1 para DNS. Si la IP no fuera a cambiar se podrian hacer resoluciones locales mediante /etc/hosts)
### Conexiones ICMP

Para todos los hosts:

``` bash
iptables -I OUTPUT -p icmp -j ACCEPT
```

para los hosts de adm:

``` bash
iptables -I INPUT 1 -p icmp -s 192.168.110.0/24 -j ACCEPT
iptables -I INPUT 2 -p icmp -s 192.168.112.0/24 -j ACCEPT
```

(-I sin valor añade la regla al final de la pila)

para los hosts de dir:

``` bash
iptables -I INPUT 1 -p icmp -s 192.168.111.0/24 -j ACCEPT
iptables -I INPUT 2 -p icmp -s 192.168.112.0/24 -j ACCEPT
```

para los hosts de sat:

``` bash
iptables -I INPUT 1 -p icmp -s 192.168.112.0/24 -j ACCEPT
```

## Reglas de puertas de enlace

### Puerta RL

#### Permitir trafico smtp e imap:

``` bash
iptables -A FORWARD -p tcp -o eth2 -m multiport --dports 587,465 -m conntrack --ctstate NEW -j ACCEPT
iptables -A FORWARD -p tcp -o eth2 --dport 993 -m conntrack --ctstate NEW -j ACCEPT
```

#### Permitir (pasar) trafico ICMP

``` bash
iptables -A FORWARD -p icmp -j ACCEPT
```

### Puerta RDI (ejercicio)

#### Permitir trafico SMTP e IMAP

``` bash
iptables -A FORWARD -p tcp -o eth1 -m multiport --dports 587,465 -m conntrack --ctstate NEW -j ACCEPT
iptables -A FORWARD -p tcp -o eth1 --dport 993 -m conntrack --ctstate NEW -j ACCEPT
```

Esencialmente es lo mismo, solo hay que tener en cuenta que interfaces son las de salida para este tipo de resoluciones:

![[Pasted image 20250120164724.png]]

(El trafico no se origina de RL obviamente, solo es una abstraccion de la generacion del trafico en las redes de usuarios)

(No hay que tener en cuenta el caso de SAT ya que utiliza eth0-eth1 para estas consultas al estar directamente conectado a RDI)
#### Permitir pasar el trafico ICMP

``` bash
iptables -A FORWARD -p icmp -j ACCEPT
```

### Puerta RDE (ejercicio)

#### Permitir trafico SMTP e IMAP

![[Pasted image 20250120164152.png]]
![[Pasted image 20250120164254.png]]
![[Pasted image 20250120164313.png]]

#### Permitir pasar el trafico ICMP

![[Pasted image 20250120164343.png]]
![[Pasted image 20250120164419.png]]