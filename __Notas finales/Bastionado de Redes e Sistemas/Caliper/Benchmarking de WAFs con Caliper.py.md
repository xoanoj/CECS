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