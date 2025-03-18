Parte de [[Splunk]]

>**Pregunta 1**

  >Tiene la tarea de encontrar los usuarios de IAM (Identity & Access Management) que accedieron a un servicio de AWS en el entorno de AWS de Frothly.
  
> ¿Enumere los usuarios de IAM que accedieron a un servicio de AWS (con o sin éxito) en el entorno de AWS de Frothly?

index="botsv3" sourcetype="aws:cloudtrail"

Y vemos el campo userIndetity.userName:

splunk-access
web_admin
bstoll
btun

>**Pregunta 2**

>¿Qué campo usaría para alertar que la actividad de la API de AWS se ha producido sin MFA (autenticación multifactor)? Guía de respuesta: Proporcione la ruta JSON completa. (Ejemplo: helado.sabores.tradicional)

index="botsv3" sourcetype="aws:cloudtrail" "\*MFA\*"

Y vemos el campo userIdentity.sessionContext.attributes.mfaAuthenticated

Si vemos las peticiones vemos que el campo es la ruta JSON, es decir:

userIdentity.sessionContext.attributes.mfaAuthenticated


>**Pregunta 3**

>Mire los tipos de fuente disponibles en el conjunto de datos. Puede haber uno en particular que contenga información sobre el hardware, como los procesadores.

index="botsv3" "i7"

Nos revela que podemos utilizar el WInHostMon

Con index="botsv3" source="hardware"

Descubrimos que la CPU del servidor web es:

Intel Xeon CPU E5-2676

>Pregunta 4

>Bud accidentalmente hace que un cubo S3 sea accesible públicamente. ¿Cuál es el ID de evento de la llamada a la API que habilitó el acceso público? Guía de respuesta: incluya cualquier carácter especial/puntuación.



>Pregunta 5

>¿Cuál es el nombre de usuario de Bud?



>Pregunta 6

>¿Cuál es el nombre del depósito S3 que se hizo públicamente accesible?



>Pregunta 7

>¿Cuál es el nombre del archivo de texto que se cargó correctamente en el depósito de S3 mientras era de acceso público? Guía de respuesta: Proporcione solo el nombre y la extensión del archivo, no la ruta completa. (Ejemplo: filename.docx en lugar de /mylogs/web/filename.docx)



>Pregunta 8

>¿Cuál es el FQDN del extremo que ejecuta una edición del sistema operativo Windows diferente a las demás?