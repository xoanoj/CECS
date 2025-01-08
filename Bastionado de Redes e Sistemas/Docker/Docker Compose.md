Parte de [[Docker]] relacionado con [[Básicas de Docker]].


Es una herramienta que permite gestionar los docker container como servicios descritos atrave de un archivo de definición YML

En la práctica usaremos docker compose, no docker-compose

La forma principal de utilizar docker compose sería:

``` shell
docker-compose up -d
```

---
Creación de imágenes:

``` shell
docker-compose build
```

Creación de los servicios:

``` shell
docker-compose create
```

Arranque de los servicios:

``` shell
docker-compose start
```

(el comando up engloba estos pasos)

---

Para eliminar el escenario:

``` shell
docker-compose stop && docker-compose rm
```

(Englobado por down)

Por defecto esto no elimina las imagenes, para eso se usaria:

``` shell
docker-compose down --rmi all
```

o 

``` shell
docker-compose down --rmi [nombreImagen]
```

---

Para ejecutar una terminal en un servicio:

``` shell
docker-compose exec [servicio] bash
```

Recordar que el nombre del servicio NO ES el nombre del contenedor.