Parte de [[Hacking Ético]]

Información del sistema

``` bash
cat /etc/issue
cat /etc/*-release
lsb_release -a
uname -a
cat /proc/version
```

Hora del sistema:

``` bash
date
timedatectl
uptime
```

Ver usuarios que se han loggeado etc:

``` bash
last
last reboot
```

Ver paquetes e instalar paquetes a mano:

``` bash
dpkg -l
dpkg
```

Ver tareas programadas:

``` bash
cat /etc/crontab
```

Ver memoria:

``` bash
free -h
```

Ver procesos:

``` bash
ps
ps -f
ps auxx
ps -ef --forest
ps -ef --forest | less

top
htop
btop
```

Redes:

``` bash
ip addr
ip a
ip route
ifconfig
cat /etc/resolv.conf
netstat
netstat -putan

```





