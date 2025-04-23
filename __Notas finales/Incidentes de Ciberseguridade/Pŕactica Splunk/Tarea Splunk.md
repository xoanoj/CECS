Parte de [[NF - Incidentes de Ciberseguridade]]

>Estamos en esta tarea frente a un escenario APT en el que vas a asumir la personalidad de Alice Bluebird, la analista que ha sido contratada recientemente para proteger y defender a Wayne Enterprises contra varias formas de ciberataque.
>
>En este escenario (APT), los informes de la siguiente gráfica provienen de su comunidad de usuarios cuando visita el sitio web de Wayne Enterprises, y algunos de los informes referencia a los informes "P01s0n1vy". A modo de aclaración, P01s0n1vy es un grupo de APT que ha apuntado a Wayne Enterprises. Se tiene como objetivo, como Alice, investigar el defacement con centrándonos en la reconstrucción del ataque a través de la Cadena Lockheed Martin Kill. En cuanto se vaya avanzando en la tarea veremos que vamos a trabajar el análisis de un ataque de fuerza bruta.
>
>En todas la preguntas es necesario documentar, no solo con images todas las decisiones tomadas hasta llegar a la respuesta (incluso aquellos casos en los que no se haya llegado a nada y se haya realizado un cambio de rumbo).
>
>Para la realización de la tarea podréis acceder a material de apoyo en lo referente al uso de Splunk (apuntes, tutoriales, consultas de compañeros) pero no al uso directo para obtener respuestas de IA o de blogs de Splunk.

---

>1. ¿Cómo ha evolucionado la cantidad de peticiones al servidor web en el tiempo, por IP origen? (Muestra el gráfico temporal tomando intervalos cada minuto entre las horas del 11 de agosto 00:00 y 00:25).

La consulta es: 

``` bash
index="botsv1" sourcetype="stream:http" | timechart span=1m count by src_ip
```

![[Pasted image 20250423195917.png]]

Podemos ver el flujo de peticiones.

>2. ¿Cuál es la dirección IP probable de alguien del grupo Po1s0n1vy que está escaneando imreallynotbatman.com en busca de vulnerabilidades en aplicaciones web?

Guiandonos por el chart anterior podemos deducir que es 40.80.148.52, ya que ha realizado una cantidad exagerada de peticiones (y según el gráfico anterior lo ha hecho en muy poco tiempo)

Podemos confirmarlo con:

``` bash
index="botsv1" sourcetype="stream:http" site="imreallynotbatman.com" | chart count by src_ip
```

![[Pasted image 20250423200453.png]]

>3. ¿Cuál es la dirección IP del servidor web al que se está atacando?

Mediante:

``` bash
index="botsv1" imreallynotbatman.com src_ip=40.80.148.42 | chart count by dest_ip
```

![[Pasted image 20250423201623.png]]

Es 192.168.250.70

>4. ¿Qué empresa creó el escáner de vulnerabilidades web utilizado por Po1s0n1vy? Escribe el nombre de la empresa. (Por ejemplo, "Microsoft" o "Oracle")

Mediante:

``` bash
index="botsv1" sourcetype="stream:http" src_ip="40.80.148.42" *Scanner*
```

Podemos ver que se trata de el escaner Acunetix de la empresa Invicti Security.

![[Pasted image 20250423201444.png]]

>5. ¿Qué sistema de gestión de contenidos es probable que esté utilizando imreallynotbatman.com?

Mediante:

``` bash
index="botsv1" sourcetype="stream:http" site="imreallynotbatman.com" | chart count by request | sort -count reverse
```

Podemos ver que la mayoría de peticiones van a /joomla/:

![[Pasted image 20250423202658.png]]

Con lo que podemos asumir que el CMS es Joomla.

>6. ¿Cuál es el nombre del archivo que desfiguró el sitio web imreallynotbatman.com? Solo el nombre del archivo con la extensión (por ejemplo, "notepad.exe" o "favicon.ico"). Nota: analiza el tráfico da red en el sentido inverso (de nuestro servidor web hacia una ip externa del atacante).

Sabiendo que la ip del webserver es 192.168.250.70 por apartados anteriores, realizamos esta búsqueda:

``` bash
index="botsv1" sourcetype="stream:http" src_ip="192.168.250.70"
```

Analizando las peticiones:

![[Pasted image 20250423202953.png]]

Vemos que se solicita "poisonivy-is-coming-for-you-batman.jpeg"

>7. Este ataque utilizó DNS dinámico para resolver la IP maliciosa. ¿Cuál es el nombre de dominio completo (FQDN) asociado con este ataque?

Vamos a ver cual es el "site" (nombre de dominio) de destino de la petición al archivo malicioso:

