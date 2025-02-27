Parte de [[Analisis Forense de Dispositivos Moviles]]

Es una disciplina muy relevante ya que los móviles son muy predominantes. El 85% del malware se crea con móviles como objetivo. Hay nuevas formas de ataque como el juice jacking.
(El juice jacking es acceder a los datos del móvil mediante cargadores USB falsos)

Se pueden obtener datos como los hábitos de vida del usuario.

El analisis forense en moviles se haria:
- Tras un delito o incidente de seguridad
- En una auditoria de seguridad
	- Mantenimiento de la privacidad, transmisiones de datos seguras...
	- Revisar el cumplimiento de regulaciones y estandares
	- Verificar que se hace un uso correcto del dispositivo

Tienen peculiaridades:
- Antes todos eran un entorno cerrado
- Tienen datos nuevos como el SMS
- Tienen localizaciones, mensajes, emails...
- Algun dispositivos IOT como los wearables tienen informacion extra por ejemplo sanitaria
- El SO son mayoritariamente Android e iOS
- Hay millones de aplicaciones y muchas se desarrollan para durar solo un tiempo limitado
- Esto todo genera nuevas formas de destruccion, ocultacion y falsificacion de las evidencias (por ejemplo el cambio de ROMs de arranque mediante un bootloader)
- Es más dificil completar las consideraciones legales para mantener la legalidad de las evidencias
- Tienen mayor proteccion y cifrado por defecto:
	- Desbloqueo del dispositivo (a veces ni se puede acceder por cable)
	- Cifrado del almacenamiento (No se puede leer ni accediendo fisicamente al chip)
	- Remote Wipe (Borrado de evidencias sin tener acceso fisico)

Las metodologías son identicas a las de PCs y discos duros. 

En cuanto a preparacion:
- Puede requerir una actuacion mas rapida:
	- Evitar la modificacion o el borrado remoto
- Evitar que se quede sin alimentacion electrica
- Es mas probable encontrar moviles sumergidos que PC
	- Si el movil esta sumergido:
		- Apagar y quitar bateria si es posible
		- Sumergirlo en alcohol isopropilico para quitar el agua
		- Aplicar papel secante (o avena, arroz)
	- Y tener en cuenta:
		- No usar secadores ni otras fuentes de calor
		- El agua salada es mucho mas corrosiva que la dulce, siendo mas probable que no podamos hacer nada

La adquisicion:

- Depende mucho:
	- Del tipo del dispositivo
	- De las versiones de hardware y software
	- De la configuracion del dispositivo
		- Si esta rooteado, apagado, bloqueado, debloqueado, encendido...
	- Tipos de memoria a adquirir y su volatilidad

Podemos hacer 3 tipos de adquisicion:
- Manual: La mas basica, haciendo capturas y fotos usando el dispositivo directamente
	- Ventajas:
		- No requiere herramientas
		- Informacion facil de entender para no expertos
	- Desventajas:
		- Solo es posible si el dispositivo esta desbloqueado
		- Solo se puede acceder a datos que aparezcan en pantalla
		- Se puede modificar la informacion
		- Lleva mucho mas tiempo procesar las evidencias
- Logica: Copiar archivos y configuracion del sistema
	- Ventajas: 
		- Facil de obtener, no requiere hardware especifico
		- A vece se puede hacer desde otro dispositivo sin emplear las API del movil
	- Desventajas:
		- Si usa las API del movil, para por el SO comprometido
		- ...
- Fisica: La similar a PCs, copia bit a bit
	- Ventajas:
		- Acceso a algunos archivos borrados, espacio no usado etc
	- Desventajas:
		- Es complejo
		- No siempre es factible
		- Requiere acceso completo al almacenamiento, lo cual no siemple es posible
		- A veces hay que emplear exploits para saltarnos la seguridad y poder acceder

Tipos de almacenanmiento:

- Son tipicamente todos flash NAND
- Antes se empleaba flash NOR
- Las tarjetas de memoria (generalmente SD) suelen usar memorias NAND y estar formateadas en FAT32
	- Iphone/iOS no permite su uso
	- Los otros fabricantes, depende del dispositivo

Acceso según el estado del dispositivo:

Si esta desbloqueado:

- Garantizar alimentacion electrica y aislarlo de la red:
	- Modo avion
	- Quitar la SIM
- Tratar de garantizar el acceso fisico
	- Desactivar el codigo de bloqueo si es posible
	- Activar el debugging USB
	- Desactivar o retrasar el bloqueo por inactividad
- Meterlo en una bolsa de Faraday que lo aisle de la radiacion electromagnetica
- Obtener tarjetas SD, backups en PC asociados, etc.

Si esta bloqueado:

- Aislarlo de la red
	- Modo avion
	- Extraer SIM
- Comprobar si el debugging USB esta activo
	- Si lo esta, tratar e cargar un bootloader para cambiar el inicio y activar acceso fisico al terminal (esto tiende a no funcionar, y el movil puede eliminar los datos si detecta un bootloader)
	- Si no lo esta, tratar de extraer el codigo de bloqueo (smudge attack, fuerza bruta, vulnerabilidades, etc.)
- Meterlo en una bolsa de Faraday
- Obtener tarjetas SD, backups en PC asociados...

Si el despositivo esta apagado:
- Quitar los dispositivos extraibles
- Encender el telefono
- Continuar como mediante en el caso de dispositivo bloqueado

Hay alternativas de pago que nos permiten obtener el codigo de inicio. Como el Cellebrite UFED.

En cuanto a herramientas de adquisicion, estan las de MSAB (XRY Physical, XRY Logical, XRY Pinpoint (para moviles asiaticos), XRY Cloud...). Tambien existe MOBILedit, SIM Cloning Tool etc.

En cuanto a software libre existe Avilla Forensics (se centra en downgradear apps hasta llegar a versiones vulnerables para acceder a los datos)

Por ultimo podemos operar a bajo nivel mediante ADB Backup con dd para clonar. Hay tambien pequeñas herramientas de downgrade para acceder a datos privados de ciertas apps.

Si no somos root siempre se extraen muchos menos datos.

---

- El IMEI Es un codigo de 15 digitos que identifica el telefono:
	- Pais de fabricacion del telefono
	- Fabricante
	- Numero de serie del telefono
	- Digito de control
- Se puede obtener marcando ```*#06#```

---

## Artefactos de moviles:

Hay muchismos, y mas sencillos que en windows:

- Contactos
- Cuentas de usuario
- Historial de llamadas
- SMS
- Correos electronicos
- Aplicaciones instaladas
- Historial de busqueda
- Historial de navegacion
- Cache del teclado
- Datos de los sensores del dispositivo
- Calendario
- Documentos
- Credenciales de redes Wifi
- ...

