Relacionado con [[Básicas de Docker]], Parte de [[Docker]]


- FROM: Indica la imagen a actualizar.
- LABEL: Añadir etiquetas de metadatos.
- ENV: Definir variables de entorno.
- RUN: Permite ejecutar comandos durante la creación de la imagen resultante (despues usar CMD).
- EXPOSE: Expone los puertos indicados. (No lo mapea a localhost)
- CMD: Permite pasar un comando y sus argumentos. De utilizar un script es recomendable utilizar ENTRYPOINT.
- COPY: Permite introducir archivos en la imagen.


Para construir una imagen a partir de un dockerfile:

``` bash
docker build -t [etiquetaNombre]:[version] [rutaADockerfile] 
```

La version no es necesaria, la ubicacion es . en caso de ser pwd.

Después habrá que iniciar un contenedor, en el ejemplo de clase:

``` bash
docker run -d --name minginx -p 8080:80 minginx:1
```

Donde minginx es el nombre de la imagen y 1 la etiqueta que se le dio en la creación.

