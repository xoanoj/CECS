Practica de [[Diseño de Redes de Computadoras Seguras]] y [[VPN IPSec]]

![[Pasted image 20250129170304.png]]
![[Pasted image 20250129170737.png]]

---

Configuramos left:

Modificando /etc/ipsec.conf:

![[Pasted image 20250129172056.png]]

![[Pasted image 20250129172301.png]]

Ahora configuramos right:

![[Pasted image 20250129172509.png]]

![[Pasted image 20250129172611.png]]

---

Ahora arrancamos la conexion IPSec en ambos equipos con:

```
ipsec start
```

Otros comandos utiles

```
ipsec stop
ipsec status
ipsec statusall
```

---

Una vez iniciado, ejecutamos en right:

```
watch ipsec statusall
```

Y desde left, ejecutamos un ping a right:

![[Pasted image 20250129173039.png]]

Vemos como se genera la SA

---

Analizando el trafico:

Buscamos la interfaz correcta con:

```
docker network ls
```

![[Pasted image 20250129173315.png]]

Y podemos ver los paquetes ICMP echo resquest e ICMP echo reply bajo el protocolo ESP:

![[Pasted image 20250129173459.png]]