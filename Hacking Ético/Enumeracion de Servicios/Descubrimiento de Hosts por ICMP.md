Parte de [[Enumeracion de Servicios]] e [[Info Gathering]]

ICMP tiene varios tipos, entre ellos:
- Saludo
- Respuesta a saludo
- Paquete descartado
- Inalcanzable

Hay tipos de mensaje ICMP que regularmente deberian ser bloqueados.

En el descubrimiento de hosts se utiliza el ICMP Echo Request - ICMP Echo Reply, tambien lo utiliza el comando ping y el protocolo ping sweep (-sn) de nmap.

Una falta de respuesta a un ICMP Echo Request no necesariamente implica que ese sistema no existe.

Tambien se puede intentar averiguar el tipo de SO del host objetivo segun el TTL de su ICMP Echo Reply:
- 64 : Linux
- 128 : Windows

En redes locales se puede utilizar el [[ARP Sweep]]

