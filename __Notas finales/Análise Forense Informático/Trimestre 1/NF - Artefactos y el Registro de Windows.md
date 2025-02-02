
Parte de [[NF - Análise Forense Informático]]

Un **artefacto** es todo aquel elemento del sistema que pueda determinar cualquier tipo de actividad en el o del sistema.

Puede ser de dos tipos:
- De actividad del sistema
- De actividad del usuario

Algunos ejemplos son:
- Particiones, Sistemas de archivos y MFT
- Hives del registro
- Logs de eventos
- Ficheros de prefetch
- Shellbags
- Accesos directos LNK
- Jump Lists
- Papelera de reciclaje
- Logs de aplcicaciones
- Metadatos de media y documentacion
- Ficheros de hibernacion
- Volume Shadow Copies
- Thumbcache
- Windows Indexing Service
- Cortana (Busquedas)
- Centro de notificaciones
- Picture Password
- Backups (smartphone)

---

El registro es una base de datos jerarquica que contiene el conjunto de configuraciones del sistema, esta configuracion esta distribuida en varios ficheros

Se trata de una alternativa a los ficheros .ini ya que eran compartidos por todos los usuarios.

Contienen la siguiente informacion:
- Perfiles de los usuarios
- Aplicaciones instaladas
- Tipos de documentos con los que trabaja cada app
- Configuracion de las hojas de propiedades para carpetas
- Iconos de aplicaciones
- Elementos de hardware que hay en el sistema
- Puertos que se estan utilizando

Las entradas del registro se llaman claves, y cuenta con 7 claves raiz:

- HKEY_LOCAL_MACHINE (HKLM): Contiene informacion de configuracion especifica del equipo
- HKEY_CURRENT_CONFIG (HKCC): Contiene informacion acerca del perfil de hardware que utiliza el equipo local cuando se inicia el sistema
- HKEY_CLASSES_ROOT (HKCR): (Realmente es una subclave de HKEY_LOCAL_MACHINE) Almacena informacion que garantiza que cuando se abra un archivo con el explorador de windows, se hara con el programa correcto.
- HKEY_CURRENT_USER (HKCU): (Es una subclave de HKEY_USERS) Contiene la raiz de la informacion de configuracion del usuario que ha iniciado sesion. Esta info esta asociada al perfil del usuario
- HKEY_USERS (HKU): Contiene todos los perfiles de usuario cargados activamente en el equipo
- HKEY_PERFORMANCE_DATA: Solo en las version de Windows basadas en NT. Proporciona informacion sobre el rendimiento del sistema en tiempo real
- HKYN_DYN_DATA: Esta obsoleta, solo existe en Windows 9x/Me. Es visible en el editor del registro de Windows

Asi mismo, el registro esta formado por multitud de ficheros:
- SystemRoot/System32/config/
	- DEFAULT
	- SAM
	- SECURITY
	- SOFTWARE
	- SYSTEM
	- SystemRoot (suele ser C:/Windows)
- UserProfile/
	- NTUSER.DAT

Pero, la localizacion de los datos de usuario varia en Windows 8:
- SystemRoot/ServiceProfiles/networkProfiles/nombreDeUsuario
- Los archibos auxiliares para HKEY_CURRENT_USER estan en la carpeta SystemRoot/Profiles/nombreDeUsuario
Las extensiones de los archivos de estas carpetas indican el tipo de datos que contienen (La falta de extension tambien puede indicar el tipo de datos)

Existen muchas herramientas para analizar el registro, muchas de ellas creadas por Eric Zimmermann, nosotros utilizamos Windows Registry Recovery, que esta desarrollada por MITEC.

---

Algunos artefactos importantes:

Aplicaciones al inicio:
- Es una forma típica de persistir malware

Listas MRU (Most recently used):
- Info sobre todos los ficheros que se han abierto o modificado recientemente, lo que se considera recientemente depende de la versión de Windows. NO APLICA a ficheros de Office.

Shellbags:
- Lugares donde el SO almacena la información relativa a las preferencias de visualización de contenidos en el Explorador de Windows, las rutas son distintas entre versiones de Windows.

Papelera de reciclaje:
- Cuando borramos un archivo la papelera guarda el archivo en si y metainformación sobre este, como su ubicación inicial
- Antes de windows vista por defecto almacenaba un 10% del total de la cueota de los usuarios
- En windows vista almacenaba el 10% del total de la cuota de los usuario +5% del resto de la cuota, si esta llega a su máximo se van borrando archivos por antigüedad. Los archivos más grandes se borran automáticamente

Prefetching:
- Carpeta introducida en Windows XP que guarda información sobre las aplicaciones para acelerar su arranque
- En Windows Vista se añadio el SuperFetch, que ademas carga en memoria las librerias de uso común para cargar más rápido
- ReadyBoost es un software que permite usar una SD card, memoria USB etc como cache.
- No viene activado en Windows Server
- Suele estar desactivado en Windows SSD
- El contenido es una evidencia ya que permite saber cuando se lanzaron ciertas apps por última vez

Logs:
- Dan información en general sobre múltiple acciones
- (Ubicaciones relevantes en diapositivas)

- Historial de navegadores
	- Se almacenan en ciertos ficheros que varian por navegador