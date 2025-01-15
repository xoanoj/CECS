Parte de [[Seguridad Perimetral]]

IPTables es una **heramienta** usada para configurar **Netfiler** (un firewall del kernel de Linux)

Conceptos:
- Regla: Especificacion que permite caracterizar un trafico para determinar si esta permitido no.
- Cadena: Implica el concepto de que un paquete debe pasar por una cadena de checks, dentro de los cuales se les aplican las reglas mencionadas.
- Tablas: Utilizadas para traduccion de direcciones de salida-entrada y entrada-salida. (DNAT (IP publica entrante a privada) y SNAT(IP privada saliente a publica)) (La tecnica de Port Forwarding es un tipo de mecanismo DNAT) (La tabla NAT no es la unica, existen otras para por ejemplo modificar el contenido de los paquetes)

Las tablas contienen cadenas (Por ejemplo, la cadena INPUT de la tabla filter, que contendria reglas para el trafico que entraria a una maquina. Pero puede existir la cadena INPUT en otra tabla, y esa cadena NO seria igual a la de la tabla filter, es decir **una cadena permenece unicamente a una tabla**)

---
## Reglas

Una regla especifica una condicion y una accion.
Las condiciones son criterios que se deben cumplir y las acciones pueden por ejemplo ser bloquear la peticion, permitir su curso o ejecutar un mecanismo SNAT entre otros.

Ejemplo:

![[Pasted image 20250115165822.png]]

-p viene de protocol , --dport es destination port.
Las acciones siempre se escriben en mayuscula, al igual que los nombres de las cadenas.
ACCEPT y DROP tendrian sentido en la tabla filter, y SNAT en la tabla NAT.

Las reglas se pueden:
- Añadir (La regla se añade al final de la cadena) (-A)
- Reemplazar
- Insertar (Se inserta en un lugar existente, moviendo las consiguientes hacia abajo) (-I)
- Eliminar (-D)

(Las reglas tienen un numero de posicion llamado numero de regla)

---
## Cadenas

Las cadenas tienen reglas apiladas en un formato de cola FIFO.
Para cada paquete se va comprobando si se le aplica cada regla de la cadena, es decir, las mas altas se le aplicaran primero.

Las cadenas suelen llevar una politica, que es la accion por defecto para la cadena, la politica predefinida para todas las cadenas es ACCEPT, cuando para un paquete no se aplica ninguna de las reglas de la cadena, se ejecuta la politica.

Se pueden listar todas las cadenas y reglas con:

``` bash
iptables -nL
```

Es comun aplicar una politica DROP, y que sean las reglas las que tienen la responsabilidad de aceptar paquetes (es decir, un modelo whitelist)

En cuanto hay un OK en cualquier regla (en la condicion, no la accion (la cual es irrelevante), el paquete se deja de evaluar.

Es importante mantener a minimos los saltos de verificacion que debe dar un paquete, por eficiencia. (Es decir, la regla con estadisticamente mas coincidencias deberia situarse como la primera)

Algunas cadenas predefinidas:

![[Pasted image 20250115171406.png]]

Cuando un paquete llega a una maquina este llega por INPUT (la IP de destino es la propia maquina) o por FORWARD (la IP de destino es otra maquina (es decir, las reglas de la cadena FORWARD se aplican a las puertas de enlace, y los hosts no deberian tener normas en esta cadena (aunque un host se puede comportar como puerta de enlace)))

![[Pasted image 20250115171506.png]]

---
## Comandos utiles
(Ejemplos)

La tabla por defecto es filter, para especificar otras se debe usar -t

Borrar reglas (de un tabla) y reiniciar contadores:

``` bash
iptables -t filter -F
iptables -t filter -Z
```

Definir politicas por defecto:

``` bash
iptables -t filter -P INPUT DROP
iptables -t filter -P FORWARD DROP
iptables -t filter -P OUTPUT ACCEPT
```

(En nuestros ejemplos(practicas) utilizaremos DROP por defecto)

Permtir el reenvio de todos los paquetes (en transito) que se reciben en un router a traves de la interfaz eth1 para que se envien a traves de eth1

``` bash
iptables -t filter -A FORWARD -i eth0 -o eht1 -j ACCEPT
```

-t = tabla
-A = añadir a cadena
-i = interfaz de entrada
-o = interfaz de salida
-j = accion

Esta regla solo permitiria el trafico en el sentido eht0->eth1, para eth1->eth0 habria que definir otra regla (Tambien serviria con la siguiente norma).

Permitir el reenvio de paquetes entrantes que pertenezcan a "conexiones" ya existentes:

``` bash
iptables -t filter -A FORWARD -i eth1 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
```

(Esta accion permite la comunicacion bidireccional una vez el primer paquete saliera de eth1 en direccion a eth0. Es decir, si el primer paquete de la comunicacion fuera de eth0 a eth1, este se bloquearia)

Otro ejemplo: Permitir el paso de datagramas UDP de entrada dirigidos a una direccion IP de la red interna(10.0.0.10) y a un puerto especifico (80):

``` bash
iptables -t filter -A FORWARD -p udp -d 10.0.0.10 --dport 80 -j ACCEPT
```

(En el enunciado se menciona "Permitir el paso", esto implica inherentemente que estamos hablando de una norma para una puerta de enlace)

Otro ejemplo: Modificar la direccion IP de origen de los datagramas IP al salir de una red privada (10.0.0.0/24) a traves de la interfaz de salida eth0 de un router NAT. Todos los datagramas llevaran la direccion UP publica del router NAT.

``` bash
iptables -t nat -A POSTROUTING -s 10.0.0.0/24 -o eth0 -j SNAT --to-source 200.0.0.1
```
