Parte de [[Enumeracion de Servicios]]

Es un protocolo donde la informacion se trasmite en claro, para poder enumerar FTP se requiere un usuario valido en el servicio, no obstante a veces existe el usuario Anonymous

En el caso de metasploitable2, podemos:

``` bash
ftp 192.168.56.102
Connected to 192.168.56.102.
220 (vsFTPd 2.3.4)
Name (192.168.56.102:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> 
```

Comandos de ftp serian:
- help: ver todos los comandos
- help {comando}: ver que hace un comando
- pwd: ver directorio
- dir / ls: ver directorio
- !: ejecutar comandos en la maquina local (!ls para listar la maquina local)
- put: intentar subir ficheros

Si estamos en una situacion en la que estamos en un carpeta sin nada, significa que podriamos estar enjaulados, podemos intentar escapar usando cd con rutas relativas o absolutas.