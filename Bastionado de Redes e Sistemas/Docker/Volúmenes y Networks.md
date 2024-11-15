Relacionado con [[Básicas de Docker]], Parte de [[Bastionado de Redes e Sistemas]]

Los volúmenes son unidades de almacenamiento que pueden conectarse a un container. 

Se pueden gestionar utilizando volúmenes locales (internos de docker, son archivos que se conectan a docker en puntos de montaje) o montando directorios del host en el contenedor (no es recomendable)

---
### Volúmenes Locales

Se pueden definir con docker run con la flag -v, se les debe dar una etiqueta, como en el ejemplo:

``` sh
docker run -d -p 80:80 --name nginx -v nginxvol:/var/www nginx:latest
```

Podemos listar volúmenes de docker con:

``` sh
docker volume list
```

E inpeccionar volumenes con:

``` sh
docker volume inspect nginxvol
```

o con:

``` sh
docker inspect [nombreContainer] | grep [nombreVolumen]
```

---
### Montaje de directorios del host

Se haría con -v, como en:

``` shell
docker run -d -p 80:80 --name nginx -v ~/www:/var/www nginx:latest
```


---

## Gestión de Networks

Docker tiene 3 redes por defecto: Host, None y bridge.

Las redes se pueden listar mediante:

``` shell
docker network ls
```

Para crear una red :

``` shell
docker network create --driver [bridge/host/none] [nombreRed]
```

Para lanzar un container conectado a una red se utiliza el parámetro --network:

``` shell
docker run -it --name [nombre] --network=[nombreRed] [images]
```

(Para salir de un proceso sin cerrarlo Ctrl+P -> Q)

(Para conectarse al proceso PID1 del containser usar 
``` shell
docker attach [nombre]
```
)

Si se crean dos contenedores con la misma red tendran un protocolo DHCP automático y un resolutos de DNS por el nombre de container (ej: container1 y container2 pueden hacer ping -c 1 contaner1)