``` bash
index="botsv1" sourcetype="stream:http" src_ip="192.168.250.70" request="GET /poisonivy-is-coming-for-you-batman.jpeg HTTP/1.0" | chart count by site
```

Sacamos esto:

![[Pasted image 20250423203444.png]]

Con lo que la respuesta es:

```
prankglassinebracket.jumpingcrab.com
```

>8. Crea un dashboard en el que se vea en forma de gráfico de secciones las ip que consultan nuestro servidor web. (Se puede obtener haciendo una consulta en una web externa)

Creamos este dashboard:

![[Pasted image 20250423204058.png]]

Que funciona con la query:

``` bash
index="botsv1" sourcetype="stream:http" dest_ip="192.168.250.70" | chart count by src_ip
```

Que ve las peticiones que llegan a nuestro webserver.

>9. ¿Qué dirección IP ha vinculado Po1s0n1vy a los dominios que están preconfigurados para atacar a Wayne Enterprises?

Podemos simplemente cambiar la petición del apartado 7 y en vez de ver el site destino, ver el dest_ip:

``` bash
index="botsv1" sourcetype="stream:http" src_ip="192.168.250.70" request="GET /poisonivy-is-coming-for-you-batman.jpeg HTTP/1.0" | chart count by dest_ip
```

![[Pasted image 20250423205220.png]]

La IP es 23.22.63.114

>10. Según los datos recopilados de este ataque y fuentes comunes de inteligencia de código abierto para nombres de dominio, ¿cuál es la dirección de correo electrónico más probable asociada con el grupo APT Po1s0n1vy?

Mediante el dork de Google:

``` bash
intext:Po1s0n1vy email
```

Encontramos en AlienVault:

https://otx.alienvault.com/indicator/email/LILLIAN.ROSE@PO1S0N1VY.COM

Con lo que sacamos que el correo podría ser:

lillian.rose@po1s0n1vy.com


>11. ¿Qué URIs parecen relacionadas con autenticación?

PROVISIONAL

``` bash
index="botsv1" sourcetype="stream:http" uri="*auth*" | chart count by uri
```

![[Pasted image 20250423212124.png]]

>12. ¿Qué dirección IP probablemente está intentando un ataque de fuerza bruta contra imreallynotbatman.com?

Podemos buscar por peticiones POST ya que están asociadas a formularios y así vemos que lasI IPs 40.80.148.42 y 23.22.63.114 tienen muchas peticiones.

Utilice la petición:

``` bash
index="botsv1" sourcetype="stream:http" site="imreallynotbatman.com" http_method="POST" | chart count by src_ip
```


Ahora viendo las peticiones que hacen en detalle podemos ver que   está realizando peticiones similares a username=admin&task=login&return=aW5kZXgucGhw&option=com_login&passwd=rock&4a40c518220c1993f0e02dc4712c5794=1

Con lo que la IP es 23.22.63.114

>13. ¿Cuál es el nombre del archivo ejecutable subido por Po1s0n1vy? Por favor, incluye la extensión del archivo. (Por ejemplo, "notepad.exe" o "favicon.ico")

Mediante:

``` bash
index="botsv1" sourcetype="stream:http" "*.exe" dest_ip="192.168.250.70" src_ip="40.80.148.42" | chart count by uri
```



>14. ¿Cuál fue la primera contraseña de fuerza bruta utilizada? (Puedes investigar sobre el comando transaction)



>15. ¿Cuál fue la contraseña correcta para acceder como administrador al sistema de gestión de contenidos que ejecuta "imreallynotbatman.com"?



>16. ¿Cuál fue la longitud promedio de las contraseñas utilizadas en el intento de fuerza bruta? (Redondea al número entero más cercano. Por ejemplo, "5" y no "5.23213")



>17. ¿Cuántos segundos transcurrieron entre el escaneo de fuerza bruta que identificó la contraseña correcta y el inicio de sesión comprometido? Redondea a 2 decimales.



>18. ¿Cuántas contraseñas únicas se intentaron en el ataque de fuerza bruta?



>19. Escribe una regla sigma que compruebe si el Windows Security Event ID (EventID) es 4656 o 4663. (Es suficiente con poner solo los campos obligatorios).



>20. Dada la siguiente consulta en Splunk escribe la regla sigma equivalente source="WinEventLog:*" AND ((Image="*\\excel.exe" OR Image="*\\mspub.exe" OR Image="*\\onenote.exe" OR Image="*\\onenoteim.exe" OR Image="*\\outlook.exe" OR Image="*\\powerpnt.exe" OR Image="*\\winword.exe") AND ImageLoaded="*\\kerberos.dll")


