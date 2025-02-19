
Practica de [[Configuracion de dispositivos y sistemas]]

>Empezamos realizando un ataque MITM (Man In The Middle) con ettercap para capturar el tráfico que se transmite entre wordpress y mysql. En este caso como no hay ningún tipo de configuración SSL en la comunicación entre wordpress y mysql el tráfico viaja en claro y por tanto es susceptible de interceptación y análisis.
>
>El ataque consistirá en utilizar ARP poisoning para redirigir el tráfico que la víctima, en este caso wordpress, envía al mysql, para que pase por el atacante y de este modo pueda ser analizado y estudiado (o incluso modificado). Una vez que los paquetes interceptados estén en el atacante (host hack) éste puede almacenarlos y estudiarlos para posteriores ataques. Para que el ataque tenga éxito y no interrumpa el servicio, los paquetes deberán ser reenviados a su legítimo destinatario, mysql, para que el ataque no sea detectado y el atacante pase desapercibido

![[Pasted image 20250219170031.png]]

Lanzamos el ataque desde hack:

``` bash
ettercap -T -o -M arp /192.168.50.2// /192.168.50.100//3306
```

Donde:
- -T: interfaz en modo texto
- -o: solo realiza ataque MITM, no captura tráfico
- -M arp: Tipo de ataque, en este caso envenenamiento ARP, desde el primer target hacia el segundo, es decir, captura el tráfico entre wordpres y mysql
- Los targets, objetivos o víctimas, sobre los que se realiza el ataque. Cuanto más específicos sean éstos más silencioso será el ataque. En este caso serán el wordpress y el mysql (en el puerto 3306)

Apuntamos la configuracion de red del atacente:

![[Pasted image 20250219170510.png]]

Ahora si vemos la tabla ARP de wordpress:

![[Pasted image 20250219170822.png]]

Vemos que la MAC de hack aparece tambien como la de mysql

Ahora con otra terminal dentro del atacante podemos dumpear el tráfico con:

``` bash
tcpdump -i eth0 -s 65535 -w /tmp/mitm.pcap
```

Donde:
- -i: La interfaz de captura
- -w: Precede al archivo de volcado del tráfico
- -s: Opción necesaria para evitar el truncado de paquetes