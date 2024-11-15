Parte de [[Bastionado de Redes e Sistemas]]

Para conectarse a un contenedor de docker activo podemos usar:

``` bash
docker exec -it [nombre] [procesoPrimario]
```

Como por ejemplo

``` bash
docker exec -it webserver bash
```

Si se sigue el comando de inicio del contenedor de los apuntes:

``` bash
docker run -it --name webserver -h webserver nginx bash
```

Una vez dentro del contenedor podemos usar Ctrl+D para cerrar el proceso al que nos hemos conectado mediante exec, si es bash (el proceso primario del contenedor) deteneremos el contenedor.

Un proceso en docker se puede llamar microservicio.

Podemos listar los procesos de docker con

``` bash
docker ps
```

Para eliminar un contenedor:

``` bash
docker stop [nombre]
docker rm [nombre]
```

O usando:

``` bash
docker rm -f [nombre]
```

---
La opción -d en:

``` bash
docker run -d --name webserver -h webserver nginx
```

Inicia el contenedor en segundo plano, sin conectarnos a el.

De usar -p en:

``` bash
docker run -d -p 8080:80 --name webserver -h webserver nginx
```

Se haría un mapeo de puertos de localhost:8080 al contenedor:80.

---
Para listar las imágenes instaladas por docker:

``` bash
docker images
```

---
Para tener persistencia de datos asociados a una imagen (no a un contenedor, es decir crear una nueva imagen a partir del estado de un contenedor) podemos utilizar el comando commit:

``` bash
docker commit [nombre] [imagen]
```

Lo normal seria dar una etiqueta como: 

``` bash
docker commit [nombre] [imagen]:[etiquetaCustom]
```

El comando commit no es trazable con lo que se puede utilizar docker file para mantener documentación de los cambios.

---
Para eliminar una imagen:

``` bash
docker rmi -f [imagen]
```
