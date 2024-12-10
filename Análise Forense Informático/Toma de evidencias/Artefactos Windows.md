Parte de [[Analise Forense]]

>Son los diferentes elementos del sistema que pueden determinar la actividad de un malware o de un usuario malicioso, así como las evidencias necesarias para una prueba

Dos tipos:
- Actividad del sistema
- Actividad del usuario

![[Pasted image 20241209205222.png]]

---
## El registro

Una base de datos jerárquica que contiene el conjunto de configuraciones del sistema, Toda esta configuración está distribuida en varios ficheros.

Es una alternativa a los ficheros .INI ya que eran compartidos por todos los usuarios.

Información que contiene:
- Perfiles de los usuarios
- Aplicaciones instaladas
- Tipos de documentos con los que trabaja cada app
- Configuraciones de las hojas de propiedades para carpetas
- Iconos de aplicaciones
- Elementos de hardware que hay en el sistema
- Puertos que se están utilizando

Hay 7 claves raíz:

![[Pasted image 20241209205608.png]]![[Pasted image 20241209205615.png]]![[Pasted image 20241209205622.png]]

Ficheros que componen el registro:

![[Pasted image 20241209210025.png]]![[Pasted image 20241209210034.png]]

Tambien existen relaciones entre el registro y archivos auxiliares

Herramientas para analizar el registro:

![[Pasted image 20241209210540.png]]

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