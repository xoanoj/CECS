Parte de [[Seguridad Perimetral]] y [[Cortafuegos con IPTables]]

![[Pasted image 20250120170010.png]]
![[Pasted image 20250120170029.png]]

## Ejercicio:

> El tráfico que atraviesa rdi con destino a la DMZ sea procesado por la cadena TRAF_TO_DMZ

``` bash
iptables -A FORWARD -i eth0 -o eth1 -d 192.168.120.0/24 -j TRAF_TO_DMZ
```

(Todos los paquetes de la cadena forward que pasen de eth0 a eth1 seran enviados a la cadena TRAF_TO_DMZ

>El tráfico con origen las redes internas atravesando rdi hacia la cadena TRAF_FROM_INT

``` bash
iptables -A FORWARD -i eth0 -o eth1 -o 192.168.110.0/24 -j TRAF_FROM_INT
iptables -A FORWARD -i eth0 -o eth1 -o 192.168.111.0/24 -j TRAF_FROM_INT
iptables -A FORWARD -i eth0 -o eth1 -o 192.168.112.0/24 -j
TRAF_FROM_INT
```