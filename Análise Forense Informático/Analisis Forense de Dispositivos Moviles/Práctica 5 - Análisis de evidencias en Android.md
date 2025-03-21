Parte de [[Analisis Forense de Dispositivos Moviles]]
## Ejercicios

>En esta tarea deberás de seguir con el análisis de las evidencias adquiridas a los tres teléfonos móviles de los integrantes de la banda criminal iniciado en el caso práctico 1.
>
>Recordamos que los miembros de la banda eran:
>• Capo. Jefe de la banda.
>• Matón. Encargado de asuntos “delicados”.
>• Mulero. Miembro reciente de la banda. Apareció muerto cerca de un centro comercial.
>
>Analizando la información disponible en las adquisiciones lógicas y en el downgrade de aplicaciones, trata de contestar las siguientes preguntas sobre los 3 implicados, aportando las capturas de pantallas que lo demuestren (1 punto por pregunta).

---

Las capturas estan realizadas tanto en una máquina Kali Linux (entorno xfce) como en un escritorio de EndeavourOS (entorno hyprland).shasu

>1. Comprueba si el hash del zip es correcto:
>SHA-1 = 37D9D64A5868AAE3E420E07149C37A74C9114916

![[Pasted image 20250320200114.png]]

El hash coincide

---
### Capo

>2. Capo mantiene varias conversaciones por WhatsApp con Mulero (Mulligan Dous). En la primera dice que tiene que ir cerca de Madrid a coger un coche. ¿Dónde tiene que cogerlo exactamente?

Encontramos en el chat :

![[Pasted image 20250320201115.png]]

Podemos asumir que es Mulero ya que el "Sending Party JID" es 34672926923@s\[.\]whatsapp\[.\]net, al igual que en el apartado de contactos:

![[Pasted image 20250320201240.png]]

Donde vemos el  mismo JID asociado a Mulligan Dous.

Cogera el coche exactamente en:
Cruz de la Horca Av. Felipe II, 23, 28280 El Escorial, Madrid

Con el enlace de Google Maps de:
https://maps.google.com/?cid=13241617964063143999&hl=es&gl=es

Con las coordenadas Geograficas:
40°34'59.7"N 4°07'18.4"W

>3. ¿En qué localización exacta debe dejar Mulero unas bolsas de deporte?

Se le indica que las entregue en Perillo:

![[Pasted image 20250320201522.png]]

Mas adelante vemos que se le indica:

![[Pasted image 20250320201731.png]]

Es decir, debe entregarlas en frente de la Oficina de Correos Rúa Zaire, 9, 15172 Perillo, A Coruña.

Enlace de maps: https://goo.gl/maps/UzDq9ud3Xz5ATtkT8

>4. El 6 de octubre a media tarde, Capo le mandó un mensaje de voz por WhatsApp a Mulero echándole una bronca por algo. Recupera el fichero de audio y escucha el mensaje. ¿Por qué le echa la bronca?

En el audio menciona:

"Eso es cosa de Mateo, tu no te metas y haz tu trabajo y limitate a eso, no hagas preguntas"

Es decir, la bronca es causa de hacer demasiadas preguntas sobre el trabajo.

>5. Por la última serie de mensajes de Whatsapp disponibles en el móvil de Capo. ¿Quién parece ser que mató a Mulero?

![[Pasted image 20250320202237.png]]
![[Pasted image 20250320202259.png]]

Se trata de Capo hablando con el usuario con JID 34672921162@s\[.\]whatsapp\[.\]net

En un mensaje, admite culpa:

```
Quién me vio? Como me enteré va a saber!! Si no había nadie cago en todo!!!!
```

Si contrastamos el JID con los contactos, podemos ver que es Mathew:

![[Pasted image 20250320202437.png]]

---
## Mulero

>6. Mulero sacó dos fotos con la cámara del móvil en su fiesta de cumpleaños en la playa. ¿Podrías decir en qué playa se celebró la fiesta?

Busacmos imagenes compartidas en la carpeta de evidencia de Mulero. Localizo la imagen en el sistema de archivos:

![[Pasted image 20250321165008.png]]

Y la analizo con exiftool:

![[Pasted image 20250321165115.png]]

Si buscamos las coordenadas en maps: 43.503611, -8.319444

Se trata de la plaia en O Outeiro, Ferrol 

![[Pasted image 20250321165352.png]]

>7. Mulero estaba interesado en invertir en criptomonedas y visitó algunas páginas web con información al respecto. ¿Qué páginas visitó?

En las cookies de firefox podemos ver multiples que pertenecen a una academia de trading llamada novatostradingclub.com:

![[Pasted image 20250321170048.png]]

En la ruta /home/kali/AFDM/ALEAPP_Reports_2025-03-20_Thursday_200709/

---
### Matón

>8. El día 7 de octubre de 2023, Matón intercambió varios mensajes con Capo por Telegram (Usuario en Telegram: Ernesto Capote), sobre un chivatazo recibido. En el tercer mensaje del día Capo le envía una localización de una calle a las afueras de Ourense. ¿Eres capaz de recuperar la localización de los mensajes de Telegram y decir qué calle es?

Podemos ver los datos de telegram en /home/kali/AFDM/Maton/APK Downgrade/org.telegram.messenger/apps/org.telegram.messenger/files/cache4.db y voy a la table messages_v2. En el apartado data podemos ver los mensajes:

![[Pasted image 20250321172135.png]]

Con chatGPT extraigo el link facilmente:

![[Pasted image 20250321172208.png]]

Se trata de: https://maps.app.goo.gl/GTBT9atyWAoH8UJ19

![[Pasted image 20250321172250.png]]

Se trata de Rúa do Castelo Ramido, Ourense.


>9. En los últimos mensajes de Telegram intercambiados entre Matón y Capo se podría deducir quién mató a Mulero. ¿Quién fue y cuándo lo hizo?

Podemos ver una serie de mensajes:

![[Pasted image 20250321173413.png]]
![[Pasted image 20250321173430.png]]
![[Pasted image 20250321173544.png]]
![[Pasted image 20250321173554.png]]

Podemos entender que es Matón quien realizo el asesinato y que fue el 2023-10-16 (ya que menciona que fue "ayer")

>10. Ahora que sabemos la fecha del asesinato, mira en las fotos sacadas con el móvil de Matón ese día a ver si nos da una pista del sitio donde se produjo. ¿Puedes indicar la localización exacta?

Veamos las imagenes de la evidencia de Maton:

![[Pasted image 20250321173905.png]]

Muchas de las imagenes tienen la fecha del asesinato. Utilicemos exiftool con una de ellas para ver si encontramos las coordenadas:

![[Pasted image 20250321174020.png]]

Se trata de: 43.505950, -8.205110

Viendolo en earth:

![[Pasted image 20250321174231.png]]

Se trata de la Rúa Petrolero Arteaga, en A Pallota, Ferrol. En frente del Centro Comercial "Parque Ferrol"

---
## Herramientas

>DB Browser for SQLite: https://sqlitebrowser.org/
>ALEAPP: https://github.com/abrignoni/ALEAPP