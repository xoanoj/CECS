Parte de [[NF - Bastionado de Redes e Sistemas]], Proyecto final de Bastionado.

## Contexto

Datos de 2022 muestran que aproximadamente el 74% de las organizaciones utilizaron Cortafuegos de Aplicaciones Web (WAF, por sus siglas en inglés) como medida de ciberseguridad. Sin embargo, el mismo estudio reveló que el 14% de las organizaciones usaron los WAF en lugar de corregir las vulnerabilidades presentes en sus sitemas, mientras que el 36% los empleó como una protección temporal antes de implementar los parches.

A partir de estos datos, podemos concluir que, desde el punto de vista de la auditoría, no es correcto asumir que una aplicación web es segura únicamente por la presencia de un WAF. Una vulnerabilidad puede existir independientemente de que haya un WAF que dificulte o impida su ejecución.

Esto significa que tanto los pentesters como los administradores de sistemas deben conocer a fondo los límites y debilidades de un WAF, para asegurar adecuadamente la aplicación web y evitar que un fallo no sea descubierto debido a la intervención del WAF.

## Objetivos

El desarrollo de la herramienta **Caliper** tiene como objetivo ofrecer una forma sencilla de identificar posibles vectores de evasión para un WAF.

La herramienta está desarrollada en Python 3 debido a su facilidad para manejar peticiones HTTP/HTTPS y su capacidad para crear aplicaciones modulares y fácilmente ampliables.

Caliper cuenta con dos modos de uso, definidos en el programa como "Mode":

- **Modo "VEC"** (Vectorización): Este modo espera que el usuario proporcione una petición bloqueada. A partir de un segmento específico (el cual corresponde a una parte de la cadena de la petición), el sistema busca formas de modificar la cadena o la petición para que, aún conteniendo dicho segmento, la petición sea aceptada por el WAF.

- **Modo "EVAL"** (Evaluación): De manera simplificada, este modo funciona como un fuzzer o sonda HTTP, similar a HTTPX de ProjectDiscovery. Utiliza diccionarios con payloads para vulnerabilidades como XSS, SQLi y LFI, los cuales incorporan diversas técnicas de evasión. Estos payloads se envían con el objetivo de identificar qué bloquea el WAF. Actualmente, este modo solo es compatible con el verbo HTTP GET.

Asimismo, el modo "VEC" cuenta con distintos tipos de vectorización de la petición:

