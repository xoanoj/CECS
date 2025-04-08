Parte de [[Hacking Ético]]

Ejemplificado en el contexto de Pivoting local mediante Port-Forwarding en [[Maquina - Dump]]

Para montar el laboratorio de movimiento laterial usaremos Vagrant.

Podemos levantar el escenario mediante:

``` bash
vagrant up
```

Ahora veremos el port forwarding mediante SSH, si existe un servidor SSH en la máquina de pivotaje entonces no suele hacer falta ningun tipo de herramienta extra.

![[Pasted image 20250408194418.png]]

Desde auditor podemos crear un tunel SSH para acceder a msql mediante:

``` bash
ssh -L 127.0.0.1:3306:127.0.0.1:3306 vagrant@192.168.56.240 -N
```

O simplificado mediante:

``` bash
ssh -L 3306:127.0.0.1:3306 vagrant@192.168.56.240 -N
```

Nos pedira autenticarnos y despues el tunel quedará configurado.

Ahora desde otra shell de auditor podremos utilizar 127.0.0.1:3306 como si fuera 127.0.0.1:3306 en pivot:

``` bash
vagrant@auditor:~$ sudo netstat -putan

Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      2224/ssh            
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      816/sshd: /usr/sbin 
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      615/systemd-resolve 
tcp        0     36 10.0.2.15:22            10.0.2.2:38344          ESTABLISHED 2225/sshd: vagrant  
tcp        0      0 192.168.56.230:33930    192.168.56.240:22       ESTABLISHED 2224/ssh            
tcp        0      0 10.0.2.15:22            10.0.2.2:33974          ESTABLISHED 2162/sshd: vagrant  
tcp6       0      0 :::22                   :::*                    LISTEN      816/sshd: /usr/sbin 
tcp6       0      0 ::1:3306                :::*                    LISTEN      2224/ssh            
udp        0      0 127.0.0.53:53           0.0.0.0:*                           615/systemd-resolve 
udp        0      0 10.0.2.15:68            0.0.0.0:*                           1320/systemd-networ 

```

Aparece que el proceso a la escucha en el puerto 3306 es ssh, esto se debe a que es un tunel SSH, pero este lleva a un servicio msql.

La conexion ESTABLISHED es la conexion con el servidor SSH de la maquina pivot.

Podemos usar msql client (La contraseña es Abc123..):

``` bash
vagrant@auditor:~$ mysql -u root -p -h 127.0.0.1
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 15
Server version: 8.0.41-0ubuntu0.22.04.1 (Ubuntu)

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
```

---

Ahora queremos acceder al servicio web(57.230) de server desde auditor.

Desde auditor:

``` bash
ssh -L 8080:192.162.57.230:80 vagrant@192.168.56.240 -N
```

Ahora auditor tiene el puerto 8080 a la escucha. Podemos usar curl contra el para conectarnos mediant HTTP.

---

Lo mismo con chisel. Auditor tiene el cliente y pivot el server.

>"En la maquina auditor debemos levantar un puerto local que vamos a mapear al puerto web de server mediante un tunel"

En la maquina Pivot:

``` bash
./chisel server -p 9999 -v --host 192.168.56.240
```

(El -v es para que sea verbose, La ip es para establecer la direccion del pivoting, es decir, el tráfico entrara solo de la red de la ip dada)

Y ahora desde auditor hacemos:

``` bash
./chisel client 192.168.56.240:9999 8080:192.168.57.230:80
```

Con lo que ya tenemos el tunel establecido, y 127.0.0.1:8080 de auditor redirige a 192.168.57.230:80 (es decir el puerto web de server)

---

Ahora veremos el port-forwarding remoto con SSH.

Se puede utilizar para obtener reverse shells de equipos que no se pueden comunicar con nosotros.

![[Pasted image 20250408202929.png]]

La idea es que si un servidor publico tunelea hacia un servidor inaccesible, podemos utilizar el servidor publico para acceder al privado.

Ahora mismo, si intentamos lanzar una revershell desde server hasta auditor, no podemos ya que la red es inalcanzable. 

Para seguir esta técnica necesitaremos que el servidor SSH este malconfigurado o que seamos root. En concreto necesitamos que /etc/ssh/shhd_config tenga la directiva GatewayPorts este configurada como yes. (Para esta práctica aplicamos esta directiva y reiniciamos el servidor ssh)

Desde auditor hacemos:

``` bash
ssh -R 192.168.57.240:4444:localhost:4444 vagrant@192.168.56.240 -N
```

Es decir, estamos diciendo a la maquina pivot que exponga su puerto 4444 y que redirija su trafico entrante por el tunel ssh al puerto local 4444 que corre en auditor. Tal que asi:

![[Pasted image 20250408204349.png]]

---

Haciendo lo mismo con chisel:

En pivot tenemos que lanzar un server:

``` bash
./chisel server -p 9999 --host 192.168.56.240 --reverse -v
```

Y en auditor:

``` bash
./chisel client 192.168.56.240:9999 R:192.168.57.240:4444:127.0.0.1:4444
```


