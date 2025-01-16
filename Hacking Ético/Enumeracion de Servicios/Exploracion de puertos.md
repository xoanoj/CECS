Tecnica de [[Enumeracion de Servicios]]

Tipicamente mediante nmap

Para descubrir si un PC esta activo podemos aprovechar el TCP 3WHandshake para ver si a nuestro paquete SYN se responde con un SYN/ACK o con RST.

Si se responde con SYN/ACK o RST sabemos que el PC esta activo, si responde con SYN/ACK ademas sabemos que el puerto esta abierto.

Podemos hacerlo a mano con netcat:

``` bash
nc -nzv [IP] [puerto]
```

Nmap puede sacar el estado de los puertos del tipo:
- Open
- Closed
- Filtered (Cuando se deduce que hay un firewall)
- Unfiltered (Producido solo por el escaneo ACK, cuando nmap no es capaz de interpretar la respuesta)
- open|filtered (Solo en escaneos NULL, FIN, UDP y Xmas, significa abierto o con firewall pero no determinable)
- closed|filtered (Ocurre solo con escaneos Idle)

Ejemplo de ping sweep con nmap

``` bash
sudo nmap -sn [red]
```

Si nmap detecta que la red a escanear es la red local, utilizara un barrido ARPing en lugar de ICMP. Para forzarlo a usar ICMP seria con la flag --send-ip.

Por defecto nmap (en un ping sweep) enviara un ICMP echo request, despues SYN a p443, despues ACK a p80 y finalmente ICMP Time Stamp. Si en vez de con sudo, lo ejecutamos con un usuario normal enviara solo SYN a p443 y ACK a p80

En vez de a una red el ping sweep tambien se puede hacer a solo un equipo. Podemos pedir que nmap justifique sus resultados con --reason

Para un escaneo de SYN (Stealth) un ejemplo tipico para casos CTF (es decir, escaneos muy rapidos) seria:

``` bash
sudo nmap -sS -T5 -p- --min-rate=100000 [ip] --reason
```

El ejemplo de clase de regal seria:

``` bash
sudo nmap -n -Pn -sS [ip]
```

(Aunque con este ejemplo no se ven todos los puertos)

Para asginar puertos a asignar:
- -p- o -p 0-65335 para todos los puertos
- -p \[puerto\] Un unico puerto
- -p \[puerto\],\[puerto\],... Para varios puertos

Existe el analisis de los 65335 puertos UDP pero es muy muy lento y por ello no se hace en muchos casos a pesar de que podria haber servicios unicos. Ademas, por como funciona UDP, los resultados no son muy concluyentes (ya que no necesariamente tiene que responder aunqe el puerto este abierto).

El barrido de puertos UDP se haria:

``` bash
sudo nmap -n -Pn -p- -sU [ip]
```

Tambien se puede hacer un TCP connect scan con -sT, pero tarda mas y genera mucho mas ruido.

La deteccion de versiones se hace con -sV, ejemplo de clase:

``` bash
sudo nmap -n -Pn -sV -p [puertos] [ip]
```

Para la deteccion del sistema operativo se puede usar -O (funciona de forma inconsistente) (se recomienda poner un puerto que esta abierto y otro que esta cerrado para que la deteccion funcione mejor)

---

Utilizar -A = -sC -sV -O