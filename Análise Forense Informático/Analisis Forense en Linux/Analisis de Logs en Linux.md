Parte de [[Analisis Forense en Linux]] y [[Artefactos Linux]]

Generalmente estan en /var/log

Suelen ser ficheros de texto plano

Historial de inicios de sesion con el comando last -i (muestra IPs ) o -f que permite utilizar ficheros que no sean /var/log/wtmp

Los inicios de sesion fallidos suelen estar en /var/log/btmp, y el comando seria lasb (no last.)

El ultimo inicio de sesion estara en /var/log/lastlog

La opcion -u permite sacas info de un usuario completo y la opcion -s especifica dias.

Tambien tenemos el Syslog, es manejado por el demonio rsyslogd. Es el principal servicio de lgos en Linux. Es atacable por medidas antiforense ya que por defecta envia datos a ficheros de texto locales. Tambien se puede enviar a SIEMS.

![[Pasted image 20250331212521.png]]

Las fuentes son:

![[Pasted image 20250331212548.png]]

Tambien tenemos los logs de webservers, que tienden a ser muy vulnerables.

![[Pasted image 20250331212616.png]]