- **Junk Data Injection (JDI)**: Esta técnica, popularizada por el plugin de Burp Suite **nowafpls** ([https://github.com/assetnote/nowafpls](https://github.com/assetnote/nowafpls)), consiste en insertar datos "basura" (junk data) en una petición para evadir el WAF. Aunque el plugin ofrece algunas pautas sobre la cantidad de datos que se deben insertar según el firewall implementado, no siempre es posible determinar la cantidad exacta de datos necesarios para evitar un firewall de manera exitosa. **Caliper** facilita este proceso, proporcionando una forma simplificada de descubrir la cantidad de datos que se pueden insertar para permitir que una carga útil previamente bloqueada pase a través del WAF. Además, este vector también convierte a la herramienta en un **estrés-tester** de red. Un ejemplo de ejecución de este comando sería:

- **Origin Header Tampering (OHT)**: Los WAFs pueden ser engañados para no inspeccionar paquetes si se modifican cabeceras HTTP como X-Originating-IP, X-Forwarded-For, X-Remote-IP, o X-Remote-Addr y se les asignan valores locales, como 127.0.0.1 o 0.0.0.0, especialmente si el WAF confía en estos valores provenientes de proxies upstream.

- **HTTP Verb Swap (HVS)**: Algunos WAFs no evalúan solicitudes que usan el método HTTP PUT, aunque podrían hacerlo si la misma solicitud utilizara el método POST. Este cambio de verbo HTTP puede permitir que una petición pase sin ser detectada.

- **Random Payload Capitalization (RPC)**: Los payloads que no son sensibles a mayúsculas y minúsculas (como aquellos que explotan vulnerabilidades de SQLi) pueden a veces evadir la detección de WAFs si se capitalizan de manera aleatoria. Este enfoque puede evitar que los WAFs, que dependen de expresiones regulares para detectar patrones, bloqueen el tráfico malicioso.

## Consideraciones

Al trabajar con Caliper, es importante tener en cuenta varios aspectos clave:

- **Uso de servidor de interceptación**: Se asume que se emplea un servidor de interceptación para obtener las peticiones en texto plano para el modo "VEC". Este servidor también será necesario para modificar las peticiones para explotación cuando se descubran posibles vectores de evasión.
 
- **Objetivo de la herramienta**: Caliper no tiene como objetivo verificar la ejecución de un payload, sino centrarse exclusivamente en la evasión del WAF. La herramienta se limita a analizar las respuestas HTTP, ya sea a través de los códigos de respuesta o, si la opción `--match-content` está activada, mediante el contenido del cuerpo de la respuesta.

---
## Instalación de la herramienta

La herramienta es de código abierto y está disponible en el siguiente enlace:

- [https://github.com/XoanOuteiro/caliper](https://github.com/XoanOuteiro/caliper)

Al instalar y utilizar Caliper, el usuario acepta implícitamente una serie de normativas éticas y legales, las cuales se pueden consultar en:

- [https://github.com/XoanOuteiro/caliper?tab=readme-ov-file#legal--ethical-considerations](https://github.com/XoanOuteiro/caliper?tab=readme-ov-file#legal--ethical-considerations)

Estas normativas especifican los casos de uso aceptables y dejan claro que la responsabilidad del uso de la herramienta recae exclusivamente en el usuario final, nunca en el desarrollador.

La instalación se simplifica mediante un script compatible con sistemas basados en Debian o Arch, que instala las dependencias de Python de manera global en el sistema. Para aquellos usuarios que prefieran utilizar entornos virtuales, también se incluye un archivo `requirements.txt`.

El proceso de instalación es el siguiente:

``` bash
git clone https://github.com/XoanOuteiro/caliper # Clonación del repositorio
cd caliper # Cambio a la carpeta de la herramienta
chmod +x install.sh && ./install.sh # Instalación de dependencias
```

Los usuarios de Fedora o de cualquier otra distribución de Linux que no utilice los gestores APT o PACMAN deberán instalar las dependencias a través de PIP.

---

## Preparación del Entorno de Pruebas

Para la demostración de concepto de la herramienta, desplegaré dos laboratorios basados en **Docker**, disponibles en el siguiente repositorio:

- [https://github.com/XoanOuteiro/WAF_Labs](https://github.com/XoanOuteiro/WAF_Labs)


Utilizaremos específicamente:

- **Laboratorio "XSS"**: para evidenciar el funcionamiento en **modo evaluación**.

- **Laboratorio "DATAI"**: para ilustrar el **modo de vectorización**, en particular el módulo JDI.

### Puesta en marcha del laboratorio XSS

Ejecuta los siguientes comandos:

``` bash
git clone https://github.com/XoanOuteiro/WAF_Labs # Clonado del repositorio
cd ./WAF_Labs/XSS # Entrada al directorio de trabajo
make build && make run # Inicio del laboratorio
```

Para detener y limpiar el escenario:

``` bash 
make clean
```

De forma análoga, para desplegar el laboratorio DATAI:

``` bash
git clone https://github.com/XoanOuteiro/WAF_Labs # Clonado del repositorio
cd ./WAF_Labs/DATAI # Entrada al directorio de trabajo
make up # Inicio del laboratorio
```

Y para eliminar el laboratorio:

``` bash
make down
```

---

## PoC #1 - Descubriendo Payloads de XSS Válidos en WAFs Basados en RegEx

![[xss_setup.png]]

En la imagen podemos observar la estructura básica del laboratorio:

- Un proxy NGINX encargado del filtrado por RegEx de las peticiones (127.0.0.1:80).
- Una aplicación web escrita en Flask, vulnerable a HTMLi y XSS (127.0.0.1:5000).

Accederemos a la web a través de `http://127.0.0.1`, lo que dirige nuestras peticiones al proxy NGINX por defecto.

![[initial_web_xss.png]]

La web es sencilla y contiene un parámetro oculto, el cual típicamente se descubriría mediante fuzzing; sin embargo, en este caso omitimos ese paso. El parámetro es `input` y refleja el contenido de la siguiente manera::

![[reflection_xss_test.png]]

Probamos a ejecutar un payload clásico de XSS para verificar si el sistema lo ejecuta:

![[forbidden.png]]

Como podemos observar, NGINX está bloqueando las peticiones que se asemejan a ataques XSS típicos.

Existen múltiples herramientas para realizar fuzzing de XSS. En este caso, **Caliper** incluye el módulo `EVAL`, que viene con un diccionario de sintaxis HTML para facilitar esta tarea dentro de la aplicación. A continuación, vemos el menú de ayuda del modo evaluación, donde podemos observar cómo estructurar nuestro comando:

![[EVAL_HELP_MENU.png]]

Los argumentos del módulo de evaluación son bastante sencillos:

- `-u/--url`: Especifica la URL objetivo.

- `-p/--parameter`: Indica el parámetro de la URL que se evaluará.

- `-st/--syntax-type`: Define el diccionario a utilizar.

Entonces un comando para este caso concreto seria:

``` bash
python3 caliper.py EVAL --url "http://127.0.0.1?input=test" --parameter input --syntax-type HTML
```

La ejecución:

![[eval_run.mp4]]

**Nota:** La velocidad está limitada artificialmente a 10 peticiones por segundo. Si se elimina esta restricción, la aplicación podría realizar entre 100 y 800 peticiones por segundo.

Los resultados se agrupan por código de respuesta. Tres payloads han logrado evadir el firewall:

``` bash
[!] RESULT -> Response Code 200:
<img src=x onerror=eval(atob('YWxlcnQoMSk=')), <svg/onload=alert(1)//, " autofocus onfocus=alert(1)
```

Aunque no podemos asegurar que estos payloads funcionen, sabemos con certeza que el firewall no los bloquea. Al probarlos, observamos que el segundo payload ejecuta un script válido, demostrando las vulnerabilidades HTMLi y RXSS en la web:

![[RXSS.png]]

Finalmente podemos ver como funciona el filtro RegEx de NGINX:

``` bash
<script.*?>.*?</script>
<img.*?onerror=.*?>
```

Este filtro es extremadamente simple y bloquea dos de los tipos de payloads más comunes. En nuestro caso, el payload `<svg/onload=alert(1)//` logró evadir el filtro, ya que no utiliza etiquetas de tipo `script` ni `img`, además de no cerrar la etiqueta de manera convencional, lo que impediría su detección por un WAF con un filtrado insuficiente.

---

## PoC #2 - Descubriendo los Límites de un WAF

El modo Evaluación de Caliper es extremadamente sencillo y está diseñado para realizar pruebas rápidas sobre un WAF en el que se esté trabajando. Esta funcionalidad es básica, ya que se limita al uso del método HTTP GET para probar diferentes payloads.

Sin embargo, el objetivo de Caliper no es simplemente probar qué payloads funcionan, sino identificar posibles fallos en la configuración de un WAF. Para ello, se utiliza el **modo VEC** (Vectorización), que se centra en modificar el vector de ataque mediante distintas técnicas de evasión.

### Enfoque del PoC

En este caso, no utilizaremos múltiples payloads, sino que, a partir de un único payload y una petición HTTP en texto plano, intentaremos descubrir cómo modificar dicha petición para que el WAF permita que sea interpretada correctamente por la aplicación web.

Para ilustrar este concepto, utilizaremos el **laboratorio DATAI**, el cual simula una situación relativamente realista:

> Estamos ante un panel de control para administradores, en el que se realiza una petición con un **ID de usuario** y se recibe en respuesta información relacionada con ese usuario.
> 
> Dado que los desarrolladores son conscientes de la vulnerabilidad **SQLi** (inyección de SQL), implementaron una protección utilizando un filtro RegEx para bloquear las peticiones que contengan sintaxis SQL. Sin embargo, este enfoque es costoso en términos de recursos, ya que el filtro debe analizar el paquete completo para detectar patrones de SQL.
> 
> Los desarrolladores, para mitigar este coste, decidieron aplicar una estrategia: **ignorar la comparación de RegEx en peticiones que superen un tamaño específico**, determinado por un umbral X cercano a los 10 KB. Este tamaño no es conocido por un atacante, pero crea una oportunidad para evadir el filtro.

### Técnica de Evasión: Junk Data Injection (JDI)

Para atacar esta aplicación, utilizaremos la técnica conocida como **Junk Data Injection (JDI)**, que consiste en inyectar grandes cantidades de "datos basura" (comentarios, por ejemplo) en el cuerpo de la petición HTTP con el objetivo de aumentar su tamaño. Esta técnica puede tener uno de dos comportamientos en un WAF vulnerable a ella:

1. **Ignorar peticiones que superen el umbral de tamaño X**: Este es el comportamiento que buscamos en este caso, ya que permite que la solicitud pase sin ser evaluada por el filtro RegEx.

2. **Evaluar solo peticiones hasta el tamaño X**: Este comportamiento es más común en soluciones de Firewall como servicio (FaaS), donde solo se analiza el tráfico hasta un cierto límite.

